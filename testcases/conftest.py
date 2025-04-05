import pytest, logging
from config.config import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def driver():
    serv_obj = Service(r'C:\Users\Administrator\Desktop\PYTHON\Selenium\Driver\Chrome\chromedriver-win64\chromedriver.exe')
    logger.debug("Initializing ChromeDriver")
    chrome_driver = webdriver.Chrome(service=serv_obj)
    chrome_driver.get(config.BASE_URL)
    chrome_driver.maximize_window()
    yield chrome_driver
    logger.debug("Quitting ChromeDriver")
    chrome_driver.quit()