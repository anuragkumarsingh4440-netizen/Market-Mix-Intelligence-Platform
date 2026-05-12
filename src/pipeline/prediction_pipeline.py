import sys
import joblib
import pandas as pd

from src.logger import logger
from src.exception import CustomException


class PredictionPipeline:

    def __init__(self):

        self.model_path = "artifacts/model.pkl"

        self.preprocessor_path = "artifacts/preprocessor.pkl"

    def predict(self, features):

        try:

            logger.info("Loading model and preprocessor")

            model = joblib.load(self.model_path)

            preprocessor = joblib.load(
                self.preprocessor_path
            )

            logger.info("Transforming input data")

            transformed_data = preprocessor.transform(
                features
            )

            logger.info("Generating predictions")

            predictions = model.predict(
                transformed_data
            )

            return predictions

        except Exception as e:

            logger.error(
                "Error occurred during prediction"
            )

            raise CustomException(e, sys)


class CustomData:

    def __init__(

        self,

        spend,
        impressions,
        clicks,
        conversions,
        ctr,
        roas
    ):

        self.spend = spend

        self.impressions = impressions

        self.clicks = clicks

        self.conversions = conversions

        self.ctr = ctr

        self.roas = roas

    def get_data_as_dataframe(self):

        try:

            custom_data_input_dict = {

                "spend": [self.spend],

                "impressions": [self.impressions],

                "clicks": [self.clicks],

                "conversions": [self.conversions],

                "ctr": [self.ctr],

                "roas": [self.roas]
            }

            return pd.DataFrame(
                custom_data_input_dict
            )

        except Exception as e:

            raise CustomException(e, sys)