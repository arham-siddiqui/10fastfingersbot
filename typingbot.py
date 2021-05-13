from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

URL = "https://10fastfingers.com/typing-test/english"

def calculate_sleep_time(wpm):
    return 60/wpm

class Automation:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(URL)
        print('wait 5 seconds...')
        sleep(5)
        self._close_cookie_prompt()
    def _close_cookie_prompt(self):
        button_id = "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection"
        self.driver.find_element_by_id(button_id).click()
    def _find_relevant_text(self):
        return self.driver.find_element_by_id("wordlist").get_attribute("innerHTML").split("|")
    
    @property
    def text(self):
        return self._find_relevant_text()
    
    def type(self):
        text = self.text
        wpm = 95
        text = text[:wpm]
        sleep_duration = calculate_sleep_time(wpm) - 0.13
        input_field = self.driver.find_element_by_id("inputfield")
        input_field.click()
        for word in text:
            print(f"typing {word}")
            input_field.send_keys(word + " ")
            sleep(sleep_duration)
        sleep(10)
        print('Finished Typing')

automation = Automation()
automation.type()