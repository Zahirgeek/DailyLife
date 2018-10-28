import requests

# 用户注册

url = "http://127.0.0.1:5000/user/blogusers/"

querystring = {"action":"register"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nZahir\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n120\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n525\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "0ce7b50c-f231-1184-9162-a9d978ce2768"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

##################################################

# 用户登录

import requests

url = "http://127.0.0.1:5000/user/blogusers/"

querystring = {"action":"login"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nZahir\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n525\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "4254897b-d2b1-0c07-727d-3addddccd769"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

##################################################

# 用户信息修改
# 必须指定修改用户的密码

import requests

url = "http://127.0.0.1:5000/user/userpatch/"

querystring = {"token":"blog_user25ffd15aef75470fac0544642123e5f6"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nAlex\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n2321\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n11\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "221f485d-01bb-29d9-5991-e5284237d602"
    }

response = requests.request("PATCH", url, data=payload, headers=headers, params=querystring)

print(response.text)

##################################################

# 用户逻辑删除
# 用户必须是管理员(permission=True)

数据库中的管理员 
username = Zahir
password = 525

import requests

url = "http://127.0.0.1:5000/user/userdelete/2/"

querystring = {"token":"blog_userf5aaad0f94e94a608496c846e0c848c4"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "d657e0ae-03f6-c453-7c7d-41af076487c5"
    }

response = requests.request("DELETE", url, headers=headers, params=querystring)

print(response.text)

##################################################

# 创建博客

import requests

url = "http://127.0.0.1:5000/blog/createblog/"

querystring = {"token":"blog_user9a841d0577884a85bb6b1efc97507e2a"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n我的第一个博客\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\nHello World!\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "bd672adb-fa8c-1785-b671-72922a435c18"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)


##################################################

# 修改博客

# 超级管理员修改
import requests

url = "http://127.0.0.1:5000/blog/patchblog/1/"

querystring = {"token":"blog_user5d2eef71517e4950a7871b2dbc299df5"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n我的第三个博客\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\nHello \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "11ca7bff-8733-89f1-cce2-038793bb1b73"
    }

response = requests.request("PATCH", url, data=payload, headers=headers, params=querystring)

print(response.text)

# 博客创建者修改

import requests

url = "http://127.0.0.1:5000/blog/patchblog/1/"

querystring = {"token":"blog_user0b2dd98ef05a4c5fbeea4d76ddf3f768"}

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n我的第三个博客\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\nHello \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "f8f941cc-dca8-7b86-20df-4cd1c6db2fe7"
    }

response = requests.request("PATCH", url, data=payload, headers=headers, params=querystring)

print(response.text)

##################################################
# 删除博客

import requests

url = "http://127.0.0.1:5000/blog/deleteblog/1/"

querystring = {"token":"blog_user12d8bc0a4bf349eb8a52e8d8aae33f36"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "ad1bbd6e-b75b-78cc-e6f7-55d8eb9afed8"
    }

response = requests.request("DELETE", url, headers=headers, params=querystring)

print(response.text)

##################################################

# 收藏博客

import requests

url = "http://127.0.0.1:5000/user/createheart/2/"

querystring = {"token":"blog_user12d8bc0a4bf349eb8a52e8d8aae33f36"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "99283c03-678a-562d-fe0d-1156f2f839ff"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

##################################################

# 获取某用户的所有收藏

import requests

url = "http://127.0.0.1:5000/user/gethearts/1/"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "3cdf7cc7-c4be-b9d9-82ef-599d303b74ff"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

##################################################
# 获取收藏某博客的所有用户

import requests

url = "http://127.0.0.1:5000/user/getheartusers/1/"

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "687c00e2-968d-2458-247b-faaaa20a4af4"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
