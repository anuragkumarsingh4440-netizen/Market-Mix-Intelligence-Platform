import os
import sys

import pandas as pd

from sklearn.model_selection import train_test_split

from src.logger import logger
from src.exception import CustomException
from src.utils.common import read_yaml


class DataIngestion:

    def __init__(self):

        paths = read_yaml("config/paths.yaml")

        self.raw_data_path = paths["paths"]["raw_data_path"]

        self.train_data_path = paths["paths"]["train_data_path"]

        self.test_data_path = paths["paths"]["test_data_path"]

    def initiate_data_ingestion(self):

        logger.info("Data ingestion started")

        try:

            df = pd.read_csv(self.raw_data_path)

            logger.info("Dataset loaded successfully")

            os.makedirs(
                os.path.dirname(self.train_data_path),
                exist_ok=True
            )

            logger.info("Train-test split initiated")

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            train_set.to_csv(
                self.train_data_path,
                index=False
            )

            test_set.to_csv(
                self.test_data_path,
                index=False
            )

            logger.info("Train and test datasets saved successfully")

            return (
                self.train_data_path,
                self.test_data_path
            )

        except Exception as e:

            logger.error("Error occurred during data ingestion")

            raise CustomException(e, sys)