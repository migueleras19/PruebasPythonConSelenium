from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(executable_path=r"/media/qacore/data/drivers/chromedriver")
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://python.org')
driver.save_screenshot("screenshot.png")

driver.close()
