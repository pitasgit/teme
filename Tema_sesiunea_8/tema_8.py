from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

## Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● Id

# driver.get ("https://phptravels.net/")
#
# hotels_tab = driver.find_element(By.ID, 'hotels-tab')
# language_tab = driver.find_element(By.ID, 'languages')
# account_tab = driver.find_element(By.ID, 'ACCOUNT')
# account_tab.click()

# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● link text
# driver.get ("https://the-internet.herokuapp.com/")
# broken_img=driver.find_element(By.LINK_TEXT, "Broken Images")
# link_text=driver.find_element(By.LINK_TEXT, "Geolocation")
# file_download=driver.find_element(By.LINK_TEXT, "File Download")
# link_text.click()
# driver.get ("https://the-internet.herokuapp.com/download")
# desert_txt=driver.find_element(By.LINK_TEXT, "Demo.txt")
#
# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● partial link text
#
# driver.get("https://www.wikipedia.org/")
# partial_eng = driver.find_element(By.PARTIAL_LINK_TEXT, "English")
# partial_eng.click()
# driver.get("https://www.wikipedia.org/")
# donate=driver.find_element(By.PARTIAL_LINK_TEXT, "donation.")
# donate.click()
# driver.get("https://www.emag.ro/")
# colet=driver.find_element(By.PARTIAL_LINK_TEXT, "coletului")
# colet.click()

# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: Name
#
# driver.get("https://www.netflix.com/ro-en/")
# name_email = driver.find_element(By.NAME, "email")
# name_email.send_keys('petre@itfactory.ro')
#
#
#
#
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# muzica_buna = driver.find_element(By.NAME, "search")
# muzica_buna.send_keys('peace in world')
# driver.get("https://www.imdb.com/?ref_=nv_home")
# oras = driver.find_element(By.NAME, "q")
# oras.send_keys('best movie ever')
# driver.get("https://www.anre.ro/ro/")
# anre = driver.find_element(By.NAME, "s")
#
# driver.get ("https://the-internet.herokuapp.com/")
# body_tn=driver.find_elements(By.TAG_NAME, "body")
# print(body_tn)
# driver.get ("https://phptravels.net/")
# button_tn=driver.find_elements(By.TAG_NAME, "button")
# print(button_tn)
# driver.get ("https://phptravels.net/")
# div_tn=driver.find_elements(By.TAG_NAME, "div")
# print(div_tn)
#
#
# ##Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● Class name
# driver.get ("https://phptravels.net/")
# class_1=driver.find_element(By.CLASS_NAME, "hero-wrappe")
# print(class_1)
#
# driver.get ("https://www.guerrillaradio.ro/player/")
# class_guerrilla=driver.find_element(By.CLASS_NAME, "container")
# print(class_guerrilla)
# driver.get ("https://the-internet.herokuapp.com/")
# class_row = driver.find_elements(By.CLASS_NAME, "row")
# print(class_row)
#
# #Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# #Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
# driver.get ("https://www.seleniumframework.com/Practiceform/")
# site_sf_cssID = driver.find_element(By.CSS_SELECTOR, 'button[id = "colorVar"]')
# site_sf_cssID.click()
#
# driver.get ("https://www.jetbrains.com/")
# class_cssID = driver.find_element(By.CSS_SELECTOR, '[class="rs-link rs-link_mode_classic rs-link_theme_dark product-card__title"]')
# class_cssID.click()
# sleep(2)
#
# driver.get ("https://account.jetbrains.com/login")
# site_tech_cssID = driver.find_element(By.CSS_SELECTOR, 'div input[name="username"]')
# site_tech_cssID.send_keys('Petre')
# sleep(2)

## Pentru xpath identifică elemente după criteriile de mai jos: ● 3 după atribut valoare

# driver.get("https://www.booking.com/")
# atrval_xpath0=driver.find_element(By.XPATH, '//input[@id="ss"]')
# driver.get("https://www.automatetheplanet.com/applications/most-exhaustive-xpath-locators-cheat-sheet/")
# atrval_xpath2=driver.find_element(By.XPATH, '//input[@data-field="name"]')
# atrval_xpath2.send_keys("numele meu")
# driver.get("https://www.google.com/")
# atrval_xpath3=driver.find_element(By.XPATH, '//input[@name="q"]')

# Pentru xpath identifică elemente după criteriile de mai jos: ● 3 după textul de pe element
# driver.get("https://phptravels.net/")
# text_xpath0= driver.find_element(By.XPATH, '//p[contains(text(), "Choose best deals")]')

# driver.get("https://www.booking.com")
# text_xpath1= driver.find_element(By.XPATH, '//span[contains(text(), "Find your next stay")]')
#
# driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# text_xpath2= driver.find_element(By.XPATH, '//span[contains(text(), "AUTOMATION PRACTICE ME")]')
#
#
# # Pentru xpath identifică elemente după criteriile de mai jos: ● 1 după parțial text
#
# driver.get("https://www.wikipedia.org/")
# partialtext_xpath1= driver.find_element(By.XPATH, '//div[contains(text(), "Wikimedia")]')

# Pentru xpath identifică elemente după criteriile de mai jos: 1 cu SAU, folosind pipe |

# driver.get("https://phptravels.net/login")
# pipe= driver.find_element(By.XPATH, '//input[@type="password"] | //input[@name="password"]')

# Pentru xpath identifică elemente după criteriile de mai jos:  ● 1 cu *
# driver.get("https://www.wikipedia.org/")
# star= driver.find_element(By.XPATH, '//*[@id="searchInput"]')
# star.send_keys("Romania")
# sleep(2)
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]
# driver.get("https://phptravels.net/")
# listxpath= driver.find_element(By.XPATH, '//a[@class="dropdown-item waves-effect"][1]')

## ● 1 în care să folosești parent::
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# parentxpath= driver.find_element(By.XPATH, '//*[@class="vector-menu-content"]//parent::div')

# ● 1 în care să folosești fratele anterior sau de după (la alegere)

# driver.get("https://en.wikipedia.org/wiki/Wikipedia:Contents")
# sibling_xpath= driver.find_element(By.XPATH, '//*[@id="mw-head"]//following-sibling::div')
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.

driver.get("https://phptravels.net/login")
def functie(placeholder_text, input_value):
    input= driver.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)

functie('Email', 'petre@itfactory.ro')
sleep(3)

