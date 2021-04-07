
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from page_object_repo.home_page import HomePage
from page_object_repo.shop_page import ShopPage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):

    def test1(self,setup):

        homePage = HomePage(self.driver)
        #homePage.getShop().click()
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()

        shopPage = homePage.clickShop()

        #shopPage = ShopPage(self.driver)
        products = shopPage.getProducts()

        for product in products:
            productName = shopPage.getProduct(product).text
            if productName == "Blackberry":
                # Add item into cart
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.waitTillElementWithLinkTextPresent(7,'India')

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")


