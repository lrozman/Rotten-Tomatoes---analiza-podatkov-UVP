from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

import os


driver = webdriver.Chrome()

def pridobi_stran(st_zanra):
    driver.get("https://www.rottentomatoes.com/browse/tv_series_browse/genres:action~sort:popular")
    sleep(5)

    #r = pri vsakem žanru pač nekaj

    for _ in range(10):
        button = driver.find_element(
            By.CSS_SELECTOR,
            "button[data-qa='dlp-load-more-button']",
        )
        #button.send_keys(Keys.RETURN)
        button.click()
        sleep(2)

    with open(os.path.join("Neobdelani_podatki", "Strani", f"stran{st_zanra}.html"), "w", encoding="utf-8") as dat:
        dat.write(driver.page_source)