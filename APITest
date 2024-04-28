import requests

#测试接口调用

# 获取所有功能列表接口
response = requests.get('http://127.0.0.1:5001/functions')
print("Function List:")
print(response.json())

# 调用具体功能接口，例如中译英
data = {
    "text": "你好，这是一个测试。"
}
response = requests.post('http://127.0.0.1:5001/translate_to_english', json=data)
print("\nTranslation to English:")
print(response.json())
