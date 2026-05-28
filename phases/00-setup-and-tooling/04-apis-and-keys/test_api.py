fake_response = {
    "model": "claude-sonnet",
    "usage": {
        "input_tokens": 12,
        "output_tokens": 20
    },
    "content": [
        {
            "text": "A neural network is a mathematical system that learns patterns from data."
        }
    ]
}

print("Model:", fake_response["model"])
print("Input Tokens:", fake_response["usage"]["input_tokens"])
print("Output:", fake_response["content"][0]["text"])