import requests

requesturl = 'http://v.juhe.cn/weather/index'#访问api

cityname = input('输入你要查询的城市天气：')
data = {  #设置参数
    'key': '88038881cca75f0888becb02fa5ef045',
    'cityname': cityname,
    'dtype':'json',
    'format':1,
}
html = requests.get(requesturl,data) #访问api并传入参数
response = html.json()
temperature = response['result']['today']['temperature']
weather = response['result']['today']['weather']
wind_direction = response['result']['today']['wind']
date_y = response['result']['today']['date_y']
dressing_index = response['result']['today']['dressing_index']
print('温度：'+ temperature)
print('天气：'+weather)
print('风向：'+wind_direction)
print('日期：'+ date_y)
print('体感温度：'+dressing_index)