# Sensitive data is being accessed through environemt variables
# more info: https://www.youtube.com/watch?v=IolxqkL7cD8&ab_channel=CoreySchafer
import os

def fillForm(driver):
    firstName = 'Duc'
    firstNameInput = driver.find_element_by_xpath('//*[@id="powermail_field_vorname"]')
    firstNameInput.send_keys(firstName)

    lastName = 'Nguyen'
    lastNameInput = driver.find_element_by_xpath('//*[@id="powermail_field_name"]')
    lastNameInput.send_keys(lastName)


    street = os.environ.get('street')
    streetInput = driver.find_element_by_xpath('//*[@id="powermail_field_strasse"]')
    streetInput.send_keys(street)


    pCode = '10961'
    pCodeInput = driver.find_element_by_xpath('//*[@id="powermail_field_plz"]')
    pCodeInput.send_keys(pCode)


    city = 'Berlin'
    cityInput = driver.find_element_by_xpath('//*[@id="powermail_field_ort"]')
    cityInput.send_keys(city)


    email = os.environ.get('email')
    emailInput = driver.find_element_by_xpath('//*[@id="powermail_field_e_mail"]')
    emailInput.send_keys(email)


    tel = os.environ.get('telephone')
    telInput = driver.find_element_by_xpath('//*[@id="powermail_field_telefon"]')
    telInput.send_keys(tel)

    privacyCheckbox = driver.find_element_by_xpath('//*[@id="c722"]/div/div/form/div[2]/div[13]/div/div/div[1]/label')
    privacyCheckbox.click()

    sendFormButton= driver.find_element_by_xpath('//*[@id="c722"]/div/div/form/div[2]/div[14]/div/div/button')
    #sendFormButton.click()
    print('done')