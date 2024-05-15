from selenium import webdriver
from selenium.webdriver.common.by import By
from src.config.setting import configure_drivers, apply_stealth
from src.parsers.avito_parser import parse_avito_apartments

options = configure_drivers()

driver = webdriver.Chrome(options=options)

apply_stealth(driver)

parse_avito_apartments(driver, By)


driver.quit()
