from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def main():
    chrome = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    chrome.get('http://code-on.be/')
    chrome.save_screenshot('/tmp/screen.png')


main()
