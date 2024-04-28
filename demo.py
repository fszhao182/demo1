from flask import Flask, jsonify, request

app = Flask(__name__)

# 假设这是你的大模型翻译函数，这里用伪代码表示
def translate_to_english(text):
    # 调用大模型进行翻译
    translated_text = "This is a test"
    return translated_text

def translate_to_chinese(text):
    # 调用大模型进行翻译
    translated_text = "这是一个测试"
    return translated_text

def summarize_text(text):
    # 调用大模型进行文本总结
    summary = "总结结果如下：......"
    return summary

# 功能列表
FUNCTION_LIST = {
    "translate_to_english": "中译英",
    "translate_to_chinese": "英译中",
    "summarize_text": "总结"
}

# 获取所有功能列表接口
@app.route('/functions', methods=['GET'])
def get_functions():
    return jsonify(FUNCTION_LIST)

# 调用具体功能接口
@app.route('/<function_name>', methods=['POST'])
def call_function(function_name):
    if function_name not in FUNCTION_LIST:
        return jsonify({"error": "Function not found"}), 404

    # 从请求中获取数据
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing text data"}), 400

    text = data['text']

    # 调用对应的功能函数
    if function_name == 'translate_to_english':
        result = translate_to_english(text)
    elif function_name == 'translate_to_chinese':
        result = translate_to_chinese(text)
    elif function_name == 'summarize_text':
        result = summarize_text(text)
    else:
        return jsonify({"error": "Unknown function"}), 500

    # 返回结果
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
