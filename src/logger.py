import logging
import os 
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # Only the logs folder
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Log file inside logs folder

logging.basicConfig(
    filename=LOG_FILE_PATH,  # <-- Use 'filename' instead of 'filemode'
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)