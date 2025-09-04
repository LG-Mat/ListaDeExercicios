import csv
import requests

CSV_URL = "https://raw.githubusercontent.com/emmendorfer/idwr/main/demo/datasets/amazon.csv"

def ler_url(CSV_URL):
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        reader = csv.reader(decoded_content.splitlines(), delimiter=',')
        mylist = list(reader)
        for row in mylist:
            print(row)

ler_url(CSV_URL)