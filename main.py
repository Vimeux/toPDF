
import base64
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
# options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


# generate pdf from url
def generate_pdf(url: str, filename: str):
    # open html in browser
    driver.get(url)

    # wait for page to load
    time.sleep(3)

    # get pdf data
    pdf = driver.execute_cdp_cmd("Page.printToPDF", {"landscape": True, "printBackground": True, "preferCSSPageSize": True})

    # save pdf to file
    with open(filename, "wb") as file:
        file.write(base64.b64decode(pdf["data"]))

    # close browser
    driver.quit()


generate_pdf("https://ut.no/", "google.pdf")


