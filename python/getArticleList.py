import requests

# 接口 URL
url = "https://api.juejin.cn/content_api/v1/article/query_list"

# 查询字符串参数 (Query String Parameters)
params = {
    "aid": "2608",
    "uuid": "7319706682807043594",
    "spider": "0"
}

# 请求体内容 (Request Payload)
data = {
    "user_id": "3998265375997175",
    "sort_type": 2,
    "cursor": "30"
}

# 发送 POST 请求
response = requests.post(url, params=params, json=data)

# 确保请求成功
if response.status_code == 200:
    # 解析 JSON 响应
    response_data = response.json()
    
    # 读取 data 属性
    if 'data' in response_data:
        data_list = response_data['data']
        
        # 循环遍历每一项并获取 article_id
        for item in data_list:
            article_id = item.get('article_id')  # 获取 article_id
            if article_id is not None:
                print(f"Article ID: {article_id}")
            else:
                print("article_id not found in this item.")
    else:
        print("No 'data' found in response.")
else:
    print("Request failed with status code:", response.status_code)
