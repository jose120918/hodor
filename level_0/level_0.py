#!/usr/bin/python3
import requests
import multiprocessing
""" Web scraping: Program that votes 1024 times """

url = 'http://158.69.76.135/level0.php'
my_id = '1850'
params = {'id': my_id, 'holdthedoor': 'Submit'}
vote_success = 'Hold the Door challenge - Level 0'
r = requests.get(url)

vote = 1
while vote <= 1024:
    try:
        r = requests.post(url, data=params)
        if r.status_code is 200 and vote_success in r.text:
            print("Upload vote #{}".format(vote), end='\r', flush=True)
            vote += 1
    except Exception as error:
        print(error)
print(":)")
