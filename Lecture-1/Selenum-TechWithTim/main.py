from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_webdriver_path = "D:\Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
driver.get("https://www.techwithtim.net/")

search = driver.find_element_by_name("s")
search.send_keys("django")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = driver.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
except:
    driver.quit()
