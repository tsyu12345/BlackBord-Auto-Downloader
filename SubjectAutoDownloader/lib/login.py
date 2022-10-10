from __future__ import annotations
from typing import Final as const

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import chromedriver_binary

from Interface import ILoginParam, AbsLogin, ILoginresult


class Login(AbsLogin):
    
    def __init__(self, login_param: ILoginParam) -> None:
        super().__init__(login_param)
        self.driver = webdriver.Chrome()
        
        
    def __login(self) -> None:
        self.driver.get("https://nuchs.blackboard.com/")
        
        login_selector:const[WebElement] = self.driver.find_element(By.ID, "redirectProvidersDropdownButton")
        login_selector.click()

        account_select:const[WebElement] = self.driver.find_element(By.CSS_SELECTOR, "#loginRedirectProviderList > li > a")
        account_select.click()
        
        #switch to login form of Microsoft
        self.driver.switch_to.window(self.driver.window_handles[1])
        next_button_id: const[str] = "idSIButton9"
        
        #input mail address
        mail_input:const[WebElement] = self.driver.find_element(By.ID, "i0116")
        mail_input.send_keys(self.login_param.address)
        
        self.driver.find_element(By.ID, next_button_id).click()       
        #input password
        password_input:const[WebElement] = self.driver.find_element(By.ID, "i0118")
        password_input.send_keys(self.login_param.password)
        
        self.driver.find_element(By.ID, next_button_id).click()
        
        #サインインの維持選択画面があるか否か
        maintain_select_window: const[list[WebElement]] = self.driver.find_elements(By.ID, "lightbox")
        if len(maintain_select_window) == 0:
            pass
        else:
            self.driver.find_element(By.ID, next_button_id).click()
    
    def login(self) -> ILoginresult:
        try:
            self.__login()
            return ILoginresult.SUCCESS
        except:
            return ILoginresult.FAILED
        
"""TEST CODE BELOW"""

if __name__ == "__main__":
    
    login_param = ILoginParam(
        address="y5419045@stu.chs.nihon-u.ac.jp",
        password="05152000s"
    )
    
    test = Login(login_param)
    result: const = test.login()
    print("RESULT: ", result)    