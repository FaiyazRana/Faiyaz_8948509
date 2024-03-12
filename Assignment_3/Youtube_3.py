# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the YouTube.com
driver.get("https://www.youtube.com/")
time.sleep(8)

# Selecting Main menu of the YouTube
Mainmenu_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[1]/yt-icon-button["
                                             "2]/button/yt-icon/yt-icon-shape/icon-shape/div")
Mainmenu_link.click()

time.sleep(4)
# selecting Sport option
Sport_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div["
                                          "2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer["
                                          "3]/div/ytd-guide-entry-renderer[7]/a/tp-yt-paper-item/yt-formatted-string")
Sport_link.click()
time.sleep(5)

# selecting Sport vidoe
Video_link1 = driver.find_element("id", "video-title")
Video_link1.click()
time.sleep(5)

# Selecting Like button for  the video
button = driver.find_element(By.CLASS_NAME, "YtLikeButtonViewModelHost")
button.click()

time.sleep(5)

# selecting sign-in to liking the video
button = driver.find_element(By.XPATH,
                             "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and"
                             "-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div"
                             "/div[2]")
button.click()

time.sleep(5)

driver.close()
