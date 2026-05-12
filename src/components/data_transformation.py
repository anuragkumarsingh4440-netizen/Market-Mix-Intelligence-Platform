import os
import sys

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import joblib

from src.logger import logger
from src.exception import CustomException
from src.utils.common import read_yaml


class DataTransformation:

    def __init__(self):

        paths = read_yaml("config/paths.yaml")

        self.train_data_path = paths["paths"]["train_data_path"]

        self.test_data_path = paths["paths"]["test_data_path"]

        self.preprocessor_path = "artifacts/preprocessor.pkl"

    def get_data_transformer_object(self):

        try:

            logger.info("Creating preprocessing pipeline")

            numerical_columns = [
                "spend",
                "impressions",
                "clicks",
                "conversions",
                "ctr",
                "roas"
            ]

            numerical_pipeline = Pipeline(
                steps=[
                    ("scaler", StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline",
                     numerical_pipeline,
                     numerical_columns)
                ]
            )

            logger.info("Preprocessing pipeline created successfully")

            return preprocessor

        except Exception as e:

            raise CustomException(e, sys)

    def initiate_data_transformation(self):

        try:

            logger.info("Data transformation started")

            train_df = pd.read_csv(self.train_data_path)

            test_df = pd.read_csv(self.test_data_path)

            preprocessing_object = self.get_data_transformer_object()

            target_column = "revenue"

            input_feature_train_df = train_df.drop(
                columns=[target_column],
                axis=1
            )

            target_feature_train_df = train_df[target_column]

            input_feature_test_df = test_df.drop(
                columns=[target_column],
                axis=1
            )

            target_feature_test_df = test_df[target_column]

            logger.info("Applying preprocessing transformations")

            input_feature_train_arr = preprocessing_object.fit_transform(
                input_feature_train_df
            )

            input_feature_test_arr = preprocessing_object.transform(
                input_feature_test_df
            )

            joblib.dump(
                preprocessing_object,
                self.preprocessor_path
            )

            logger.info("Preprocessor object saved successfully")

            return (
                input_feature_train_arr,
                input_feature_test_arr,
                target_feature_train_df,
                target_feature_test_df,
                self.preprocessor_path
            )

        except Exception as e:

            logger.error("Error occurred during data transformation")

            raise CustomException(e, sys)