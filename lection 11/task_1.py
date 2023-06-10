# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Keys, ActionChains
driver = webdriver.Chrome()
site = 'https://sbis.ru/'
site_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
try:
    driver.get(site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == site, 'Неверный адрес сайта'
    assert driver.title == site_title, 'Неверный заголовок сайта'
    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Количество элементов отличается'
    print('Проверить текст, атрибут и видимость ссылки Контакты')
    link_txt = 'Контакты'
    start_link = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
    assert start_link.text == link_txt
    print('Перейти на страницу Конаткты')
    assert start_link.is_displayed(), 'Элемент не отображается'
    start_link.click()
    sleep(1)
    contacts_url = 'https://sbis.ru/contacts/76-yaroslavskaya-oblast?tab=clients'
    contacts_title = 'СБИС Контакты — Ярославская область'
    assert driver.current_url == contacts_url, 'Неверный адрес сайта'
    assert driver.title == contacts_title, 'Неверный заголовок сайта'
    tensor_link = driver.find_element(By.CSS_SELECTOR, '[id=\'contacts_clients\'] '
                                                       '[class="sbisru-Contacts__logo-tensor mb-8"]')
    print('Перейти на страницу Тензор')
    assert tensor_link.is_displayed(), 'Элемент не отображается'
    tensor_link.click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("localStorage.setItem('s3ca', '.')")
    driver.refresh()
    block_header_txt = 'Сила в людях'
    block_header = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert block_header.text[:12] == block_header_txt
    about_link = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content [href="/about"]')
    print('Перейти на страницу Подробнее')
    assert about_link.is_displayed(), 'Элемент не отображается'
    about_link.click()
    about_url = 'https://tensor.ru/about'
    about_title = 'О компании | Тензор — IT-компания'
    assert driver.current_url == about_url, 'Неверный адрес сайта'
    assert driver.title == about_title, 'Неверный заголовок сайта'
    print('Все тесты прошли')

finally:
    driver.quit()

