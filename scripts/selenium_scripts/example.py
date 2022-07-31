import json
import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def example_task(selhook):
    driver = selhook.driver
    driver.get("http://www.python.org")
    logging.info(f"Title - {driver.title}")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
