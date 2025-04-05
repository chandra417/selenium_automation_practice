import logging, pytest
from pages.locators.firstpagelocators import HandlingPaginationTabel

logger = logging.getLogger(__name__)

def test_pagination(driver):
    logger.info("Testing pagination web tabs")
    pages = driver.find_elements(*HandlingPaginationTabel.pages)
    for each_page in pages:
        logger.info("Click on pagination")
        each_page.click()
        names = driver.find_elements(*HandlingPaginationTabel.names_in_each_page)
        for each_name in names:
            logger.info(f"Names on the table: {each_name.text}")