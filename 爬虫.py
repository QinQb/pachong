import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.example.com')
#请求网页信息
print(res.status_code)
#检查请求是否成功
string = res.text
#将数据转换为字符串格式
soup = BeautifulSoup(string,'html.parser')
#解析数据至可读懂格式
data = soup.find('div')
#提取首个<div>元素，并命名为变量data
print(data)