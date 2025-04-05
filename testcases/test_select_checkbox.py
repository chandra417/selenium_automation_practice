import pytest, logging, time
from pages.locators.firstpagelocators import CheckboxLocators

logger = logging.getLogger(__name__)

def test_choose_checkboxes(driver):
    logger.info("Selecting male checkbox")
    driver.find_element(*CheckboxLocators.select_male).click()

    logger.debug("select days from checkbox")
    days_element = driver.find_elements(*CheckboxLocators.select_days)

    selected_days = ["sunday", "friday"]
    for each_day_element in days_element:
        property = each_day_element.get_property("value")
        if property in selected_days:
            logger.info(f"selecting {property} from checkbox")
            each_day_element.click()
