import pytest, time, logging
from pages.locators.firstpagelocators import AddressLocators

logger = logging.getLogger(__name__)
def test_input_basic_details(driver):
    logger.info("Enter name into enter name search bar")
    driver.find_element(*AddressLocators.enter_name).send_keys("Chandrasekhar")

    logger.info("Enter email into enter email search bar")
    driver.find_element(*AddressLocators.enter_email).send_keys("chandu@gmail.com")

    logger.info("Enter phone into enter phone search bar")
    driver.find_element(*AddressLocators.enter_phone).send_keys("9632963250")

    logger.info("Enter address into enter address search bar")
    driver.find_element(*AddressLocators.enter_address).send_keys("Vani Towers, Narasaraopet, Gunur")


