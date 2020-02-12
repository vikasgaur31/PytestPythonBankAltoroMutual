import pytest

from pageObjects.loginHomePage import loginHomePage
from pageObjects.onlineBankingHomePage import onlineBankingHomePage
from testData import loginData
from tests import test_OnlineBanking_Altoro
from tests.test_OnlineBanking_Altoro import TestLogin
from utilities.BaseClass import BaseClass

'''
@pytest.mark.usefixtures("setup")
class TestOnlineBankingHome(BaseClass):

    def test_verifyAccountDetails(self,getLoginSuccessData):
        #test_login.TestLogin.test_login_success(self,getLoginSuccessData)
        loginPage = loginHomePage(self.driver)
        loginPage.getOnlineBankingLogin().click()
        #print(getLoginSuccessData)
        # if getData == "{'UserName': 'admin', 'Password': 'admin'}":
        loginPage.setUserName().send_keys(getLoginSuccessData["UserName"])
        loginPage.setPassword().send_keys(getLoginSuccessData["Password"])
        # print("entered correct user name")
        # elif getData == "{'UserName': 'admin', 'Password': 'admin1'}":
        # assert loginData.test_loginData == "Login Failed: We're sorry, but this username or password was not found in our system. Please try again."
        # print("entered Incorrect user name")
        loginPage.getSubmit().click()



        onlineBankingPage = onlineBankingHomePage(self.driver)
        dropdownSelectedText = onlineBankingPage.getAccountDetails().select_by_index(1)
        #dropdownSelectedGetText = onlineBankingPage.getAccountDetails().dropdownSelected().first_selected_option
        print("test_onlineBankingHome - dropdownSelectedText", dropdownSelectedText.first_selected_option)
        #print("test_onlineBankingHome - dropdownSelectedGetText", dropdownSelectedGetText)


    #def verifyAccountInformationpage(self):


    #def verifyAccountNumber(self):


    #def verifyCurrentDate(self):



    @pytest.fixture(params=loginData.test_loginSuccessData) #Data Handling with dictonary
    def getLoginSuccessData(self, request):
        return request.param

'''