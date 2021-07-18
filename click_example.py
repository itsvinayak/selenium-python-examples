from selenium import webdriver
from selenium.webdriver import ActionChains

## constants
username = "<YOUR_LAMBDATEST_USERNAME>"
access_key = "<YOUR__LAMBDATEST_ACCESS_KEY>"

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
driver.get("https://www.lambdatest.com/")
## selecting element 
live_button = driver.find_element_by_xpath('//body[1]/div[1]/header[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/a[1]')


## creating a Action chain object
action = ActionChains(driver)

## calling function to click live button
action.click(live_button)

## perform the action
action.perform()

## to save screenshot for verification 
## this screenshort can be found in you local storage
driver.save_screenshot("screenshot.png")

#to close the browser
driver.close()