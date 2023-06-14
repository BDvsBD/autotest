# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
import os

driver = webdriver.Chrome()
site = 'https://sbis.ru/'
site_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
action_chains = ActionChains(driver)
try:
    driver.get(site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == site, 'Неверный адрес сайта'
    assert driver.title == site_title, 'Неверный заголовок сайта'
    footer = driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer')
    footer.location_once_scrolled_into_view
    download_link = driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer__link[href="/download?tab=ereport&innerTab=ereport25"]')
    download_link.click()
    sbis_plaguin = driver.find_elements(By.CSS_SELECTOR, '.controls-TabButton__right-align.controls-ListView__item ')[1]
    print(sbis_plaguin.text)
    sbis_plaguin.click()
    download_link = driver.find_element(By.CSS_SELECTOR, '[href = "https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"] ')
    download_link.click()

    download_folder = os.path.dirname(os.path.abspath(__file__))
    sleep(5)

    # находим скачанный файл и выводим его размер в мегабайтах
    for file in os.listdir(download_folder):
        if file.endswith('.exe'):
            file_size = os.path.getsize(os.path.join(download_folder, file))
            print(f'Размер файла {file} составляет {round(file_size / 1048576, 2)} МБ')


finally:
    driver.quit()

