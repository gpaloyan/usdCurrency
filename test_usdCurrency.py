from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = r"C:\Your_ChromeDriver_Path"
browser = webdriver.Chrome(PATH)

browser.get("https://rate.am")
browser.maximize_window()
browser.implicitly_wait(15)

usdBuyPriceList = browser.find_elements(By.XPATH, "//table[@id='rb']/tbody/tr[@id]/td[6]")

def test_usdCurrency():
    temp = []
    for usdPrice in usdBuyPriceList:
        temp.append(float(usdPrice.text))

    for i in range(len(temp) - 1):
        for j in range(0, len(temp) - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]

    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            assert temp[i] <= temp[j], "The List does not Sorted"