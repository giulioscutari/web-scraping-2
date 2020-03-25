from webbot import Browser
from bs4 import BeautifulSoup
import requests
import time
import csv

# credentials: they are not real credentials as this code is to be published.
username = "thisUsernameWontWork"
password = "thisPasswordWontWork"
# log into admin page
web = Browser()
web.go_to('https://www.zumostraining.co.uk/Login.aspx')
web.type(username)
web.click(id='ContentPlaceHolder1_txtPassword')
web.type(password)
web.press(web.Key.ENTER)
# class="btn btn-primary btn-block top-margin-sm text-left"
# navigate to titles page, create soup and select values
web.go_to('https://www.zumostraining.co.uk/Zumos_Admin/Titles.aspx')
soup = BeautifulSoup(web.get_page_source(),'lxml')
values = soup.find_all('input', {'class' : 'btn btn-primary btn-block top-margin-sm text-left'})

# print(values) # test - success
links = ['nothing'] * len(values)
i = 0
print("beginning the loop into every button...")
for value in values: # loops into every button    
    web.click(id=value['id'])
    time.sleep(1) # this is needed to make the browser get on the new page before getting the source. It would be a nice improvement to have it done as a webbot function, but I can't find that.
    rawpage = web.get_page_source()
    # print(rawpage)
    titlePage = BeautifulSoup(rawpage,'lxml')
    # print(titlePage)
    iframe = titlePage.find(id='ContentPlaceHolder1_vidYoutube')
    # print("printing 'iframe':")
    # print(iframe)
    # print("printing source:")
    # print(iframe['src'])
    links[i] = iframe['src']
    print(links[i])
    i += 1 
    web.go_to("https://www.zumostraining.co.uk/Zumos_Admin/Titles.aspx")
print("end of loop, writing CSV file...")


with open('titles.csv','w') as outputFile:
    writer = csv.writer(outputFile)
    writer.writerow(links)