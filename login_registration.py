
# #---Registration ------done--------
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.get("https://practice.automationtesting.in/")
# account_btn =driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# account_btn.click()
# email_reg = driver.find_element_by_css_selector("#reg_email")
# email_reg.send_keys("mail1@mail.ru")
# pass_reg = driver.find_element_by_css_selector("#reg_password")
# pass_reg.click()
# time.sleep(1)
# pass_reg.send_keys("1Passwordpassword!!")
# submit_btn = driver.find_element_by_css_selector("[value='Register']")
# submit_btn.click()
# time.sleep(1)
# driver.quit()

# #---LOgin -------done-----------------
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver.get("https://practice.automationtesting.in/")
# account_btn =driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# account_btn.click()
# user_name = driver.find_element_by_id("username")
# user_name.send_keys("mail1@mail.ru")
# pass_in = driver.find_element_by_id("password")
# pass_in.send_keys("1Passwordpassword!!")
# login_btn = driver.find_element_by_css_selector("[value='Login'].woocommerce-Button")
# login_btn.click()
# logout_exist = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-36 li:nth-child(6) >a"), "Logout"))
# driver.quit()