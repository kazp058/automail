from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

url = 'https://www.facebook.com/post_ejemplo/posts/1896238197175327'

me = ["correo ","contraseña"]

#send_box = driver.find_element_by_class_name(' _3d2q _65tb  _4w79')
#_5rp7
i = 1

print("Ready for show?")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

with open('texto.txt', 'r') as f:
    for parrafo in f.readlines():
        palabras = parrafo.split(' ')
        for palabra in palabras:

            try:

                driver = webdriver.Chrome("C:\\Users\\KEVIN Z\\Downloads\\chromedriver.exe")
                driver.get(url)

                time.sleep(4)
                driver.find_element_by_id('email').send_keys(me[0])
                driver.find_element_by_id('pass').send_keys(me[1])
                driver.find_element_by_id('u_0_2').click()

                time.sleep(4)
                section = driver.find_element_by_xpath(r"//form[@class=' _129h']")

                comment_box = section.find_element_by_class_name("_65td")
                comment_box.send_keys(palabra,Keys.ENTER)

                section = None
                comment_box = None
                #comment_box.click()
                #_7c_q
                print("Comment " + str(i) + " sended to EDNN07: " + palabra)

                time.sleep(4)

                driver.close()
                time.sleep(4)
            except Exception:
                print("Error!, reintentando")
                if driver:
                    driver.close()
