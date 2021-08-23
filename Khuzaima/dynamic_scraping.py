import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


print("starting...")

url = "https://www.daraz.pk/laptops/?spm=a2a0e.home.cate_1.5.6a274937VstcSP"

opts = Options()
opts.add_argument("--headless")
opts.headless = True

driverPath = "E:\\mk\\PythonLearning\\chromedriver_win32\\chromedriver.exe"

print("opening the browser...")
driver = webdriver.Chrome(options=opts, executable_path=driverPath)
print("opening the url...")
driver.get(url)



print("parsing...")
soup = BeautifulSoup(driver.page_source, "html.parser")
soup = soup.find("div", "c1_t2i")
# print(soup.prettify())


print("finding...")
itemDetails = soup.find_all("div", "c3KeDq")
print("\n\n\n\n")

print(len(itemDetails))

names = []
prices = []

for item in itemDetails:
    price = item.find("span", class_="c13VH6").text
    # price = item.find("span", class_="c13VH6").get_text(strip=True, separator=' ')
    prices.append(price)
    # print(price.strip().ljust(15), end="")

    name = item.find("div", class_="c16H9d").text
    names.append(name)
    # print(name.strip(), end="")
    # print()

data = {"Prices": prices, "Names": names}
# print(type(data))   # dict
df = pd.DataFrame(data)
df.to_csv("daraz.csv", index=False)
df.to_html("daraz.html")

print(df)
# print(df.head())
# print(df.tail())

# print("saving screen shot")
#
# driver.save_screenshot("ss.png")
# print("screenshot saved")
#
# driver.get_screenshot_as_file("2.png")
# driver.find_element_by_tag_name('body').screenshot("fullpage.png")
# print("Full page ss saved successfully")
driver.quit()
