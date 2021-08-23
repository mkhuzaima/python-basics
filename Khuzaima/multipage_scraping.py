from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

from random import randint
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url = 'https://www.daraz.pk/laptops/?page=1&spm=a2a0e.home.cate_1.5.6a274937VstcSP'
url = 'https://www.daraz.pk/smartphones/?spm=a2a0e.home.cate_1.1.35e34937tX3Jyv'
# url = 'https://www.cdn.geeksforgeeks.org/'

'''ua = UserAgent()

print(ua)
print()

# a = ua.chrome
# print(a)

user_agent = ua.chrome

print(user_agent)
'''

options = Options()
# options.add_argument("window-size=1400,600")
# options.headless = True
options.add_argument("Accept-Language=en-US,en;q=0.5")
# options.add_argument(f'user-agent = {user_agent}')


# hd = {
#     'user-agent': user_agent,
#     "Accept-Language": "en-US, en;q=0.5"
# }

print("opening the browser")
driverPath = "..\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=driverPath)

print('opening the url')
# driver.execute_script('alert("Hello 1")')
driver.get(url)
print("URL has opened successfully")

#
# print('alert is popping up')
# driver.execute_script('alert("Before clicking next button")')
# time.sleep(1)
#
# driver.switch_to.alert.accept
# driver.switch_to.alert.accept
# print('alert has been canceled')

print(driver.current_url)

# print("Finding the nextBtn")
# nextbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[3]/div/ul/li[9]/a')
nextbtn = driver.find_element_by_xpath('//li[@title="Next Page"]')
if 'ant-pagination-disabled' in nextbtn.get_attribute('class'):
    print('disabled button')
    nextbtn = None

'''
# checking whether the program gives exception on unfound elements
khuzaima = driver.find_elements_by_css_selector('.khuzaima')
print(type(khuzaima))
print(khuzaima)
print(not khuzaima)'''


# nextbtn = driver.find_element_by_class_name("nextpostslink")

# driver.implicitly_wait(100)
# print('executing the script')
# S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
# print(S)
# height = S('Height')
# print(height)
# print(type(S('Height')))
#
# width = S('Width')
# print(width)
# print(type(S('Width')))
#
# print("height is " + str(height))
# driver.set_window_size(width, height)

def pause():
    time = randint(2, 10)
    print(f'sleeping for {time} second(s)')
    sleep(time)
    print('sleeping time elapsed')


pause()


def scrollTo(element):
    desired_y = (element.size['height'] / 2) + element.location['y']
    current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script(
        'return window.pageYOffset')
    scroll_y_by = desired_y - current_y
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)


names = []
prices = []
n = 0
while nextbtn is not None:
    # driver.implicitly_wait(100)
    print('button is not none')


    '''try:
        while True:
            alert = driver.switch_to.alert
            print(alert.text)
            alert.dismiss()
            print("a popup is removed")
    except Exception:
        print(Exception.__class__)
        print("no alert found\n")
    
    print("sleeping for 2 seconds after removing popups")
    sleep(2)
    print('\n\n\n')
    '''


    # scraping a page

    print('---------------------------------------------------------')
    print(f'scraping "{driver.current_url}" .')

    print("parsing...")
    soup = BeautifulSoup(driver.page_source, "html.parser")

    soup = soup.find("div", "c1_t2i")
    # print(soup.prettify())

    print("finding...")
    itemDetails = soup.find_all("div", "c3KeDq")
    print("\n\n\n\n")

    print(len(itemDetails))


    for item in itemDetails:
        # price = item.find("span", class_="c13VH6").text.strip()
        price = item.find("span", class_="c13VH6").get_text(strip=True, separator=' ')
        prices.append(price)
        # print(price.strip().ljust(15), end="")

        name = item.find("div", class_="c16H9d").text.strip()
        names.append(name)
        # print(name.strip(), end="")
        # print()

        n= n+1
        print(n)

    #end of scraping page

    # issue = driver.find_element_by_class_name('lzd-logo-bar')

    print('waiting for presence of button')
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'li[title = "Next Page"]'))
        # EC.element_to_be_clickable(
        #     # (By.CSS_SELECTOR, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[3]/div/ul/li[9]/a')
        #     (By.CSS_SELECTOR, 'li[@title="Next Page"]')
        # )
    )
    print('button is present')

    # webElement = driver.findElement(By.cssSelector("div[class*="loadingWhiteBox"]"))
    # ((JavascriptExecutor) driver).executeScript("arguments[0].click();", webElement);

    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li .ant-pagination-next"))).click()


    # this scrolls until the element is in the middle of the page
    '''scrollTo(nextbtn)   # optional'''

    # print('pasted line has executed')

    nextbtn.click()
    print('clicked the next button')

    # print('button is clicked')


    '''lists = driver.find_element_by_class_name('cpF1IH')
    # soup = BeautifulSou(lists.text, "html.parser")
    print(type(lists))
    print(lists)
    print(lists.text)
    print('now buttons are going to print')
    for btn in lists.find_elements_by_css_selector('li.ant-pagination'):
        print(btn.get_attribute('title'))
    '''

    # nextbtn.submit()
    pause()
    # nextbtn = driver.find_element_by_css_selector('li.ant-pagination-next')

    nextbtn = driver.find_element_by_xpath('//li[@title="Next Page"]')

    area_disabled = type(nextbtn.get_attribute('aria-disabled'))
    classNames = nextbtn.get_attribute('class')

    if (area_disabled == 'true') or ('ant-pagination-disabled' in classNames):
        # print('disabled button')
        nextbtn = None
    # print(nextbtn.get_attribute('innerhtml'))
    # print(nextbtn)
    # print(len(nextbtn))

    # nextbtn = nextbtn[0] if len(nextbtn) > 0 else None


    # print('\n\n')
    # print(nextbtn)
    # print('Is None: '+ str(type(nextbtn)) + '\n\n')

    # nextbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[3]/div/ul/li[9]/a')
    # nextbtn = driver.find_element_by_class_name("nextpostslink")

    # print(nextbtn)
    print('\n----------------------------------------------\n')

print('button is none. Ended...')


print('saving data')

df = pd.DataFrame({"Prices": prices, "Names": names})

df.to_csv("CompleteDarazLaptopData.csv", index=False)
# df.to_html("daraz.html")
print('saved')


print('quitting the browser in 3 seconds')
sleep(3)
driver.quit()
