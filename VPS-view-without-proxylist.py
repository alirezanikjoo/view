import os
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.common.by import By
import time

flag=0
while flag!=10:

    proxy_ip_port=[]

    with open(r"C:\Users\Administrator\Downloads\http-proxy[DigiProxy.net].txt") as f:
        reader=f.read().split("\n")
    numberofproxies=len(reader)
    print(numberofproxies)
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
            driver.get("https://tarahisiteseo.com")
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
            for j in range(20):   
                driver.execute_script("window.scrollTo(0,%i)" %(height1-30))
                time.sleep(0.5)
                height1+=height
            time.sleep(3)
            print("%ist proxy from %i proxies" %(i,numberofproxies))
        except:
            print('error')

        driver.quit()
    flag+=1
    print("Done!!")