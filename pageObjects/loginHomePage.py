import pytest
from selenium.webdriver.common.by import By

from testData.loginData import loginData


class loginHomePage:
    def __init__(self,driver):
        self.driver = driver

    img_Logo                       =  (By.XPATH, ("//*[@src='/images/logo.gif']"))

    tab_link_personal              =    (By.XPATH, ("//*[@href='/index.jsp?content=personal.htm']"))
    tab_link_smallbusiness         =    (By.XPATH, ("//*[@href='/index.jsp?content=business.htm']"))
    tab_link_InsideAltro           =    (By.XPATH, ("//*[@href='/index.jsp?content=inside.htm']"))


    link_online_banking_Login       = (By.XPATH, ("//*[@href='/login.jsp']"))
    inputUserName                   = (By.XPATH, ("//*[@id='uid']"))
    inputPassword                   = (By.XPATH, ("//*[@id='passw']"))
    btnSubmit                       = (By.XPATH, ("//*[@name='btnSubmit']"))
    linkSignOff                     = (By.XPATH, ("//*[@id='LoginLink']"))
    txtLoginFailed                  =  (By.XPATH, ("//*[@id='_ctl0__ctl0_Content_Main_message']"))

    def getLogoImage(self):
        return self.driver.find_element(*loginHomePage.img_Logo)

    def verifyTabOnlineBankingLogin(self):
        return self.driver.find_element(*loginHomePage.link_online_banking_Login)

    def verifyTabPersonal(self):
        return self.driver.find_element(*loginHomePage.tab_link_personal)

    def verifyTabSmallBusiness(self):
        return self.driver.find_element(*loginHomePage.tab_link_smallbusiness)

    def verifyTabInsideAltro(self):
        return self.driver.find_element(*loginHomePage.tab_link_InsideAltro)

    def getTabPersonal(self):
        return self.driver.find_element(*loginHomePage.link_online_banking_Login)

    def getOnlineBankingLogin(self):
        return self.driver.find_element(*loginHomePage.link_online_banking_Login)

    def setUserName(self):
        return self.driver.find_element(*loginHomePage.inputUserName)

    def setPassword(self):
        return self.driver.find_element(*loginHomePage.inputPassword)

    def getSubmit(self):
        return self.driver.find_element(*loginHomePage.btnSubmit)

    def getSignOff(self):
        return self.driver.find_element(*loginHomePage.linkSignOff)

    def getMsgLoginFailed(self):
        return self.driver.find_element(*loginHomePage.txtLoginFailed)


#def loginSuccess(self, getdata):
#self.driver.find_element(*HomePage.link_online_banking_Login).click()
#self.driver.find_element(*HomePage.inputUserName).send_keys(getdata["userName"])
#self.driver.find_element(*HomePage.inputPassword).send_keys(getdata["password"])
#self.driver.find_element(*HomePage.btnSubmit).click()
#self.driver.find_element(*HomePage.linkSignOff).click()