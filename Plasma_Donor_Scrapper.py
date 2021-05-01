from selenium import webdriver
import csv
import time


def scrapper():
    driver = webdriver.Firefox()
    driver.get("https://coronaclusters.in/plasma/donors")
    time.sleep(60)
    fields = ['verified', 'location', 'donor', 'blood_group', 'phone_number', 'date_of_negative', 'date_of_positive',
              'registered_on']
    dict_data = []
    pages = len(driver.find_elements_by_css_selector(".page-item")) - 2

    for page in range(1,pages):
        next_page = driver.find_element_by_xpath("//a[@aria-label='Next »']")
        count = len(driver.find_elements_by_xpath("//tbody/tr"))
        for i in range(1, count + 1):
            elementList = driver.find_elements_by_xpath("//tbody/tr[%d]/td[1]/img" % i)
            if len(elementList) == 0:
                verified = ""
            else:
                verified = "Verified"
            location = driver.find_element_by_xpath("//tbody/tr[%d]/td[2]" % i).text
            donor = driver.find_element_by_xpath("//tbody/tr[%d]/td[3]" % i).text
            blood_group = driver.find_element_by_xpath("//tbody/tr[%d]/td[4]" % i).text
            phone_number = driver.find_element_by_xpath("//tbody/tr[%d]/td[5]" % i).text
            date_of_negative = driver.find_element_by_xpath("//tbody/tr[%d]/td[6]" % i).text
            date_of_positive = driver.find_element_by_xpath("//tbody/tr[%d]/td[7]" % i).text
            registered_on = driver.find_element_by_xpath("//tbody/tr[%d]/td[8]" % i).text
            dict_data.append([verified, location, donor, blood_group, phone_number, date_of_negative, date_of_positive,
                              registered_on])
        next_page.click()


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

scrapper()