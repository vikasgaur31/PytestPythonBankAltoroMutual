from datetime import date

import pytest
from selenium import webdriver

from pageObjects import loginHomePage
from pageObjects.onlineAccountInformationPage import onlineAccountInformationPage
from pageObjects.onlineBankingHomePage import onlineBankingHomePage
from pageObjects.onlineTransferFundPage import onlineTransferFundPage
from testData.loginData import loginData
from utilities.BaseClass import BaseClass
from pageObjects.loginHomePage import loginHomePage
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class TestOnlineBank(BaseClass):

# 1) Test Logo Image - Verify that AltoroMutual logo image is displayed in top left
    def test_logo_available(self):
        loginPage = loginHomePage(self.driver)
        logoAvailable = loginPage.getLogoImage().is_displayed()
        if logoAvailable == True:
            print("Logo is displayed")
        else:
            raise ("Logo is not displaying")

# 2) Test Top Four Tabs - Verify that following four tabs are displayed at the top: ONLINE BANKING LOGIN, PERSONAL, SMALL BUSINESS and INSIDE ALTORO MUTUAL
    def test_top_four_tabs(self):
        loginPage = loginHomePage(self.driver)

        OnlineBankingLoginAvailable = loginPage.verifyTabOnlineBankingLogin().is_enabled()
        if OnlineBankingLoginAvailable == True:
            print("OnlineBankingLoginAvailable tab available and enabled")
        else:
            print("OnlineBankingLoginAvailable tab NOT available and enabled")

        tabPersonalAvailable = loginPage.verifyTabPersonal().is_enabled()
        if tabPersonalAvailable == True:
            print("Personal tab available and enabled")
        else:
            print("Personal tab NOT available and enabled")


        tabSmallBusinessAvailable = loginPage.verifyTabSmallBusiness().is_enabled()
        if tabSmallBusinessAvailable == True:
            print("Small Business tab available and enabled")
        else:
            print("Small Business tab NOT available and enabled")


        tabInsideAltro = loginPage.verifyTabInsideAltro().is_enabled()
        if tabInsideAltro == True:
            print("InsideAltro tab available and enabled")
        else:
            print("InsideAltro tab NOT available and enabled")

# 3) Test Login Failure - Verify that when user enters incorrect username and password then following Login Failed message should be displayed.
    def test_login_failure(self, getLoginFailureData):
        loginPage = loginHomePage(self.driver)
        loginPage.getOnlineBankingLogin().click()
        print(getLoginFailureData)
        loginPage.setUserName().send_keys(getLoginFailureData["UserName"])
        loginPage.setPassword().send_keys(getLoginFailureData["Password"])
        loginPage.getSubmit().click()
        print(getLoginFailureData)
        msgLoginFailied = loginPage.getMsgLoginFailed().text
        print(msgLoginFailied)
        assert msgLoginFailied == "Login Failed: We're sorry, but this username or password was not found in our system. Please try again.", "Login Failed message successfully matched"
        # print("Login Failed message successfully matched")
        loginPage.getSignOff().click()


# 4) Login Success - Verify that when user enters valid username and password then Online Banking Home page should be displayed.
    def test_login_success(self,getLoginSuccessData):
        loginPage = loginHomePage(self.driver)
        loginPage.getOnlineBankingLogin().click()
        print (getLoginSuccessData)
        #if getData == "{'UserName': 'admin', 'Password': 'admin'}":
        loginPage.setUserName().send_keys(getLoginSuccessData["UserName"])
        loginPage.setPassword().send_keys(getLoginSuccessData["Password"])
        #print("entered correct user name")
        #elif getData == "{'UserName': 'admin', 'Password': 'admin1'}":
        #assert loginData.test_loginData == "Login Failed: We're sorry, but this username or password was not found in our system. Please try again."
        #print("entered Incorrect user name")
        loginPage.getSubmit().click()
        loginPage.getSignOff().click()

#Online Banking Home
    # 1)Select a bank account in View Account Details dropdown and click on GO button

#def test_verifyAccountDetails(self):
    def test_e2e_OnlineBank(self):
    #Login Page
        loginPage = loginHomePage(self.driver)
        loginPage.getOnlineBankingLogin().click()
        loginPage.setUserName().send_keys("admin")
        loginPage.setPassword().send_keys("admin")
        loginPage.getSubmit().click()

# Test scenario - Online Banking Home
        onlineBankingPage = onlineBankingHomePage(self.driver)
        onlineBankingPage.getAccountDetails()
        onlineBankingPage.verifyAccountInformationPageACNumber()
        onlineBankingPage.verifyCurrentDateWithBalanceDate()


# Test scenario - Transfer Funds Page
        onlineTransferFund = onlineTransferFundPage(self.driver)

        onlineTransferFund.verifyTranfserFundLinkCorrectPageOpened()
        onlineTransferFund.verifyAccountToandFromTransferMoney()
        onlineTransferFund.verifyMessageCorrectwithAccountDetail()

# Test scenario - Account Information page
#1)	Click on View Account Summary link in left hand navigation section
        onlineAccountInformation = onlineAccountInformationPage(self.driver)

        onlineAccountInformation.verifyAccountSummaryLinkNavigation()
        onlineAccountInformation.verifySameFromAccountClickGo()
        onlineAccountInformation.verifyDebtAmountAvailableInTable()
        onlineAccountInformation.verifyToAccountPresentinBalanceTable()
        onlineAccountInformation.verifyAmountPresentInCreditTable()

    @pytest.fixture(params=loginData.test_loginSuccessData) #Data Handling with dictonary
    def getLoginSuccessData(self, request):
        return request.param

    @pytest.fixture(params=loginData.test_loginFailureData)  # Data Handling with dictonary
    def getLoginFailureData(self, request):
        return request.param



'''     
#Online Banking Home
    # 1)Select a bank account in View Account Details dropdown and click on GO button
        dropdownSelectedText = Select(self.driver.find_element_by_xpath("//*[@name='listAccounts']"))
        dropdownValueSelected = dropdownSelectedText.select_by_index(1)
        dropdownSelectedNo = dropdownSelectedText.first_selected_option
        txtAccountHistory = dropdownSelectedNo.text
        print(txtAccountHistory)
        txtAccountNumber = txtAccountHistory[0:6]
        print(txtAccountNumber)
        print("Account History - " + txtAccountHistory)
        self.driver.find_element_by_xpath("//*[@id='btnGetAccount']").click()

#2)	Verify Account Information page is displayed. Also verify that account number displayed in heading Account History - <Account no.> is same as bank account selected in above step
        txtAccountHistoryHeader = self.driver.find_element_by_xpath("//h1[contains(text(),'Account History')]").text
        txtAccountNumberHeader = txtAccountHistoryHeader[18:24]
        assert "Account History - " + txtAccountHistory == txtAccountHistoryHeader, "webpage is not correctly matched"
        assert txtAccountNumber == txtAccountNumberHeader, "Account Number is not correctly matched"
        print("Account History Account Number is correctly matched - " + txtAccountNumberHeader)

#3)	Verify that current date is displayed in Balance Detail table (Ending balance as of <Date>)
        txtAccountBalanceWithDate = self.driver.find_element_by_xpath("//td[contains(text(), 'Ending balance')]").text
        txtAccountBalanceTodayDate = txtAccountBalanceWithDate[20:28]
        print("txtAccountBalanceWithDate =" + txtAccountBalanceTodayDate)

        todayDate = date.today()
        current_Date = todayDate.strftime("%m/%d/%Y")
        current_updated_Date = current_Date[1:]
        print('Today Date -' + current_updated_Date)

        if current_updated_Date == '2/10/2020':
            print("Today Date " + current_updated_Date + " is Correctly displayed in Balance Detail table under Account History Details")

# Test scenario - Transfer Funds Page
#1)	Click on Transfer Funds link in left hand navigation section, verify that Transfer Funds page is displayed
        self.driver.find_element_by_xpath("//*[@href='/bank/transfer.jsp']").click()
        txtTransferFundHeading = self.driver.find_element_by_xpath("//h1[contains(text(), 'Transfer Funds')]").text
        assert 'Transfer Funds' == txtTransferFundHeading, "Transfer Funds Text is not correctly matched on Transfer Fund Page"

# 2)	Select From Account, To Account and Amount to Transfer and click on Transfer Money button
        select = Select(self.driver.find_element_by_xpath("//*[@name='fromAccount']"))
        select.select_by_visible_text("800001 Checking")
        SelectedValue = select.first_selected_option
        txtFromAccount = SelectedValue.text
        print(txtFromAccount)

        select = Select(self.driver.find_element_by_xpath("//*[@name='toAccount']"))
        select.select_by_visible_text("800000 Corporate")
        SelectedValue1 = select.first_selected_option
        txtFromAccount1 = SelectedValue1.text
        print(txtFromAccount1)
        inputTransferAmount = 2222
        self.driver.find_element_by_xpath("//*[@id='transferAmount']").send_keys(inputTransferAmount)
        # inputTransferAmount.text
        self.driver.find_element_by_xpath("//*[@id='transfer']").click()
        print("Click on Transfer Money Button")

#3)	Verify that a message is displayed with correct amount and from/to account details
        txtSuccessTransferredMessage = self.driver.find_element_by_xpath("//span[contains(text(), 'successfully transferred from Account')]").text
        txtSuccessMessage = txtSuccessTransferredMessage.split('from Account')[1]
        txtSuccessMessageAmount = txtSuccessTransferredMessage.split(' ', 1)[0]
        txtSuccessMessageFromAccount = txtSuccessMessage[1:7]
        txtSuccessMessageToAccount = txtSuccessMessage[21:27]

        print("txtSuccessTransferredMessage - " + txtSuccessTransferredMessage)
        print("txtSuccessTransferredAmount - " + txtSuccessMessageAmount)
        print("txtSuccessTransferredFromAccount - " + txtSuccessMessageFromAccount)
        print("txtSuccessTransferredToAccount - " + txtSuccessMessageToAccount)

        assert '2222.0' == txtSuccessMessageAmount, "Transfer Amount is not correctly matched"
        assert '800001' == txtSuccessMessageFromAccount, "Transfer From Account No is not correctly matched"
        assert '800000' == txtSuccessMessageToAccount, "Transfer To Account No is not correctly matched"

# Test scenario - Account Information page
#1)	Click on View Account Summary link in left hand navigation section
        self.driver.find_element_by_xpath("//*[@href='/bank/main.jsp']").click()

#2)	Select From account (same as used before) in the dropdown and click on GO button
        select = Select(self.driver.find_element_by_xpath("//*[@name='listAccounts']"))
        select.select_by_visible_text("800001 Checking")
        self.driver.find_element_by_xpath("//*[@id='btnGetAccount']").click()

#3)	Verify that an entry is present in the Debits table for transaction done on Transfer Funds page.
#3.1) Verify that the amount is same as entered while transferring funds.
        txtDebtAmount = self.driver.find_element_by_xpath("//td[contains(text(),'-$2222.00')]").text
        print("entry is present in the Debits table - " + txtDebtAmount)
        inputTransferMinusAmount = '-$' + str(inputTransferAmount) + '.00'
        print(inputTransferMinusAmount)
        assert inputTransferMinusAmount == txtDebtAmount, "Debits Entry is NOT present in the Debits table"

# 4) Select To Account (same as used before) in dropdown present inside Balance Detail table and click on Select Account button.
        select = Select(self.driver.find_element_by_xpath("//*[@id='listAccounts']"))
        select.select_by_visible_text("800000 Corporate")
        self.driver.find_element_by_xpath("//*[@id='btnGetAccount']").click()

# 5) Verify that an entry is present in the Credits table for transaction done on Transfer Funds page.
# Verify that the amount is same as entered while transferring funds.
        txtCreditAmount = self.driver.find_element_by_xpath("//td[contains(text(),'$2222.00')]").text
        print("entry is present in the Credit table - " + txtCreditAmount)
        inputTransferMinusAmount = '$' + str(inputTransferAmount) + '.00'
        print(inputTransferMinusAmount)
        assert inputTransferMinusAmount == txtCreditAmount, "Credits Entry is NOT present in the Debits table"

'''



#self.driver.find_element_by_xpath("//*[@href='/login.jsp']").click()
        #loginPage.loginSuccess(self.getdata)

'''
driver = webdriver.Chrome(executable_path="C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.get("http://demo.testfire.net/index.jsp")
driver.maximize_window()
driver.find_element_by_xpath("//*[@href='/login.jsp']").click()
driver.find_element_by_xpath("//*[@id='uid']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='passw']").send_keys("admin")
driver.find_element_by_xpath("//*[@name='btnSubmit']").click()
driver.find_element_by_xpath("//*[@id='LoginLink']").click()
driver.quit()
'''

