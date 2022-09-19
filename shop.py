# Shop: отображение страницы товара--------done------------

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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# html_book = driver.find_element_by_css_selector("#content li:nth-child(3) img")
# html_book.click()
# book_name_check = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".entry-summary h1"), "HTML5 Forms"))
# driver.quit()

#  #  Shop: количество товаров в категории-----done---

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# account_btn =driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# account_btn.click()
# user_name = driver.find_element_by_id("username")
# user_name.send_keys("mail1@mail.ru")
# pass_in = driver.find_element_by_id("password")
# pass_in.send_keys("1Passwordpassword!!")
# login_btn = driver.find_element_by_css_selector("[value='Login'].woocommerce-Button")
# login_btn.click()
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# html_folder = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product-category/html/']")
# html_folder.click()
# # items_cat = WebDriverWait(driver, 5).until(
# #     EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cat-item-19 span"), "(3)"))
# items_cat = driver.find_element_by_css_selector(".cat-item-19 span")
# items_cat_text = items_cat.text
# if len(items_cat_text) == 3:
#     print("В каталоге 3 товара")
# else:
#     print("Ошибка. Товаров в каталоге: " + str(len(items_cat_text)))
# driver.quit()

# #---Shop: сортировка товаров---------------done ---------

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# from selenium.webdriver.support.select import Select
# driver.get("https://practice.automationtesting.in/")
# account_btn =driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# account_btn.click()
# user_name = driver.find_element_by_id("username")
# user_name.send_keys("mail1@mail.ru")
# pass_in = driver.find_element_by_id("password")
# pass_in.send_keys("1Passwordpassword!!")
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# sort_sel_btn = driver.find_element_by_css_selector("[value='menu_order']")
# sort_sel_btn_check = sort_sel_btn.get_attribute("selected")
# selector_btn = driver.find_element_by_css_selector(".orderby")
# select = Select(selector_btn)
# select.select_by_visible_text("Sort by price: high to low")
# sort_sel_btn = driver.find_element_by_css_selector("[value='price-desc']")
# sort_sel_btn_check2 = sort_sel_btn.get_attribute("selected")
# print(sort_sel_btn_check2)
# driver.quit()


# Shop: отображение, скидка товара -------done ------
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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# andr_book = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']")
# andr_book.click()
# old_price = driver.find_element_by_css_selector(".price >del >span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price >ins >span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# close_click = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# close_click.click()
# driver.quit()



# #----Shop: проверка цены в корзине ---done-------
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# account_btn =driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/my-account/']")
# account_btn.click()
# user_name = driver.find_element_by_id("username")
# user_name.send_keys("mail1@mail.ru")
# pass_in = driver.find_element_by_id("password")
# pass_in.send_keys("1Passwordpassword!!")
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# add_bascket = driver.find_element_by_css_selector("[data-product_id='182']")
# add_bascket.click()
# time.sleep(2)
# check_num = driver.find_element_by_css_selector(".cartcontents")
# check_num_text = check_num.text
# print(check_num_text)
# assert check_num_text == "1 Item"
# check_price = driver.find_element_by_css_selector(".amount")
# check_price_text = check_price.text
# print(check_price_text)
# assert check_price_text == "₹180.00"
# driver.quit()


# #-----Shop: работа в корзине------done----
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 300);")
# add_bascket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
# add_bascket.click()
# time.sleep(2)
# add_bascket_2 = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']")
# add_bascket_2.click()
# time.sleep(2)
# bascket_btn = driver.find_element_by_css_selector(".added_to_cart.wc-forward")
# bascket_btn.click()
# time.sleep(2)
# remove_1 = driver.find_element_by_css_selector("[data-product_id='182']")
# remove_1.click()
# undo_remove = driver.find_element_by_css_selector(".woocommerce-message a")
# undo_remove.click()
# change_num = driver.find_element_by_css_selector("tbody tr:nth-child(1) >td:nth-child(5) .text")
# change_num.clear()
# change_num.send_keys("3")
# update_cart = driver.find_element_by_css_selector(".actions [name='update_cart']")
# update_cart.click()
# value_num = change_num.get_attribute("value")
# assert value_num == "3"
# time.sleep(2)
# apply_btn = driver.find_element_by_css_selector(".actions [name='apply_coupon']")
# apply_btn.click()
# update_text = driver.find_element_by_css_selector(".woocommerce-error li")
# update_text_check = update_text.text
# assert update_text_check == "Please enter a coupon code."
# driver.quit()



# #---------Shop: покупка товара -----done ----

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
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 a")
# shop_btn.click()
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 300);")
# add_bascket = driver.find_element_by_css_selector("[data-product_id='182']")
# add_bascket.click()
# time.sleep(3)
# bascket_btn = driver.find_element_by_css_selector(".added_to_cart.wc-forward")
# bascket_btn.click()
# checkout_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
# checkout_btn.click()
# checkout_name = WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#billing_first_name")))
# checkout_name.send_keys("Vasya")
# checkout_name_last = driver.find_element_by_id("billing_last_name")
# checkout_name_last.send_keys("Ivanov")
# checkout_mail = driver.find_element_by_id("billing_email")
# checkout_mail.send_keys("mail1@mail.ru")
# checkout_phone = driver.find_element_by_id("billing_phone")
# checkout_phone.send_keys("1234567890")
# country_sel = driver.find_element_by_id("s2id_billing_country")
# country_sel.click()
# country_sel_search = driver.find_element_by_id("s2id_autogen1_search")
# country_sel_search.send_keys("russ")
# country_sel_search_russ = driver.find_element_by_css_selector(".select2-match")
# country_sel_search_russ.click()
# checkout_adress = driver.find_element_by_id("billing_address_1")
# checkout_adress.send_keys("Kima,1")
# checkout_sity = driver.find_element_by_id("billing_city")
# checkout_sity.send_keys("SPB")
# checkout_state = driver.find_element_by_id("billing_state")
# checkout_state.send_keys("rus")
# checkout_zip = driver.find_element_by_id("billing_postcode")
# checkout_zip.send_keys("123456")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# check_metod = driver.find_element_by_css_selector("#payment_method_cheque.input-radio")
# check_metod.click()
# place_order = driver.find_element_by_id("place_order")
# place_order.click()
# text_received = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received" ), "Thank you. Your order has been received."))
# print(text_received)
# text_payment = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))
# print(text_payment)
# driver.quit()
