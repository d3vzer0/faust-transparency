from streaming.wordmatching.api.snapshot import Snapshot
from selenium import webdriver

class Screenshot():
    def __init__(self, url, grid='http://localhost:4444/wd/hub', browser='chrome'):
        self.url = url
        self.driver = webdriver.Remote(
            command_executor=grid,
            desired_capabilities={
                "browserName": browser
            }
        )

    def to_png(self):
        try:
            print("screenshot for {0}".format(self.url))
            self.driver.get(self.url)
            screenshot = self.driver.get_screenshot_as_png()
            print('yeet')
            self.driver.quit()

        except Exception as err:
            self.driver.quit()
            pass
        
        return screenshot
