# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://practice.automationtesting.in/")
# driver.execute_script("window.scrollBy(0, 600);")
# ruby_btn = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/selenium-ruby/']")
# ruby_btn.click()
# reviews_btn = driver.find_element_by_css_selector(".reviews_tab")
# reviews_btn.click()
# star_click = driver.find_element_by_css_selector(".star-5")
# star_click.click()
# com_text = driver.find_element_by_css_selector("#comment")
# com_text.send_keys("Nice book!")
# name_field = driver.find_element_by_css_selector("#author")
# name_field.send_keys("Васисуалий")
# email_send = driver.find_element_by_css_selector("#email")
# email_send.send_keys("mail@mail.ru")
# submit_btn = driver.find_element_by_css_selector("#submit.submit")
# time.sleep(2)
# submit_btn.click()
# driver.quit()