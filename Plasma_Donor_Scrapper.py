from selenium import webdriver
import csv
import time

driver = webdriver.Firefox()
driver.get("https://coronaclusters.in/plasma/donors?state=2168&page=3")
# time.sleep(60 )
fields = ['verified','location','donor','blood_group','phone_number','date_of_negative','date_of_positive','registered_on']
count = len(driver.find_elements_by_xpath("//tbody/tr"))
dict_data = []

for i in range(1,count+1):
    elementList = driver.find_elements_by_xpath("//tbody/tr[%d]/td[1]/img" %i)
    if len(elementList) == 0:
        verified = ""
    else:
        verified = "Verified"
    location = driver.find_element_by_xpath("//tbody/tr[%d]/td[2]" %i).text
    donor = driver.find_element_by_xpath("//tbody/tr[%d]/td[3]" %i).text
    blood_group = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]" %i).text
    phone_number = driver.find_element_by_xpath("//tbody/tr[%d]/td[5]" %i).text
    date_of_negative = driver.find_element_by_xpath("//tbody/tr[%d]/td[6]" %i).text
    date_of_positive = driver.find_element_by_xpath("//tbody/tr[%d]/td[7]" %i).text
    registered_on = driver.find_element_by_xpath("//tbody/tr[%d]/td[8]" %i).text
    dict_data.append([verified,location,donor,blood_group,phone_number,date_of_negative,date_of_positive,registered_on])

print(dict_data)

filename = "plasmadonor3.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(dict_data)
driver.close()

