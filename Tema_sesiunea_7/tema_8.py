from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● Id

# driver.get ("https://phptravels.net/")
#
# hotels_tab = driver.find_element(By.ID, 'hotels-tab')
# language_tab = driver.find_element(By.ID, 'languages')
# account_tab = driver.find_element(By.ID, 'ACCOUNT')
# account_tab.click()
#
# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● link text
# driver.get ("https://the-internet.herokuapp.com/")
# broken_img=driver.find_element(By.LINK_TEXT, "Broken Images")
# link_text=driver.find_element(By.LINK_TEXT, "Geolocation")
# file_download=driver.find_element(By.LINK_TEXT, "File Download")
# link_text.click()
# driver.get ("https://the-internet.herokuapp.com/download")
# desert_txt=driver.find_element(By.LINK_TEXT, "Desert.jpg")
#
# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: ● partial link text
#
# driver.get("https://www.wikipedia.org/")
# partial_eng = driver.find_element(By.PARTIAL_LINK_TEXT, "English")
# partial_eng.click()
# driver.get("https://www.wikipedia.org/")
# donate=driver.find_element(By.PARTIAL_LINK_TEXT, "You can support our work with a donation.")
# donate.click()
# driver.get("https://www.emag.ro/")
# colet=driver.find_element(By.PARTIAL_LINK_TEXT, "Deschiderea coletului la livrare")
# colet.click()
#
# # Alege câte 3 elemente din fiecare tip de selector din următoarele categorii: Name

# driver.get("https://www.netflix.com/ro-en/")
# name_email = driver.find_element(By.NAME, "email")
# name_email.send_keys('petre@itfactory.ro')




driver.get("https://www.youtube.com")
driver.implicitly_wait(10)
driver.find_element('https://www.youtube.com/*[@id="uc-btn-accept-banner"]').click()
muzica_buna = driver.find_element(By.NAME, "search_query")
muzica_buna.send_keys('indie rock')
# driver.get("https://phptravels.net/hotels")
# oras = driver.find_element(By.NAME, "childs")
# oras.send_keys('2')
# site_php_cssID = driver.find_element(By.CSS_SELECTOR, 'span[id="select2-hotels_city-container"]')

# site_php_cssID.click()