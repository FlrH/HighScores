from django.test import TestCase


import requests

def scores():
    url='http://127.0.0.1:8000/api/scores/'
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',        
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept':'Application/json'
    }
    for i in range(100):
        data = "uid=dlh_{}&scores=10000{}".format(i,i)
        response=requests.post(url=url,data=data,headers=headers)
        # response=requests.get(url=url,params=data,headers=headers)
        print(response.json())
        print(response.status_code)


def _sort():
    url='http://127.0.0.1:8000/api/sort/'
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',        
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept':'Application/json'
    }
    data = "uid=dlh_92&start=112&end=21"
    response=requests.post(url=url,data=data,headers=headers)
    # response=requests.get(url=url,headers=headers)
    print(response.json())
    print(response.status_code)


if __name__ == '__main__':
    # post_scores()
    _sort()
