from selenium import webdriver

## constants
# username = "<YOUR_LAMBDATEST_USERNAME>"
username = "itssvinayak"
# access_key = "<YOUR__LAMBDATEST_ACCESS_KEY>"
access_key = "ikeqE9WZrVc0FbweXa1iIcTrnfiYRrifw0pHmnTqA5RV7OSR1x"

## your desired capabilities from lambdatest
desired_caps = {
    "build": "Build_Name",
    "name": "Test_Name",
    "platform": "Windows 10",
    "browserName": "Chrome",
    "version": "92.0",
    "selenium_version": "3.13.0",
    "geoLocation": "IN",
    "chrome.driver": "91.0",
}

"""
Setup remote driver 
        -------
        username and access_key can be found on the lt platform

"""
driver = webdriver.Remote(
    command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(
        username, access_key
    ),
    desired_capabilities=desired_caps,
)

## to maximize the browser window
driver.maximize_window()
## opening webpage
driver.get("https://accounts.lambdatest.com/login")

## xpath for our element
email_xpath = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]"
password_xpath = (
    "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]"
)
login_button_xpath = (
    "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]"
)

## selecting element
email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

email_element.send_keys("itssvinayak@gmail.com")
password_element.send_keys("Vinayak@123")

## clicking on login button
login_button_element.click()

## to save screenshot for verification
## this screenshort can be found in you local storage
driver.save_screenshot("screenshot.png")

# to close the browser
driver.close()
