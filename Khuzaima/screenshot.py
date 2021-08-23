import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')

driverPath = "..\\chromedriver_win32\\chromedriver.exe"

# url = 'https://www.reddit.com/'
url = input("Please enter the URL: ")

print("opening the browser")
driver = webdriver.Chrome(options=chrome_options, executable_path=driverPath)

try:
    driver.implicitly_wait(100)
    print("opening the url")
    driver.get(url)
    # driver.get_screenshot_as_file('reddit_1.png')

    print('executing the script')
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    print(S)
    height = S('Height')
    print(height)
    print(type(S('Height')))

    width = S('Width')
    print(width)
    print(type(S('Width')))

    print("height is " + str(height))
    driver.set_window_size(width, height)

    
    result = url.lstrip('https://')
    result = result.lstrip('http://')
    resutl = result.rstrip('/')
    result = result.replace('/', '_')
    results = result.split('.')
    for result in results:
        result = re.findall(r"(?i)\b[0-9A-Za-z]+\b", result)
    result = ".".join(results)

    print("saving the screenshot")
    driver.save_screenshot(f'{result}.png')
    '''body = driver.find_element_by_tag_name('body')
    print(body.size)
    body.screenshot("bodyss.png")
    '''
    
    print("screenshot saved")

finally:
    print("quitting the browser")
    driver.quit()
    print("All done. ")


# def test_fullpage_screenshot():
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--start-maximized')
#
#     print("opening browser")
#
#     driver = webdriver.Chrome(options=chrome_options)
#
#     print("opening url")
#     driver.get("https://www.reddit.com/")
#
#     print("opened url...")
#     time.sleep(2)
#
#     #ele = driver.find_element("xpath", '//div[@class="react-grid-layout layout"]')
#
#
#     # S = lambda X: driver.execute('return document.body.parentMode.scroll' + X)
#     # driver.set_window_size(S('Width'), S('Height'))
#
#     driver.find_element_by_tag_name('body').screenshot("screenshotlast.png")
#
#     # the element with longest height on page
#     '''# ele = driver.find_element("xpath", '//div[@class="react-grid-layout layout"]')
#     # ele = driver.find_element_by_tag_name("body")
#     # print(ele.size["Height"])
#
#     # total_height = ele.size["height"] + 10000
#
#     # print(total_height)
#
#     # driver.set_window_size(1920, total_height)  # the trick'''
#     print('wait...')
#     time.sleep(2)
#     driver.save_screenshot("screenshot1.png")
#     driver.quit()
#
#
# if __name__ == "__main__":
#     test_fullpage_screenshot()