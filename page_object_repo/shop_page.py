from selenium.webdriver.common.by import By


class ShopPage():

    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    products = (By.XPATH,"//div[@class='card h-100']")
    product = (By.XPATH,"div/h4/a")


    def getProducts(self):
       return self.driver.find_elements(*ShopPage.products)

    def getProduct(self,product):
        return product.find_element(*ShopPage.product)