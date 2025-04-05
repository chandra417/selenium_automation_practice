from time import sleep

import pytest, logging
from pages.locators.firstpagelocators import DropdownLocators
from selenium.webdriver.support.ui import Select

logger = logging.getLogger(__name__)

def test_dropdown(driver):
    logger.info("Selecting country")
    drop_down = driver.find_element(*DropdownLocators.select_country)
    select = Select(drop_down)

    logger.info("Selecting india from the countries list")
    select.select_by_visible_text("India")

def test_select_multiple(driver):
    logger.info("Selecting colors")
    select = driver.find_element(*DropdownLocators.select_colors)
    select = Select(select)

    logger.info("Selecting red and green")
    select.select_by_visible_text("Red")
    select.select_by_visible_text("Green")

def test_animal_multiple(driver):
    logger.info("Selecting animals")
    select_animal = driver.find_element(*DropdownLocators.select_animals)
    select = Select(select_animal)

    logger.info("Selecting Elephant and Lion")
    select.select_by_visible_text("Elephant")
    select.select_by_visible_text("Lion")