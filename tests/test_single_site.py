from datetime import date

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Browsers_Selenium\\Chrome\\ChromeDriver.exe")
driver.get("http://demo.testfire.net/index.jsp")
driver.maximize_window()

logoAvailable = driver.find_element_by_xpath("//*[@src='/images/logo.gif']").is_displayed()
if logoAvailable == True:
    print("Logo is displayed")
else:
    raise ("Logo is not displaying")

driver.find_element_by_xpath("//*[@href='/login.jsp']").is_enabled()
driver.find_element_by_xpath("//*[@href='/index.jsp?content=personal.htm']").is_enabled()
driver.find_element_by_xpath("//*[@href='/index.jsp?content=business.htm']").is_enabled()
driver.find_element_by_xpath("//*[@href='/index.jsp?content=inside.htm']").is_enabled()
print("Top is displayed")


driver.find_element_by_xpath("//*[@href='/login.jsp']").click()
driver.find_element_by_xpath("//*[@id='uid']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='passw']").send_keys("admin")
driver.find_element_by_xpath("//*[@name='btnSubmit']").click()
#message = driver.find_element_by_xpath("//*[@id='_ctl0__ctl0_Content_Main_message']").text
#print(message)


# Test scenario - Online Banking Home
#1)	Select a bank account in View Account Details dropdown and click on GO button
#driver.find_element_by_xpath("//*[@name='listAccounts']").is_selected(1)#send_keys("800000 Corporate")
select = Select(driver.find_element_by_xpath("//*[@name='listAccounts']"))
dropdownValueSelected = select.select_by_index(0)
option = select.first_selected_option
txtAccountHistory = option.text
print(txtAccountHistory)
txtAccountNumber = txtAccountHistory[0:6]
print(txtAccountNumber)
print ("Account History - " + txtAccountHistory)
driver.find_element_by_xpath("//*[@id='btnGetAccount']").click()


#2)	Verify Account Information page is displayed. Also verify that account number displayed in heading Account History - <Account no.> is same as bank account selected in above step
txtAccountHistoryHeader = driver.find_element_by_xpath("//h1[contains(text(),'Account History')]").text
txtAccountNumberHeader = txtAccountHistoryHeader[18:24]
assert "Account History - " + txtAccountHistory == txtAccountHistoryHeader, "webpage is not correctly matched"
assert txtAccountNumber == txtAccountNumberHeader, "Account Number is not correctly matched"


#3)	Verify that current date is displayed in Balance Detail table (Ending balance as of <Date>)
txtAccountBalanceWithDate = driver.find_element_by_xpath("//td[contains(text(), 'Ending balance')]").text
txtAccountBalanceTodayDate = txtAccountBalanceWithDate[20:28]
print("txtAccountBalanceWithDate =" + txtAccountBalanceTodayDate)


todayDate = date.today()
current_Date = todayDate.strftime("%m/%d/%Y")
current_updated_Date = current_Date[1:]
print('Today Date -' + current_updated_Date)

if current_updated_Date == '2/10/2020':
    print("Today Date " + current_updated_Date +  " is Correctly displayed in Balance Detail table under Account History Details")


# Test scenario - Transfer Funds Page
#1)	Click on Transfer Funds link in left hand navigation section, verify that Transfer Funds page is displayed
driver.find_element_by_xpath("//*[@href='/bank/transfer.jsp']").click()
txtTransferFundHeading = driver.find_element_by_xpath("//h1[contains(text(), 'Transfer Funds')]").text
assert 'Transfer Funds' == txtTransferFundHeading, "Transfer Funds Text is not correctly matched on Transfer Fund Page"

#2)	Select From Account, To Account and Amount to Transfer and click on Transfer Money button
select = Select(driver.find_element_by_xpath("//*[@name='fromAccount']"))
select.select_by_visible_text("800001 Checking")
SelectedValue = select.first_selected_option
txtFromAccount = SelectedValue.text
print(txtFromAccount)

select = Select(driver.find_element_by_xpath("//*[@name='toAccount']"))
select.select_by_visible_text("800000 Corporate")
SelectedValue1 = select.first_selected_option
txtFromAccount1 = SelectedValue1.text
print(txtFromAccount1)
inputTransferAmount = 2222
driver.find_element_by_xpath("//*[@id='transferAmount']").send_keys(inputTransferAmount)
#inputTransferAmount.text
driver.find_element_by_xpath("//*[@id='transfer']").click()
print("Click on Transfer Money Button")


#3)	Verify that a message is displayed with correct amount and from/to account details
txtSuccessTransferredMessage = driver.find_element_by_xpath("//span[contains(text(), 'successfully transferred from Account')]").text

txtSuccessMessage = txtSuccessTransferredMessage.split('from Account')[1]
txtSuccessMessageAmount = txtSuccessTransferredMessage.split(' ', 1)[0]
txtSuccessMessageFromAccount = txtSuccessMessage[1:7]
txtSuccessMessageToAccount =  txtSuccessMessage[21:27]

print("txtSuccessTransferredMessage - " + txtSuccessTransferredMessage)
print("txtSuccessTransferredAmount - " + txtSuccessMessageAmount)
print("txtSuccessTransferredFromAccount - " + txtSuccessMessageFromAccount)
print("txtSuccessTransferredToAccount - " + txtSuccessMessageToAccount)

assert '2222.0' == txtSuccessMessageAmount, "Transfer Amount is not correctly matched"
assert '800001' == txtSuccessMessageFromAccount, "Transfer From Account No is not correctly matched"
assert '800000' == txtSuccessMessageToAccount, "Transfer To Account No is not correctly matched"

# Test scenario - Account Information page
#1)	Click on View Account Summary link in left hand navigation section
driver.find_element_by_xpath("//*[@href='/bank/main.jsp']").click()

#2)	Select From account (same as used before) in the dropdown and click on GO button
select = Select(driver.find_element_by_xpath("//*[@name='listAccounts']"))
select.select_by_visible_text("800001 Checking")
driver.find_element_by_xpath("//*[@id='btnGetAccount']").click()

#3)	Verify that an entry is present in the Debits table for transaction done on Transfer Funds page.
#3.1) Verify that the amount is same as entered while transferring funds.
txtDebtAmount = driver.find_element_by_xpath("//td[contains(text(),'-$2222.00')]").text
print("entry is present in the Debits table - " + txtDebtAmount)
inputTransferMinusAmount = '-$'+str(inputTransferAmount)+'.00'
print(inputTransferMinusAmount)
assert inputTransferMinusAmount == txtDebtAmount, "Debits Entry is NOT present in the Debits table"

#4) Select To Account (same as used before) in dropdown present inside Balance Detail table and click on Select Account button.
select = Select(driver.find_element_by_xpath("//*[@id='listAccounts']"))
select.select_by_visible_text("800000 Corporate")
driver.find_element_by_xpath("//*[@id='btnGetAccount']").click()

#5)	Verify that an entry is present in the Credits table for transaction done on Transfer Funds page.
#Verify that the amount is same as entered while transferring funds.
txtCreditAmount = driver.find_element_by_xpath("//td[contains(text(),'$2222.00')]").text
print("entry is present in the Credit table - " + txtCreditAmount)
inputTransferMinusAmount = '$'+str(inputTransferAmount)+'.00'
print(inputTransferMinusAmount)
assert inputTransferMinusAmount == txtCreditAmount, "Credits Entry is NOT present in the Debits table"

#6) Click on Sign off link at the top and verify that user is signed off.








#driver.find_element_by_xpath("//*[@id='LoginLink']").click()
#driver.quit()