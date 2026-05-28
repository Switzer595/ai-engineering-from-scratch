import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()

url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['DASHSCOPE_API_KEY']}",
}

body = json.dumps({
    "model": "qwen-plus",
    "messages": [
        {
            "role": "user",
            "content": "用一句话解释什么是神经网络。"
        }
    ]
}).encode("utf-8")

req = urllib.request.Request(
    url,
    data=body,
    headers=headers,
    method="POST"
)

with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read().decode("utf-8"))
    print(result["choices"][0]["message"]["content"])