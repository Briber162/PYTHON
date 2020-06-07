from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

class find_jobs:
    #job_title = input("Enter job title : ")
    #job_location = input("Enter Location : ")
    driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\KUNAL\\PYTHON\\chromedriver.exe")
    driver.maximize_window()
    #dataframe = pd.DataFrame(columns=["Title", "Location", "Comapny", "Salary", "Sponsered", "Description"])
    def find_url(self,job_title,job_location):
        url = "https://www.indeed.co.in/"
        link = url + 'jobs?q=' + job_title + '&l=' + job_location
        driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\KUNAL\\PYTHON\\chromedriver.exe")
        driver.get(link)
        all_jobs = driver.find_elements_by_class_name('result')
        dataframe = pd.DataFrame(columns=["Title", "Location", "Comapny", "Salary", "Sponsered", "Description"])
        for job in all_jobs:
            result_html = job.get_attribute('innerHTML')
            soup = BeautifulSoup(result_html,'html.parser')
            try:
                title = soup.find("a",class_="jobtitle turnstileLink").text.replace('\n','')
            except:
                title = 'None'
            try:
                location = soup.find(class_="location accessible-contrast-color-location").text
            except:
                location = 'None'
            try:
                company = soup.find(class_="company").text.replace("\n","").strip()
            except:
                company = 'None'
            try:
                salary = soup.find(class_="salary").text.replace("\n","").strip()
            except:
                salary = 'None'
            try:
                sponsered = soup.find(class_="sponseredGray").text
                sponsered = "Sponsered"
            except:
                sponsered = 'Organic'

            sum_div = job.find_elements_by_class_name("summary")[0]
    #try:
            sum_div.click()
            driver.implicitly_wait(100)    
            job_desc = driver.find_element_by_id("vjs-desc").text
    
            dataframe = dataframe.append({'Title':title, 'Location':location,'Company':company,'Salary':salary,'Sponsered':sponsered,'Description':job_desc},ignore_index=True)
            dataframe.to_csv("C:\\Users\\User\\Desktop\\KUNAL\\PYTHON\\ASSIGNMENT 2\\datascience.csv",index=False)
