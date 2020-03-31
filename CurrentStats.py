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
    for tr in soup.find_all("tbody")[1].find_all("tr"):
        myDataStr += tr.get_text()

    myDataStr = myDataStr[1:]
    itemList = myDataStr.split("\n")

    # print(itemList)
    tempList = int(itemList[-11].strip('#')
                   ), int(itemList[-8].strip('#')), int(itemList[-5].strip('#'))
    print(tempList)

    # return tempList


def StateStatus(state):
    everything = []
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
    # print(itemList)
    count = 0
    for item in itemList[0:54]:

        dataList = item.split("\n")

        if count == 1:
            # print(dataList[0], dataList[1])
            everything.append(dataList[0])
            everything.append(dataList[1])
            count = 0

        if dataList[1] == state:
            # everything.append(dataList[1])
            everything.append(dataList[2])
            count = 1

    # print(everything)

    return everything


if __name__ == '__main__':
    currentStatus()
    # StateStatus("Maharashtra")
    pass
