# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru'
site_title = 'Вход в личный кабинет'
action_chains = ActionChains(driver)
try:
    driver.get(site)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == site, 'Неверный адрес сайта'
    assert driver.title == site_title, 'Неверный заголовок сайта'
    user_login, user_password = 'retailmobile', 'Test123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.clear()
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    print('Навести курсор на сообщения')
    contacts = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="informers_informerContent_Messages_icon"]')))
    contacts.click()
    receiver = 'Кассирыч Кар Иванов'
    search = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.controls-StackTemplate-content .controls-Field')))
    search.send_keys(receiver, Keys.ENTER)
    addressee = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-addressee-selector_plain-list [title="Кассирыч Кар"]')))
    addressee.click()
    message_text = 'Тестовое сообщение'
    message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')))
    message.send_keys(message_text)
    send = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.controls-Button_clickable[data-qa="msg-send-editor__send-button"]')))
    send.click()
    received_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-qa="counter_new"]')))
    received_message.click()
    receiver_name = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.msg-dialogs-item__addressee_limited[title="Кассирыч Кар"]')))
    assert receiver_name.text == 'Кассирыч Кар'
    unread_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.layout-Browser__content .controls-BaseControl')))
    action_chains.context_click(unread_message)
    action_chains.perform()
    message_del = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.controls-Menu__content-wrapper_width')))[5]
    message_del.click()
    empty = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.hint-Template__text_message')))
    assert empty.text == 'Не найдено ни одного сообщения', 'Элемент не отображается'
    print('Все тесты прошли')

finally:
    driver.quit()
