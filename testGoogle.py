from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():
    
    driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")

    driver.get("https://google.com")

    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    value = search_box.get_attribute("value")
    assert value == "Selenium"

    driver.quit()