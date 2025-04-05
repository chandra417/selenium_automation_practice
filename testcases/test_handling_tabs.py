from time import sleep

import pytest, logging
from pages.locators.firstpagelocators import HandlingTabsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


def test_handling_tabs(driver):
    logger.info("Wiki searching with laptops")
    driver.find_element(*HandlingTabsLocators.wiki_search_bar).send_keys("laptops")
    driver.find_element(*HandlingTabsLocators.wiki_search_button).click()

    logger.info("Wait until the search result appears")
    all_links = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located(HandlingTabsLocators.search_results)
    )

    main_window = driver.current_window_handle
    for each_link in all_links:
        logger.info(f"Opening new tab {each_link.get_property('href')}")
        each_link.click()
        driver.switch_to.window(main_window)

    window_handle = driver.window_handles
    for each_handle in window_handle:
        if each_handle != main_window:
            driver.switch_to.window(each_handle)
            logger.info(f"page title :{driver.title}")
            driver.close()
    driver.switch_to.window(main_window)

def test_new_tab_button(driver):
    main_window = driver.current_window_handle
    logger.info("Click on the new tab button!")
    driver.find_element(*HandlingTabsLocators.new_tab).click()

    all_windows = driver.window_handles
    for each_handle in all_windows:
        if each_handle != main_window:
            driver.switch_to.window(each_handle)
            logger.info(f"the title of the new page is {driver.title}")
            driver.close()
    logger.info("Switching back to main window")
    driver.switch_to.window(main_window)

def test_popup_window(driver):
    main_window = driver.current_window_handle
    logger.info("CLick on the popup window!")
    driver.find_element(*HandlingTabsLocators.popup_window).click()

    all_windows = driver.window_handles
    for each_handle in all_windows:
        if each_handle != main_window:
            driver.switch_to.window(each_handle)
            logger.info(f"the title of the new page is {driver.title}")
            driver.close()
    logger.info("Switching back to main window")
    driver.switch_to.window(main_window)