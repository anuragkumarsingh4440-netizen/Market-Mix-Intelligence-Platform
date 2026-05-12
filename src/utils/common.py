import yaml

from src.logger import logger
from src.exception import CustomException

import sys


def read_yaml(file_path):

    try:

        with open(file_path, "r") as file:

            logger.info(f"Reading YAML file: {file_path}")

            content = yaml.safe_load(file)

            logger.info("YAML file loaded successfully")

            return content

    except Exception as e:

        raise CustomException(e, sys)