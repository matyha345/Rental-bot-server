from selenium import webdriver
from selenium.webdriver.common.by import By
from src.config.setting import configure_drivers, apply_stealth
from src.parsers.avito_parser import parse_avito_apartments
from src.database.connector import initialize_database


def main():
    # Инициализация базы данных
    initialize_database()

    # Конфигурация веб-драйвера
    options = configure_drivers()

    # Создание веб-драйвера
    driver = webdriver.Chrome(options=options)

    # Применение Stealth режима
    apply_stealth(driver)

    # Парсинг данных с Авито
    parse_avito_apartments(driver, By)

    # Закрытие веб-драйвера
    driver.quit()


if __name__ == "__main__":
    main()
