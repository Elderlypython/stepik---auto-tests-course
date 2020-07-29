from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    button_1 = browser.find_element_by_css_selector('.trollface.btn.btn-primary')
    button_1.click()


    browser.switch_to.window(browser.window_handles[1])

    variab = browser.find_element_by_css_selector('#input_value')
    x = variab.text

    inp_text = calc(x)

    input_1 = browser.find_element_by_css_selector('#answer')
    input_1.send_keys(inp_text)

    but_submit = browser.find_element_by_css_selector('.btn.btn-primary')
    but_submit.click()


    # тут обращение к алерту,получение проверочного кода из него
    alert2 = browser.switch_to.alert
    alert_text = alert2.text
    alert_text = alert_text.split(': ')[-1]
    print(alert_text)


finally:
    time.sleep(7)
    browser.quit()