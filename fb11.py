from selenium import webdriver
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.facebook.com/')

fb_name = input("Your Facebook Email (or phone)")
fb_pass = input("Your Facebook pass")

browser.find_element_by_name('email').send_keys(fb_name)
browser.find_element_by_name('pass').send_keys(fb_pass)
browser.find_element_by_id('loginbutton').click()

fr_id = input("Your Friend's Facebook ID")
driver.find_element_by_link_text("Add Friend").click()

status = input("Enter your status")
browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div').click()
browser.find_element_by_class_name("_1mf _1mj").send_keys(status)
browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div').click()

comment = input("Enter your Comment")
browser.find_element_by_id("compserInput").send_keys(comment)
browser.find_elements_by_tag_name("button").click()
