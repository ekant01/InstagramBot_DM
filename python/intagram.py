from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
# import random


def InstagramBot(username, password, person, message):

    # driver = webdriver.Chrome()
    # driver = ChromeDriver(); 
    driver = webdriver.Chrome('./chromedriver')

    driver.get("https://www.instagram.com/")

    enter_username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
    enter_username.send_keys(username)

    enter_password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)

    enter_password.send_keys(Keys.RETURN)
    time.sleep(7)

    try:
        not_now = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, '_acao')))
        # a = not_now.find_elements_by_tag_name("button")
        actions = ActionChains(driver)
        actions.click(not_now)
        actions.perform()
    except:
        pass
    
    # finally:
    #     inbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'xWeGp')))
    #     actions = ActionChains(driver)
    #     actions.click(inbox)
    #     actions.perform()
    #     time.sleep(random.randint(1, 4))
    
    try:
        not_now = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, '_a9_1')))
        #a = not_now.find_elements_by_tag_name("button")[1]
        actions = ActionChains(driver)
        actions.click(not_now)
        actions.perform()

    except:
        pass

    finally:
        inbox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"direct/inbox/")]')))
        actions = ActionChains(driver)
        actions.click(inbox)
        actions.perform()
        time.sleep(10)

    
    new_message = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="New message"]')))
    actions = ActionChains(driver)
    actions.click(new_message)
    actions.perform()
    time.sleep(8)

    enter_person_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, 'queryBox')))
    enter_person_name.send_keys(person)
    time.sleep(5)

    select_person = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]')))
    actions = ActionChains(driver)
    actions.click(select_person)
    actions.perform()
    #driver.find_element_by_xpath('//*[@id="f20eb93e50b030c"]/button').click()
    
    time.sleep(3)

    next_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, '_aagz')))
    actions1 = ActionChains(driver)
    actions1.click(next_button)
    actions1.perform()
    time.sleep(25)
    


    messagebox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
    messagebox.send_keys(message)
    time.sleep(2)

    messagebox.send_keys(Keys.RETURN)
    time.sleep(10)

InstagramBot("username", "password", "person", "Hii.... This message send by instagram bot automatically" )