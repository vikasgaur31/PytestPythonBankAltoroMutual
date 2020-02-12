from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class onlineBankingHomePage:

    def __init__(self,driver):
        self.driver = driver


    xpathDropdownAccountNo              =  (By.XPATH, ("//*[@name='listAccounts']"))
    xpathBtnGo                          =  (By.XPATH, ("//*[@id='btnGetAccount']"))
    txtAccountHistory                   =  (By.XPATH, ("//h1[contains(text(),'Account History')]"))
    txtMessageBalance                   =   (By.XPATH, ("//td[contains(text(), 'Ending balance')]"))

    #Data
    DropDownCheckAccountSelectedValue       = "800001 Checking"
    DropDownCorporateAccountSelectedValue   = "800000 Corporate"
    inputTransferAmount                     = '2222'


    def getAccountDetails(self):
        dropdownSelectedText = Select(self.driver.find_element(*onlineBankingHomePage.xpathDropdownAccountNo))
        dropdownValueSelected = dropdownSelectedText.select_by_visible_text(onlineBankingHomePage.DropDownCheckAccountSelectedValue)
        dropdownSelectedNo = dropdownSelectedText.first_selected_option
        txtAccountHistory = dropdownSelectedNo.text
        print(txtAccountHistory)
        txtAccountNumber = txtAccountHistory[0:6]
        print(txtAccountNumber)
        print("Account History - " + txtAccountHistory)
        self.driver.find_element(*onlineBankingHomePage.xpathBtnGo).click()

    def verifyAccountInformationPageACNumber(self):
        txtAccountHistoryHeader = self.driver.find_element(*onlineBankingHomePage.txtAccountHistory).text
        txtAccountNumberHeader = txtAccountHistoryHeader[18:24]
        #assert "Account History - " + txtAccountHistory == txtAccountHistoryHeader, "webpage is not correctly matched"
        #assert txtAccountNumber == txtAccountNumberHeader, "Account Number is not correctly matched"
        print("On Account History Page, Account Number is correctly matched - " + txtAccountNumberHeader)

    def verifyCurrentDateWithBalanceDate(self):
        txtAccountBalanceWithDate = self.driver.find_element(*onlineBankingHomePage.txtMessageBalance).text
        txtAccountBalanceTodayDate = txtAccountBalanceWithDate[20:28]
        print("txtAccountBalanceWithDate =" + txtAccountBalanceTodayDate)

        todayDate = date.today()
        current_Date = todayDate.strftime("%m/%d/%Y")
        current_updated_Date = current_Date[1:]
        print('Today Date -' + current_updated_Date)

        if current_updated_Date == '2/10/2020':
            print("Today Date " + current_updated_Date + " is Correctly displayed in Balance Detail table under Account History Details")



'''
    btnBankTransfer                     =   (By.XPATH, ("//*[@href='/bank/transfer.jsp']"))
    txtMessageFundTransfer              =   (By.XPATH, ("//h1[contains(text(), 'Transfer Funds')]"))
    dropdownFromAccount                 =   (By.XPATH, ("//*[@name='fromAccount']"))
    dropdownToAccount                   =   (By.XPATH, ("//*[@name='toAccount']"))
    xpathInputTransferAmount            =   (By.XPATH, ("//*[@id='transferAmount']"))
    xpathBtnTransferMoney               =   (By.XPATH, ("//*[@id='transfer']"))
    xpathMessageTransferredSuccessfuly  =   (By.XPATH, ("//span[contains(text(), 'successfully transferred from Account')]"))
'''


'''
# Test scenario - Transfer Funds Page
#1)	Click on Transfer Funds link in left hand navigation section, verify that Transfer Funds page is displayed
    def verifyTranfserFundLinkCorrectPageOpened(self):
        self.driver.find_element(*onlineBankingHomePage.btnBankTransfer).click()
        txtTransferFundHeading = self.driver.find_element(*onlineBankingHomePage.txtMessageFundTransfer).text
        assert 'Transfer Funds' == txtTransferFundHeading, "Transfer Funds Text is not correctly matched on Transfer Fund Page"

# 2)	Select From Account, To Account and Amount to Transfer and click on Transfer Money button
    def verifyAccountToandFromTransferMoney(self):
        select = Select(self.driver.find_element(*onlineBankingHomePage.dropdownFromAccount))
        select.select_by_visible_text(onlineBankingHomePage.DropDownCheckAccountSelectedValue)
        SelectedValue = select.first_selected_option
        txtFromAccount = SelectedValue.text
        print(txtFromAccount)

        select = Select(self.driver.find_element(*onlineBankingHomePage.dropdownToAccount))
        select.select_by_visible_text(onlineBankingHomePage.DropDownCorporateAccountSelectedValue)
        SelectedValue1 = select.first_selected_option
        txtFromAccount1 = SelectedValue1.text
        self.driver.find_element(*onlineBankingHomePage.xpathInputTransferAmount).send_keys(onlineBankingHomePage.inputTransferAmount)
        self.driver.find_element(*onlineBankingHomePage.xpathBtnTransferMoney).click()
        print("Click on Transfer Money Button")

# 3)	Verify that a message is displayed with correct amount and from/to account details
    def verifyMessageCorrectwithAccountDetail(self):
        txtSuccessTransferredMessage = self.driver.find_element(*onlineBankingHomePage.xpathMessageTransferredSuccessfuly).text
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

    xpathLinkAccountSummaryNavigation   =   (By.XPATH, ("//*[@href='/bank/main.jsp']"))
    xpathListAccountSelected            =   (By.XPATH, ("//*[@name='listAccounts']"))
    xpathBtnClickGetAccount             =   (By.XPATH, ("//*[@id='btnGetAccount']"))
    xpathMessageDebtAmount              =   (By.XPATH, ("//td[contains(text(),'-$2222.00')]"))
    xpathDropdownListAccount            =   (By.XPATH, ("//*[@id='listAccounts']"))
    xpathMessageTransferredAmount       =   (By.XPATH, ("//td[contains(text(),'$2222.00')]"))


    # Test scenario - Account Information page
#1)	Click on View Account Summary link in left hand navigation section
    def verifyAccountSummaryLinkNavigation(self):
        self.driver.find_element(*onlineBankingHomePage.xpathLinkAccountSummaryNavigation).click()


#2)	Select From account (same as used before) in the dropdown and click on GO button
    def verifySameFromAccountClickGo(self):
        select = Select(self.driver.find_element(*onlineBankingHomePage.xpathListAccountSelected))
        select.select_by_visible_text(onlineBankingHomePage.DropDownCheckAccountSelectedValue)
        self.driver.find_element(*onlineBankingHomePage.xpathBtnClickGetAccount).click()

#3)	Verify that an entry is present in the Debits table for transaction done on Transfer Funds page.
#3.1) Verify that the amount is same as entered while transferring funds.
    def verifyDebtAmountAvailableInTable(self):
        txtDebtAmount = self.driver.find_element(*onlineBankingHomePage.xpathMessageDebtAmount).text
        print("entry is present in the Debits table - " + txtDebtAmount)
        inputTransferMinusAmount = '-$' + str(onlineBankingHomePage.inputTransferAmount) + '.00'
        print(inputTransferMinusAmount)
        assert inputTransferMinusAmount == txtDebtAmount, "Debits Entry is NOT present in the Debits table"

# 4) Select To Account (same as used before) in dropdown present inside Balance Detail table and click on Select Account button.
    def verifyToAccountPresentinBalanceTable(self):
        select = Select(self.driver.find_element(*onlineBankingHomePage.xpathDropdownListAccount))
        select.select_by_visible_text(onlineBankingHomePage.DropDownCorporateAccountSelectedValue)
        self.driver.find_element(*onlineBankingHomePage.xpathBtnGo).click()

# 5) Verify that an entry is present in the Credits table for transaction done on Transfer Funds page.
# Verify that the amount is same as entered while transferring funds.
    def verifyAmountPresentInCreditTable(self):
        txtCreditAmount = self.driver.find_element(*onlineBankingHomePage.xpathMessageTransferredAmount).text
        print("entry is present in the Credit table - " + txtCreditAmount)
        inputTransferMinusAmount = '$' + str(onlineBankingHomePage.inputTransferAmount) + '.00'
        print(inputTransferMinusAmount)
        assert inputTransferMinusAmount == txtCreditAmount, "Credits Entry is NOT present in the Debits table"




'''
