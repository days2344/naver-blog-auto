from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["POST"])
def post_to_naver():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Naver API로 데이터 전송 (예제)
    naver_api_url = "https://api.naver.com/your-endpoint"
    headers = {"Authorization": f"Bearer {data.get('token')}"}
    response = requests.post(naver_api_url, json=data, headers=headers)

    return jsonify(response.json())

# Vercel은 `app` 변수를 자동으로 인식함
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
