import os
import logging
import logging.config
import yaml

from datetime import datetime

LOG_DIR = "logs/application"

os.makedirs(LOG_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

log_file_name = f"{timestamp}.log"

log_file_path = os.path.join(LOG_DIR, log_file_name)

with open("config/logging.yaml", "r") as file:
    config = yaml.safe_load(file)

config["handlers"]["file"]["filename"] = log_file_path

logging.config.dictConfig(config)

logger = logging.getLogger("MarketMixLogger")
