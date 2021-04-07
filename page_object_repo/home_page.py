from selenium.webdriver.common.by import By

from page_object_repo.shop_page import ShopPage


class HomePage():

    def __init__(self,driver):
        self.driver = driver


    shop = (By.CSS_SELECTOR,"a[href*='shop']")

    #self.driver.find_element_by_css_selector("a[href*='shop']")


    def getShop(self):
        return self.driver.find_element(*HomePage.shop)

    def clickShop(self):
        self.getShop().click()
        return ShopPage(self.driver)

    name = (By.NAME,'name')
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def enterNameValue(self,value):
        self.driver.find_element(*HomePage.name).send_keys(value)
    #self.driver.find_element_by_name("name")