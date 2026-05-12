import os
import sys

import pandas as pd

from src.logger import logger
from src.exception import CustomException
from src.utils.common import read_yaml


class DataValidation:

    def __init__(self):

        paths = read_yaml("config/paths.yaml")

        self.train_data_path = paths["paths"]["train_data_path"]

        self.schema_path = "config/schema.yaml"

    def validate_columns(self, df, schema):

        logger.info("Column validation started")

        expected_columns = schema["columns"].keys()

        actual_columns = df.columns

        missing_columns = []

        for column in expected_columns:

            if column not in actual_columns:

                missing_columns.append(column)

        if len(missing_columns) > 0:

            logger.error(f"Missing columns: {missing_columns}")

            return False

        logger.info("Column validation successful")

        return True

    def validate_null_values(self, df):

        logger.info("Null value validation started")

        null_counts = df.isnull().sum()

        total_nulls = null_counts.sum()

        if total_nulls > 0:

            logger.warning(f"Total null values found: {total_nulls}")

            return False

        logger.info("No null values found")

        return True

    def validate_duplicates(self, df):

        logger.info("Duplicate validation started")

        duplicate_count = df.duplicated().sum()

        if duplicate_count > 0:

            logger.warning(f"Duplicate rows found: {duplicate_count}")

            return False

        logger.info("No duplicate rows found")

        return True

    def validate_business_rules(self, df):

        logger.info("Business rule validation started")

        if (df["spend"] < 0).any():

            logger.error("Negative spend values found")

            return False

        if (df["revenue"] < 0).any():

            logger.error("Negative revenue values found")

            return False

        logger.info("Business rule validation successful")

        return True

    def initiate_data_validation(self):

        try:

            logger.info("Data validation pipeline started")

            df = pd.read_csv(self.train_data_path)

            schema = read_yaml(self.schema_path)

            column_status = self.validate_columns(df, schema)

            null_status = self.validate_null_values(df)

            duplicate_status = self.validate_duplicates(df)

            business_status = self.validate_business_rules(df)

            validation_status = all([
                column_status,
                null_status,
                duplicate_status,
                business_status
            ])

            if validation_status:

                logger.info("Data validation completed successfully")

            else:

                logger.warning("Data validation failed")

            return validation_status

        except Exception as e:

            logger.error("Error occurred during data validation")

            raise CustomException(e, sys)