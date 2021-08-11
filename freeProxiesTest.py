import requests
import csv
import concurrent.futures

proxylist = []

with open('proxies.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        proxylist.append(row[0])

    print(len(proxylist))

def extract(proxy):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
        print(r.json(), '  -  working')
    except:
        pass
    return proxy

with concurrent.futures.ThreadPoolExecutor() as exec:
    exec.map(extract, proxylist)
