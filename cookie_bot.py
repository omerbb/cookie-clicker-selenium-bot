from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
a = 0
browser.get("https://orteil.dashnet.org/cookieclicker/")
lista=[]
sleep(10)
cookie =browser.find_element_by_xpath('//*[@id="bigCookie"]')

while True:
    cookie.click()
    cookie.click()
    suc=False
    a+=1


    try:
        cursor = int(browser.find_element_by_id("productPrice0").text)
        cursor = 0.1 / cursor

        lista.append(cursor)
        suc=True
        if suc == True:
            suc=False
            try:
                grandma = int(browser.find_element_by_id("productPrice1").text)
                grandma = 1 / grandma
                lista.append(grandma)
                suc = True
                if suc ==True:
                    suc=False
                    try:
                        farm = int(browser.find_element_by_id("productPrice2").text)
                        farm = 8 / farm
                        lista.append(farm)
                        suc=True
                        if suc == True:
                            suc=False
                            try:
                                mine = int(browser.find_element_by_id("productPrice3").text)
                                mine =47/mine
                                lista.append(mine)
                                suc=True
                                if suc ==True:
                                    suc=False
                                    try:
                                        factory = int(browser.find_element_by_id("productPrice4").text)
                                        factory =260/factory
                                        lista.append(factory)
                                        suc=True
                                        if suc==True:
                                            suc=False
                                            try:
                                                bank = int(browser.find_element_by_id("productPrice5").text)
                                                bank =1400/bank
                                                lista.append(bank)
                                                suc=True
                                                if suc==True:
                                                    suc=False
                                                    try:
                                                        temple=int(browser.find_element_by_id("productPrice6").text)
                                                        temple = 7800/temple
                                                        lista.append(temple)
                                                        suc=True
                                                        if suc == True:
                                                            suc=False
                                                            try:
                                                                wizard = int(browser.find_element_by_id("productPrice7").text)
                                                                wizard = 44000/wizard
                                                                lista.append(wizard)
                                                                suc=True
                                                                if suc==True:
                                                                    try:
                                                                        shipment = int(browser.find_element_by_id("productPrice8").text)
                                                                        shipment = 260000/shipment
                                                                        lista.append(shipment)

                                                                    except:
                                                                        pass
                                                            except:
                                                                pass
                                                    except:
                                                        pass
                                            except:
                                                pass
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
            except:
                pass
    except:
        pass
    cookie.click()
    a+=1
    if a ==50:
        a = 0
        if len(lista) != 0:
            maks = max(lista)
        lista =[]
        try:
            if maks == cursor:
                link = browser.find_element_by_id("product0")
                link.click()
                del link
        except:
            pass
        try:
            if maks == grandma:
                link = browser.find_element_by_id("product1")
                link.click()
                del link
        except:
            pass
        try:
            if maks == farm:
                link = browser.find_element_by_id("product2")
                link.click()
                del link
        except:
            pass
        try:
            if maks == mine:
                link = browser.find_element_by_id("product3")
                link.click()
                del link
        except:
            pass
        try:
            if maks == factory:
                link = browser.find_element_by_id("product4")
                link.click()
                del link
        except:
            pass
        try:
            if maks == bank:
                link = browser.find_element_by_id("product5")
                link.click()
                del link
        except:
            pass
        try:
            if maks == temple:
                link = browser.find_element_by_id("product6")
                link.click()
                del link
        except:
            pass
        try:
            if maks == wizard:
                link = browser.find_element_by_id("product7")
                link.click()
                del link
        except:
            pass
        try:
            if maks == shipment:
                link = browser.find_element_by_id("product8")
                link.click()
                del link
        except:
            pass






