import logging, pytest
from pages.locators.firstpagelocators import MouseHoverLocators
from selenium.webdriver.common.action_chains import ActionChains

def test_mouse_hover(driver):
    logging.info("Testing mouse-hover")
    mouse = ActionChains(driver)
    point_me = driver.find_element(*MouseHoverLocators.mouse_hover)
    laptops = driver.find_element(*MouseHoverLocators.mouse_hover_laptops)
    logging.info("Mouse-hover to laptops")
    mouse.move_to_element(point_me).move_to_element(laptops).perform()
    laptops.click()

def test_double_click(driver):
    logging.info("Testing double click")
    mouse = ActionChains(driver)

    text = "Welcome!"
    logging.info(f"Enter text {text} into field1")
    field = driver.find_element(*MouseHoverLocators.field_1)
    field.clear()
    field.send_keys(text)

    copy_text = driver.find_element(*MouseHoverLocators.double_click)
    logging.info("Performing double click")
    mouse.double_click(copy_text).perform()

    logging.info("Validating double click action!")
    field1 = driver.find_element(*MouseHoverLocators.field_1).text
    field2 = driver.find_element(*MouseHoverLocators.field_2).text

    if field1 == field2:
        logging.info("Double click action successful!")
    else:
        logging.info("Double click action unsuccessful!")