import urllib.parse
import http.client
import json


def get_access_token():
    test_data = {'appKey': '4bff5395057145bcab2c490a6c0ca101', 'appSecret': '274718445440b42cda760d1fc146faec'}
    test_data_url_encode = urllib.parse.urlencode(test_data)
    request_url = "https://open.ys7.com/api/lapp/token/get"
    conn = http.client.HTTPConnection('open.ys7.com')
    header = {"Content-type": "application/x-www-form-urlencoded"}
    conn.request(method="POST", url=request_url, headers=header, body=test_data_url_encode)
    response = conn.getresponse()
    res = response.read()
    resp = json.loads(res)
    return resp['data']['accessToken']

