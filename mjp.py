from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import pyautogui

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

mjg21 = {
  "appium:automationName": "Appium",
  "appium:deviceName": "R3CR30LBMKH",
  "platformName": "Android",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", mjg21)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="아이나비 에어").click()
time.sleep(5)
driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tvSearchHint").click()
time.sleep(5)
driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/etKeyword").send_keys("서울시청")
time.sleep(5)
driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/ivSearch").click()
time.sleep(5)
driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tvButtonText").click()
time.sleep(10)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(535, 383)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()
time.sleep(5)
pyautogui.screenshot('test.png')