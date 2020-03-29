# This Program gives Current stats of conoravirus cases and death by fetching it from government website

import requests
from bs4 import BeautifulSoup
import time


def getData(url):
    r = requests.get(url)  # gives the html data
    return r.text  # returns in text format


def currentStatus():
    myHtmlData = getData("https://www.mohfw.gov.in/")

#     print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, "html.parser")
#     print(soup.prettify())

    # gets only the table from whole html page
    myDataStr = ""
    for tr in soup.find_all("tbody")[9].find_all("tr"):
        myDataStr += tr.get_text()

    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n")

    print(itemList)
    tempList = int(itemList[-9].strip('#')
                   ), int(itemList[-6].strip('#')), int(itemList[-3].strip('#'))
    print(tempList)

    return tempList


def StateStatus(state):
    myHtmlData = getData("https://www.mohfw.gov.in/")

#     print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, "html.parser")
#     print(soup.prettify())

    # gets only the table from whole html page
    myDataStr = ""
    for tr in soup.find_all("tbody")[9].find_all("tr"):
        myDataStr += tr.get_text()

    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n\n")
    for item in itemList[0:23]:
        dataList = item.split("\n")
        if dataList[1] == state:
            Cases = int(dataList[2]) + int(dataList[3])
            everything = [Cases, dataList[4], dataList[5]]
            # print(everything)
            # time.sleep(2)
    return everything


if __name__ == '__main__':
    # currentStatus()
    # StateStatus("Maharashtra")
    pass
