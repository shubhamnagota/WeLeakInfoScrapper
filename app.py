import os
import sys
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.chrome.service as service

service = service.Service(os.path.abspath('chromedriver'))
service.start()

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

url = 'https://search.weleakinfo.com/'
search_box_xpath = '//*[@id="main"]/section[2]/div[2]/div[2]/div/form/div/div[2]/input'
search_type_xpath = '//*[@id="main"]/section[2]/div[2]/div[3]/div/button'
results_text_xpath = '//*[@id="results"]/div/div/div/h1'
error_xpath = '//*[@id="results"]/div/div/div[2]/div/p'
search_type_options_xpath = {
    'username': 0,
    'email': 1,
    'password': 2,
    'hash': 3,
    'ip': 4,
    'name': 5,
    'phone': 6
}
finalResultsForXLS = []
wb = Workbook()
sheet = wb.active

driver = webdriver.Remote(
    service.service_url,   desired_capabilities=chrome_options.to_capabilities())
driver.implicitly_wait(10)
driver.get(url)


def searchAndGetData(searchTerm, searchType):
    global finalResultsForXLS
    print(f"\nSearch Term : {searchTerm} ---> Type : {searchType}")
    search_type_button = driver.find_elements_by_xpath(
        search_type_xpath)[search_type_options_xpath[searchType.lower()]]
    search_type_button.click()

    search_box = driver.find_element_by_xpath(search_box_xpath)
    search_box.send_keys(searchTerm)
    search_box.submit()

    try:
        resultsText = driver.find_element_by_xpath(results_text_xpath).text
        print('Results : ', resultsText)
        data = [searchTerm, searchType, resultsText]
    except:
        error_check = driver.find_element_by_xpath(error_xpath).text
        print(f"Error in searching : {searchTerm} ---> {error_check}")
    finally:
        finalResultsForXLS.append(data)
        driver.back()


with open('input.txt') as fr:
    inputsArray = fr.readlines()
    for inp in inputsArray:
        inputArray = inp.split()
        searchAndGetData(inputArray[0], inputArray[1])

for index, data in enumerate(finalResultsForXLS):
    for i in range(3):
        sheet.cell(index+1, i+1).value = data[i]

wb.save('output.xlsx')

driver.quit()
