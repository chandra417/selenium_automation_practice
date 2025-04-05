from time import sleep

import pytest, logging
from pages.locators.firstpagelocators import DynamicLocators

logger = logging.getLogger(__name__)

def test_dynamic_button(driver):
    toggle = driver.find_element(*DynamicLocators.dynamic_button)
    logger.info("Check button is selected")
    toggle.is_selected()
    logger.info("Check if is_selected is true")
    if toggle:
        toggle.click()
    else:
        toggle.click()
