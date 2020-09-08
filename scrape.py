#selenium packages
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#pandas to convert to csv
import pandas as pd

import time #to give time to the webdriver to click

try:
    start_time=time.time()
    web = webdriver.Chrome(executable_path=r"yourpath\chromedriver.exe")
    web.get('https://www.linkedin.com')

    web.find_element_by_id("session_key").send_keys("your email")
    web.find_element_by_id("session_password").send_keys("password")

    web.find_element(By.CSS_SELECTOR, "body > main > section.section.section--prominent > div.sign-in-form-container > form > button").click()
    #to allow time to sign in
    element = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div/nav/ul/li[7]")))
    
    web.get('post-link')
    loadXPath='/html/body/div[7]/div[3]/div/div/div/div/div/section/div/div[6]/div/div[3]/div[3]/div/button/span'
    
    counter=0
    '''
    web.find_element_by_xpath(loadXPath).click()
    time.sleep(0.5)
    web.find_element_by_xpath(loadXPath).click()
    time.sleep(0.5)
    web.find_element_by_xpath(loadXPath).click()#takes too long for it too run 4000 comments
    time.sleep(0.5)
    '''
    #scraping number of comments
    time.sleep(0.25)
    

    try:
        while True:
            time.sleep(0.5)#play around with this, you may need more time depending on internet speed
            try:
                while True:
                    web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div/section/div/div[4]/div/div[3]/div[3]/article[1]/div[6]/div/div[4]/div/button').click()

            except:
                print('No load more replies button')
                
            web.find_element_by_class_name('comments-comments-list__load-more-comments-button').click()
            print('Load Click!')
            counter+=1
            print('Counter =', counter)
    except selenium.common.exceptions.NoSuchElementException:
        print('Got all comments!')

    
    links=web.find_elements_by_class_name('feed-link')
    print(len(links))
    emails=[]
    
    for i in links:
        if '@' in i.text:
            emails.append(i.text)
        
    print(emails)
    print(len(emails))
    d = {'emails':emails}
    df = pd.DataFrame(data=d)
    df.to_csv(r'yourpath\li-web.csv', index=True)
    
    
except Exception as e:
    print(e)

finally:
    web.close()
    print("--- %s seconds ---" % (time.time() - start_time))
