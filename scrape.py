import csv
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path="./chromedriver", options=options)

urls = (
    "https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops",
    "https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets",
    "https://webscraper.io/test-sites/e-commerce/scroll/phones/touch",
)

products_list = []

for resource in urls:

    driver.get(resource)
    last_id_on_page = json.loads(
        driver.find_element(
            By.CSS_SELECTOR, ".row.ecomerce-items.ecomerce-items-scroll"
        ).get_attribute("data-items")
    ).pop()["id"]

    while True:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        len_ = len(
            driver.find_elements(By.XPATH, f"//a[contains(@href, '{last_id_on_page}')]")
        )
        if len_ > 0:
            break

    subcat_items = driver.find_elements(By.CLASS_NAME, "caption")
    for item in subcat_items:
        price = item.find_element(By.XPATH, ".//*[contains(@class, 'price')]").text
        description = item.find_element(By.CLASS_NAME, "description").text
        title = item.find_element(By.CLASS_NAME, "title").get_attribute("title")
        url = item.find_element(By.CLASS_NAME, "title").get_attribute("href")
        prod_id = url.split("/").pop()

        prod_attrs = (prod_id, url, title, description, price)
        products_list.append(prod_attrs)


with open("products.csv", "w", newline="") as csv_f:
    writer = csv.writer(csv_f)
    writer.writerow(["Product ID", "URL", "Title", "Description", "Price"])
    writer.writerows(products_list)


driver.quit()
