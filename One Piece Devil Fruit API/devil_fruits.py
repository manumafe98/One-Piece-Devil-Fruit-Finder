import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class DevilFruits:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.fruits = []
        self.fruits_dict = {}

    def get_fruits(self, div):
        self.driver.get("https://onepiece.fandom.com/wiki/Devil_Fruit")
        time.sleep(1)
        div_element = self.driver.find_element(By.XPATH, div)
        time.sleep(1)
        span_elements = div_element.find_elements(By.TAG_NAME, "span")
        time.sleep(1)
        excluded_links = ["https://onepiece.fandom.com/wiki/Vegapunk", "https://onepiece.fandom.com/wiki/Caesar_Clown",
                          "https://onepiece.fandom.com/wiki/MADS"]
        href_list = [span.find_element(By.CSS_SELECTOR, "div > a").get_attribute("href") for span in span_elements if
                     span.find_element(By.CSS_SELECTOR, "div > a").get_attribute("href") not in excluded_links]
        return href_list

    def get_fruit_info(self, array):
        href_list = array
        for link in href_list:
            self.driver.get(link)
            time.sleep(1)
            self.driver.maximize_window()
            time.sleep(1)
            primary_anchor_tag = self.driver.find_element(
                By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[2]/div[1]/div[1]/div/a[1]").text
            secondary_anchor_tag = self.driver.find_element(
                By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[2]/div[1]/div[1]/div/a[2]").text
            if "Non-Canon" in primary_anchor_tag or "Non-Canon" in secondary_anchor_tag:
                continue
            try:
                fruit_name = self.driver.find_element(
                    By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[3]"
                              "/div[2]/div/aside/section/div[2]/div").text.split("\n")[0]
            except selenium.common.exceptions.NoSuchElementException:
                fruit_name = self.driver.find_element(
                    By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[3]"
                              "/div[2]/div/aside/section/div[3]/div").text.split("\n")[0]
            if "(" in fruit_name:
                fruit_name = fruit_name.split("(")[0]
            elif "[" in fruit_name:
                fruit_name = fruit_name.split("[")[0]

            try:
                current_user = self.driver.find_element(
                    By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[3]"
                              "/div[2]/div/aside/section/div[8]/div").text.split("[")[0]
            except selenium.common.exceptions.NoSuchElementException:
                current_user = self.driver.find_element(
                    By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[3]"
                              "/div[2]/div/aside/section/div[7]/div").text.split("[")[0]

            fruit_type_elem = self.driver.find_element(
                By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/aside/section/div[6]/div")
            for fruit_type in fruit_type_elem.find_elements(By.CSS_SELECTOR, "div > a"):
                if "Chapter" in fruit_type.text:
                    fruit_type_elem = self.driver.find_element(
                        By.XPATH, "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div/aside/section/div[7]/div")

            types = [fruit_type.text for fruit_type in fruit_type_elem.find_elements(By.CSS_SELECTOR, "div > a")]

            if len(types) > 1:
                fruit_type = ", ".join(types)
                self.fruits_dict = {"fruit_name": fruit_name, "current_user": current_user, "type": fruit_type}
                self.fruits.append(self.fruits_dict)
            else:
                self.fruits_dict = {"fruit_name": fruit_name, "current_user": current_user, "type": types[0]}
                self.fruits.append(self.fruits_dict)
        self.driver.quit()
        return self.fruits
