from datetime import date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class onlineTransferFundPage:

    def __init__(self,driver):
        self.driver = driver

    btnBankTransfer                     =   (By.XPATH, ("//*[@href='/bank/transfer.jsp']"))
    txtMessageFundTransfer              =   (By.XPATH, ("//h1[contains(text(), 'Transfer Funds')]"))
    dropdownFromAccount                 =   (By.XPATH, ("//*[@name='fromAccount']"))
    dropdownToAccount                   =   (By.XPATH, ("//*[@name='toAccount']"))
    xpathInputTransferAmount            =   (By.XPATH, ("//*[@id='transferAmount']"))
    xpathBtnTransferMoney               =   (By.XPATH, ("//*[@id='transfer']"))
    xpathMessageTransferredSuccessfuly  =   (By.XPATH, ("//span[contains(text(), 'successfully transferred from Account')]"))

    #Data
    DropDownCheckAccountSelectedValue       = "800001 Checking"
    DropDownCorporateAccountSelectedValue   = "800000 Corporate"
    inputTransferAmount                     = '2222'


# Test scenario - Transfer Funds Page
#1)	Click on Transfer Funds link in left hand navigation section, verify that Transfer Funds page is displayed
    def verifyTranfserFundLinkCorrectPageOpened(self):
        self.driver.find_element(*onlineTransferFundPage.btnBankTransfer).click()
        txtTransferFundHeading = self.driver.find_element(*onlineTransferFundPage.txtMessageFundTransfer).text
        assert 'Transfer Funds' == txtTransferFundHeading, "Transfer Funds Text is not correctly matched on Transfer Fund Page"

# 2)	Select From Account, To Account and Amount to Transfer and click on Transfer Money button
    def verifyAccountToandFromTransferMoney(self):
        select = Select(self.driver.find_element(*onlineTransferFundPage.dropdownFromAccount))
        select.select_by_visible_text(onlineTransferFundPage.DropDownCheckAccountSelectedValue)
        SelectedValue = select.first_selected_option
        txtFromAccount = SelectedValue.text
        print(txtFromAccount)

        select = Select(self.driver.find_element(*onlineTransferFundPage.dropdownToAccount))
        select.select_by_visible_text(onlineTransferFundPage.DropDownCorporateAccountSelectedValue)
        SelectedValue1 = select.first_selected_option
        txtFromAccount1 = SelectedValue1.text
        self.driver.find_element(*onlineTransferFundPage.xpathInputTransferAmount).send_keys(onlineTransferFundPage.inputTransferAmount)
        self.driver.find_element(*onlineTransferFundPage.xpathBtnTransferMoney).click()
        print("Click on Transfer Money Button")

# 3)	Verify that a message is displayed with correct amount and from/to account details
    def verifyMessageCorrectwithAccountDetail(self):
        txtSuccessTransferredMessage = self.driver.find_element(*onlineTransferFundPage.xpathMessageTransferredSuccessfuly).text
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

