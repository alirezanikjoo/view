import os
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy , ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

path=r"..\..\Users\Alireza\Downloads\http-proxy[DigiProxy.net].txt"

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

# with open(r"..\..\Users\Alireza\Downloads\socks5-proxy[DigiProxy.net].txt") as f:
with open(r"..\..\Users\Alireza\Downloads\http-proxy[DigiProxy.net].txt") as f:
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
        driver.get("https://sarzaminhooshmand.com")
        link=driver.find_element(By.TAG_NAME,"body")
        time.sleep(2)
        er=link.text
        
        if "This page isn’t working" in er:
            pass
        elif "This site can’t be reached" in er:
            pass

        height=int(driver.execute_script("return document.documentElement.scrollHeight"))//15
        height1=height
        for i in range(15):   
            driver.execute_script("window.scrollTo(0,%i)" %(height1))
            time.sleep(0.35)
            height1+=height

    except:
        print('error')
    driver.quit()

print("Done!!")

# driver.execute_async_script(
        #     """
        #         count = 400;
        #         let callback = arguments[arguments.length - 1];
        #         t = setTimeout(function scrolldown(){
        #             console.log(count, t);
        #             window.scrollTo(0, count);
        #             if(count < (document.body.scrollHeight || document.documentElement.scrollHeight)){
        #             count+= 400;
        #             t = setTimeout(scrolldown, 1000);
        #             }else{
        #             callback((document.body.scrollHeight || document.documentElement.scrollHeight));
        #             }
        #         }, 1000);
        #     """
        # )

    # 00
    # 11