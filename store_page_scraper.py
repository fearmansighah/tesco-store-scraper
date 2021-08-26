import re
import csv
import urllib.request
import re


def extractMapsLink(pageSource):

    pattern = r'https://goo.gl/maps/' + r'\w+'

    foundMapsLink = re.findall(pattern, pageSource)
    return foundMapsLink


def accessStoreLink(url):

    store_page = urllib.request.urlopen(url)
    page_source = store_page.read()

    return str(page_source)


def extractURLs(pageSource, csvwriter):

    pattern = r'/Tesco-MY/Store-Locator/' + \
        r'[\w|-]+' + r'/StoreLocatorDetails'
    pattern_list = re.findall(pattern, pageSource)
    pattern_list.sort()
    original_length = len(pattern_list)
    url_list = ['https://www.tesco.com.my/'] * original_length

    print(original_length)
    for i in range(original_length):

        url_list[i] += pattern_list[i]
        print(url_list[i])

        storePageSource = accessStoreLink(url_list[i])
        googleMapsLink = extractMapsLink(storePageSource)
        print(googleMapsLink)

        csvwriter.writerow([url_list[i], googleMapsLink])

    return url_list


def main():

    f = open('storeLocator_pageSource.txt', 'r')
    pageSource = f.read()

    csvfile = open("store_links.csv", "w", newline="")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['URL Link', 'GMaps Link'])

    urls = extractURLs(pageSource, csvwriter)

    # close file
    # f.close()


if __name__ == "__main__":
    main()
