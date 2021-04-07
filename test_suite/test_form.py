from selenium.webdriver.support.select import Select

from page_object_repo.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestForm(BaseClass):


    def test_submit_form(self,data):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        #homepage.getName().send_keys(data[0])

        homepage.enterNameValue(data[0])
        #self.driver.find_element_by_name("name").send_keys(data[0])
        log.info(f'Name with value {data[0]} has been entered')
        self.driver.find_element_by_name("email").send_keys(data[1])
        log.info(f'Email with value {data[1]} has been entered')



        self.driver.find_element_by_id("exampleInputPassword1").send_keys(data[2])
        self.selectValueWithText(self.driver.find_element_by_id("exampleFormControlSelect1"),data[3])


        self.driver.find_element_by_xpath("//*[@type='submit']").submit()
        message = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        print(f'message: {message}')
        assert 'Success' in message , 'Form not submitted successfully'





