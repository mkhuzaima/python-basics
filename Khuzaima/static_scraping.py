import requests
from bs4 import BeautifulSoup

print("program is starting ")

print ("loading")
page = requests.get("https://realpython.github.io/fake-jobs/")

print("loaded")
# print(page.text)

print("parsing")
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.get_text())



print("finding")
results = soup.find(id = "ResultsContainer")


print(type(results))

# print(result)
# print(results.prettify())
job_elements = results.find_all("div", class_="card-content")
# job_elements = results.find("div", class_="card-content")

print(job_elements[0].prettify())
print('\n\n\n\n\n')


for job_element in job_elements:
    titleName = job_element.find("h2", class_= "title")
    location = job_element.find("p", class_ = "location")
    location = location.text.strip()
    date = job_element.find("time")

    print (titleName.text.ljust(50), end = "")
    print (location.ljust(30), end = "")
    print(date.text)
    #print("{}".titleName.text, location, sep = "--------", end="\n"*2)
