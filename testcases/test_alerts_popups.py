from time import sleep

import pytest, logging
from pages.locators.firstpagelocators import AlertsAndPopupsLocators
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

logger = logging.getLogger(__name__)


def test_simple_alert(driver):
    logger.info("Accepting simple alert")
    driver.find_element(*AlertsAndPopupsLocators.simple_alert).click()

    alert = Alert(driver)
    alert_text = alert.text
    logger.info(f"Alert text is \"{alert_text}\"")
    alert.accept()
    # OR
    # alert.dismiss()


def test_confirm_alert(driver):
    logger.info("Check and confirm alert button")
    driver.find_element(*AlertsAndPopupsLocators.confirm_alert).click()

    alert = Alert(driver)
    alert_text = alert.text

    if alert_text == "Press a button!":
        alert.accept()
    else:
        alert.dismiss()

    logger.info("Validating text after confirm alert")
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AlertsAndPopupsLocators.after_confirm_alert)
    )

    if element.text == "You pressed OK!":
        logger.info(f"Text in the alert is {element.text} and you pressed ok")
    else:
        logger.info(f"Text in the alert is {element.text} and you pressed cancel")

def test_prompt_alert(driver):
    pass
    # logger.info("Entering value in prompt alert")
    # driver.find_element(*AlertsAndPopupsLocators.prompt_alert).click()
    # sleep(1)
    # alert_window = driver.switch_to.alert
    # sleep(1)
    # print(alert_window.text)
    # sleep(1)
    # alert_window.send_keys("welcome!")
    # alert_window.accept()
    # sleep(1)

