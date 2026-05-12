from src.logger import logger

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer


logger.info("MarketMix Pipeline Started")


data_ingestion = DataIngestion()

train_path, test_path = data_ingestion.initiate_data_ingestion()


logger.info(f"Train file saved at: {train_path}")

logger.info(f"Test file saved at: {test_path}")


data_validation = DataValidation()

validation_status = data_validation.initiate_data_validation()


logger.info(f"Validation Status: {validation_status}")


data_transformation = DataTransformation()

(
    train_arr,
    test_arr,
    train_target,
    test_target,
    preprocessor_path
) = data_transformation.initiate_data_transformation()


logger.info(
    "Data transformation completed successfully"
)


model_trainer = ModelTrainer()

model_report = model_trainer.initiate_model_training(
    train_arr,
    test_arr,
    train_target,
    test_target
)


logger.info(f"Model Report: {model_report}")