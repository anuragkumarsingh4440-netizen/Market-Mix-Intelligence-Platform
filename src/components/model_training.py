import mlflow
import mlflow.sklearn
import os
import sys

import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)

import joblib

from src.logger import logger
from src.exception import CustomException


class ModelTrainer:

    def __init__(self):

        self.model_path = "artifacts/model.pkl"

    def evaluate_model(self, true, predicted):

        r2 = r2_score(true, predicted)

        mae = mean_absolute_error(true, predicted)

        rmse = np.sqrt(mean_squared_error(true, predicted))

        return r2, mae, rmse

    def initiate_model_training(

        self,

        train_array,
        test_array,
        train_target,
        test_target
    ):

        try:

            logger.info("Model training started")

            models = {

                "LinearRegression": LinearRegression(),

                "RandomForest": RandomForestRegressor(
                    random_state=42
                )
            }

            model_report = {}

            for model_name, model in models.items():

                with mlflow.start_run(run_name=model_name):

                    logger.info(f"Training model: {model_name}")

                    model.fit(
                        train_array,
                        train_target
                    )

                    predicted = model.predict(test_array)

                    r2, mae, rmse = self.evaluate_model(
                        test_target,
                        predicted
                    )

                    mlflow.log_param(
                        "model_name",
                        model_name
                    )

                    mlflow.log_metric(
                        "r2_score",
                        r2
                    )

                    mlflow.log_metric(
                        "mae",
                        mae
                    )

                    mlflow.log_metric(
                        "rmse",
                        rmse
                    )

                    mlflow.sklearn.log_model(
                        model,
                        artifact_path=model_name
                    )

                    model_report[model_name] = {

                        "R2 Score": r2,
                        "MAE": mae,
                        "RMSE": rmse
                    }

                    logger.info(
                        f"{model_name} Evaluation Completed"
                    )

            best_model_name = max(
                model_report,
                key=lambda x: model_report[x]["R2 Score"]
            )

            best_model = models[best_model_name]

            logger.info(
                f"Best model found: {best_model_name}"
            )

            joblib.dump(
                best_model,
                self.model_path
            )

            logger.info(
                "Best model saved successfully"
            )

            return model_report

        except Exception as e:

            logger.error(
                "Error occurred during model training"
            )

            raise CustomException(e, sys)