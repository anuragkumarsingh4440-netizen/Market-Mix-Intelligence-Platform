from dataclasses import dataclass


@dataclass
class TrainingPipelineConfig:

    artifacts_dir: str


@dataclass
class DataIngestionConfig:

    train_data_path: str

    test_data_path: str

    raw_data_dir: str