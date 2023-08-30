import yaml
from module import Site
import time

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata['address'])


# def test_step1():  # негативный тест с передачей неправильнного логина и пароля
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""   # поле логина задаем селектор по xpath
#     input1 = site.find_element('xpath', x_selector1)  #поиск элемента
#     input1.clear()
#     input1.send_keys('test')         # отправляем неправильный логин
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""   # поле пароля
#     input2 = site.find_element('xpath', x_selector2)
#     input2.clear()
#     input2.send_keys('test')
#     btn_selector = 'button'   #задаем селектор по css селектору
#     btn = site.find_element('css', btn_selector)               # находим элемент по селектору
#     btn.click()  # клик по кнопке
#     x_selector3 = '//*[@id="app"]/main/div/div/div[2]/h2'  # селектор элемента с ошибкой 401 (chrome!)
#     err_label = site.find_element('xpath', x_selector3)
#     assert err_label.text == '401'  # получили текст ошибки
#
# def test_step2():  # авторизация с правильным логином и паролем
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""  # поле логина задаем селектор по xpath
#     input1 = site.find_element('xpath', x_selector1)  # поиск элемента
#     input1.clear()
#     input1.send_keys(testdata['login'])  # отправляем  логин
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""  # поле пароля
#     input2 = site.find_element('xpath', x_selector2)
#     input2.clear()
#     input2.send_keys(testdata['passwd'])
#     btn_selector = 'button'  # задаем селектор по css селектору
#     btn = site.find_element('css', btn_selector)  # находим элемент по селектору
#     btn.click()  # клик по кнопке
#     x_selector3 = '// *[ @ id = "app"] / main / nav / ul / li[3] / a'  # селектор элемента
#     hello_label = site.find_element('xpath', x_selector3)
#     assert hello_label.text == f'Hello, {testdata["login"]}'

def test_step3():   #проверка создания поста
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""  # поле логина задаем селектор по xpath
    input1 = site.find_element('xpath', x_selector1)  # поиск элемента
    input1.clear()
    input1.send_keys(testdata['login'])  # отправляем  логин
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""  # поле пароля
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(testdata['passwd'])
    btn_selector = 'button'  # задаем селектор по css селектору
    btn = site.find_element('css', btn_selector)  # находим элемент по селектору
    btn.click()  # клик по кнопке
    add_btn_selector = """//*[@id="create-btn"]"""
    add_btn = site.find_element('xpath', add_btn_selector)
    add_btn.click()
    x_selector3 = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
    input3 = site.find_element('xpath', x_selector3)
    input3.send_keys(testdata['title'])
    save_btn_selector = """// *[ @ id = "create-item"] / div / div / div[7] / div / button / span"""
    save_btn = site.find_element('xpath', save_btn_selector)
    save_btn.click()
    time.sleep(testdata['sleep_time'])
    x_selector4 = """//*[@id="app"]/main/div/div[1]/h1"""
    title_label2 = site.find_element('xpath', x_selector4)
    text = title_label2.text
    assert text == f'{testdata["title"]}'






# css_selector = 'span.mdc-text-field__ripple'   # скопировали селектор элемента из инструмента разработчика браузера
# print(site.get_element_property('css', css_selector, 'height'))  # получили высоту элемента
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property('xpath', xpath, 'color'))  #получили цвет элемента по xpath
#
# if __name__ == '__main__':
#     pass
