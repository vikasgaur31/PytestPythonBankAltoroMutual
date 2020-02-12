from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class onlineAccountInformationPage:

    def __init__(self,driver):
        self.driver = driver

    xpathLinkAccountSummaryNavigation       = (By.XPATH, ("//*[@href='/bank/main.jsp']"))
    xpathListAccountSelected                = (By.XPATH, ("//*[@name='listAccounts']"))
    xpathBtnClickGetAccount                 = (By.XPATH, ("//*[@id='btnGetAccount']"))
    xpathMessageDebtAmount                  = (By.XPATH, ("//td[contains(text(),'-$2222.00')]"))
    xpathDropdownListAccount                = (By.XPATH, ("//*[@id='listAccounts']"))
    xpathMessageTransferredAmount           = (By.XPATH, ("//td[contains(text(),'$2222.00')]"))
    xpathBtnGo                              =  (By.XPATH, ("//*[@id='btnGetAccount']"))


    # Data
    DropDownCheckAccountSelectedValue       = "800001 Checking"
    DropDownCorporateAccountSelectedValue   = "800000 Corporate"
    inputTransferAmount                     = '2222'



    # Test scenario - Account Information page
#1)	Click on View Account Summary link in left hand navigation section
    def verifyAccountSummaryLinkNavigation(self):
        self.driver.find_element(*onlineAccountInformationPage.xpathLinkAccountSummaryNavigation).click()


#2)	Select From account (same as used before) in the dropdown and click on GO button
    def verifySameFromAccountClickGo(self):
        select = Select(self.driver.find_element(*onlineAccountInformationPage.xpathListAccountSelected))
        select.select_by_visible_text(onlineAccountInformationPage.DropDownCheckAccountSelectedValue)
        self.driver.find_element(*onlineAccountInformationPage.xpathBtnClickGetAccount).click()

#3)	Verify that an entry is present in the Debits table for transaction done on Transfer Funds page.
#3.1) Verify that the amount is same as entered while transferring funds.
    def verifyDebtAmountAvailableInTable(self):
        txtDebtAmount = self.driver.find_element(*onlineAccountInformationPage.xpathMessageDebtAmount).text
        print("entry is present in the Debits table - " + txtDebtAmount)
        inputTransferMinusAmount = '-$' + str(onlineAccountInformationPage.inputTransferAmount) + '.00'
        print(inputTransferMinusAmount)
        assert inputTransferMinusAmount == txtDebtAmount, "Debits Entry is NOT present in the Debits table"

# 4) Select To Account (same as used before) in dropdown present inside Balance Detail table and click on Select Account button.
    def verifyToAccountPresentinBalanceTable(self):
        select = Select(self.driver.find_element(*onlineAccountInformationPage.xpathDropdownListAccount))
        select.select_by_visible_text(onlineAccountInformationPage.DropDownCorporateAccountSelectedValue)
        self.driver.find_element(*onlineAccountInformationPage.xpathBtnGo).click()

# 5) Verify that an entry is present in the Credits table for transaction done on Transfer Funds page.
# Verify that the amount is same as entered while transferring funds.
    def verifyAmountPresentInCreditTable(self):
        txtCreditAmount = self.driver.find_element(*onlineAccountInformationPage.xpathMessageTransferredAmount).text
        print("entry is present in the Credit table - " + txtCreditAmount)
        inputTransferMinusAmount = '$' + str(onlineAccountInformationPage.inputTransferAmount) + '.00'
        print(inputTransferMinusAmount)
        assert inputTransferMinusAmount == txtCreditAmount, "Credits Entry is NOT present in the Debits table"


