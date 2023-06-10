# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep
driver = webdriver.Chrome()
site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru'
site_title = 'Вход в личный кабинет'
action_chains = ActionChains(driver)
try:
    driver.get(site)
    sleep(1)
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
    contacts = driver.find_element(By.CSS_SELECTOR, '.informers-InformersBar-informer-header_container'
                                                    '[title="Новое сообщение"]')
    contacts.click()
    sleep(1)
    receiver = 'Кассирыч Кар Иванов'
    search = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content .controls-Field')
    search.send_keys(receiver, Keys.ENTER)
    search.send_keys(Keys.ENTER)
    message_text = 'Тестовое сообщение'
    message = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message.send_keys(message_text)
    send = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__content-area [title="Отправить"]')
    send.click()
    received_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="counter_new"]')
    received_message.click()
    receiver_name = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item__addressee_limited[title="Кассирыч Кар"]')
    receiver_text = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    assert receiver_name.text == 'Кассирыч Кар', receiver_text.text == message_text
    unread_message = driver.find_element(By.CSS_SELECTOR, '.layout-Browser__content .controls-BaseControl')
    action_chains.context_click(unread_message)
    action_chains.perform()
    message_del = driver.find_elements(By.CSS_SELECTOR, '.controls-Menu__content-wrapper_width')[5]
    message_del.click()
    empty = driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message')
    assert empty.text == 'Не найдено ни одного сообщения', 'Элемент не отображается'
    print('Все тесты прошли')

finally:
    driver.quit()
