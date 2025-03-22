import os, pathlib, unittest
from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

