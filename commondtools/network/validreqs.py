"""
Massive selenium requests.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Validreqs:
    """
    Validated selenium requests.
    """

    def __init__(self):
        pass

    @staticmethod
    def select_element(web_driver, element_name: str, element_type: str):
        """
        1. Check that it exists,
        2. select a web element,
        3. validate the selection,
        4. check for errors.

        :param web_driver: selenium webdriver instance
        :param element_name: name of the element. (id, class, name, xpath, css)
        :type element_name: str
        :param element_type: type of the element (id, class, name, xpath, css)
        :type element_type: str

        :return: bool: success of selection
        """
        WebDriverWait(web_driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()

        pass


if __name__ == "__main__":
    driver = webdriver.Firefox(
        executable_path="C:\\Users\\nagyd\\Downloads\\geckodriver-v0.28.0-win64\\geckodriver.exe")
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

    Validreqs.select_element(web_driver=driver, element_name="about", element_type="id")

    driver.close()
