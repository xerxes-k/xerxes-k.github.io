import os
import pathlib
import unittest

from selenium.webdriver.common.by import By

from selenium import webdriver


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        og = int(driver.find_element(By.TAG_NAME, "h1").text)
        increase = driver.find_element(By.ID, "increase")
        increase.click()
        self.assertEqual(int(driver.find_element(By.TAG_NAME, "h1").text), og+1)

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        og = int(driver.find_element(By.TAG_NAME, "h1").text)
        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(int(driver.find_element(By.TAG_NAME, "h1").text), og-1)

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        og = int(driver.find_element(By.TAG_NAME, "h1").text)
        increase = driver.find_element(By.ID, "increase")
        for i in range(3):
            increase.click()
        self.assertEqual(int(driver.find_element(By.TAG_NAME, "h1").text), og+3)



if __name__ == "__main__":
    unittest.main()
