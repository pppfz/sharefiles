import requests
import json

url = "https://332ea060-0eaf-41e3-b423-0ec826a40211-00-3p2h9q7cxnyr.picard.replit.dev/submit"

# 定义要发送的JSON数据
data = {
    "status_code": 200,
    "message": "succeed",
    "data": {
        "trade_id": "202203271648380592218340",
        "order_id": "9",
        "amount": 53,
        "actual_amount": 7.9104,
        "token": "TNEns8t9jbWENbStkQdVQtHMGpbsYsQjZK",
        "expiration_time": 1648381192,
        "payment_url": "http://example.com/pay/checkout-counter/20220327164838059221834"
    },
    "request_id": "b1344d70-ff19-4543-b601-37abfb3b3686"
}

# 定义请求头
headers = {
    "Content-Type": "application/json"
}

# 发送POST请求，包含请求头
response = requests.post(url, json=data, headers=headers)
# response = requests.get(url)

# 打印响应结果
print(response.text)
