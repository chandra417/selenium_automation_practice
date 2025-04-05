import logging
import os
from datetime import datetime

class config:
    BASE_URL = "https://testautomationpractice.blogspot.com/"

def configure_logging():
    log_dir = r"C:\\Users\\Administrator\\Desktop\\PYTHON\\Selenium\\selenium_automation_practice\\reports\\logs"
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Get current timestamp for log filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = f'{log_dir}/automation_{timestamp}.log'

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    # Set selenium and urllib3 logging levels to WARNING to reduce noise
    logging.getLogger('selenium').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)


# Call the configuration function when the module is imported
configure_logging()


