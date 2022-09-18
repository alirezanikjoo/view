import os
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.common.by import By
import time

flag=0
while flag!=10:
    path=r"C:\Users\Administrator\Downloads\http-proxy[DigiProxy.net].txt"

    if os.path.exists(path):
        os.remove(path)
    else:
        print("file does not exist")

    driver=webdriver.Chrome("chromedriver.exe")
    driver.get("https://digiproxy.net/")
    link=driver.find_element(By.XPATH,'//*[@id="main"]/div/div/section[2]/div/div[1]/div/div/div/div[1]/div[3]/a')
    link.click()
    time.sleep(3)
    driver.quit()

    proxy_ip_port=[]

    with open(r"C:\Users\Administrator\Downloads\http-proxy[DigiProxy.net].txt") as f:
        reader=f.read().split("\n")
    print(len(reader))
    for i in range(len(reader)):

        proxy=Proxy()
        proxy.proxy_type=ProxyType.MANUAL
        proxy.http_proxy=reader[i]
        proxy.ssl_proxy=reader[i]
        capabilities=webdriver.DesiredCapabilities.CHROME
        proxy.add_to_capabilities(capabilities)


        driver=webdriver.Chrome("chromedriver.exe",desired_capabilities=capabilities)
        try:
            driver.set_page_load_timeout(20)
            driver.get("https://sarzaminhooshmand.com")
            link=driver.find_element(By.TAG_NAME,"body")
            time.sleep(2)
            er=link.text
            
            if "This page isn’t working" in er:
                driver.quit()
                continue
            elif "This site can’t be reached" in er:
                driver.quit()
                continue

            height=int(driver.execute_script("return document.documentElement.scrollHeight"))//20
            height1=height
            for i in range(20):   
                driver.execute_script("window.scrollTo(0,%i)" %(height1-40))
                time.sleep(0.5)
                height1+=height
            time.sleep(3)
        except:
            print('error')

        driver.quit()
    flag+=1
    print("Done!!")