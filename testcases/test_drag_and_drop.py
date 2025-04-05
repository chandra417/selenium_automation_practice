from time import sleep
import pytest, logging
from selenium.webdriver.common.action_chains import ActionChains
from pages.locators.firstpagelocators import DragAndDropLocators
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)

def test_drag_and_drop(driver):
    logger.info("Testing drag and drop!")
    source = driver.find_element(*DragAndDropLocators.source)
    destination = driver.find_element(*DragAndDropLocators.destination)

    mouse = ActionChains(driver)
    logger.info("Performing drag and drop!")
    mouse.drag_and_drop(source, destination).perform()

def test_slider(driver):
    logger.info("Testing slide bar!")
    slide_start = driver.find_element(*DragAndDropLocators.slide_start)
    slide_end = driver.find_element(*DragAndDropLocators.slide_end)

    mouse = ActionChains(driver)
    logger.info("Performing slide bar!")
    mouse.drag_and_drop_by_offset(slide_end, +100, 0).perform()
    mouse.drag_and_drop_by_offset(slide_start, +100, 0).perform()

def test_scrolling(driver):
    logger.info("Scrolling tests")
    logger.info("Scroll to Bottom of Page")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scroll to Bottom of Page
    logger.info("Scroll to Top of Page")
    driver.execute_script("window.scrollTo(0, 0);")                             # Scroll to Top of Page
    element = driver.find_element(By.XPATH, "//*[name()='circle' and contains(@cx,'15')]")
    logger.info("Scroll till specific element")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(4)

    driver.find_element(*DragAndDropLocators.scroll_down).click()
    scroll_list = driver.find_element(*DragAndDropLocators.scroll_down_list)
    logger.info("Scroll till specific element with text Item 26")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_list)
    scroll_list.click()
