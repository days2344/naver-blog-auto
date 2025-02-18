import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 네이버 블로그 API 설정
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_BLOG_ID = os.getenv("NAVER_BLOG_ID")

NAVER_BLOG_API_URL = "https://openapi.naver.com/blog/writePost.json"

# ✅ GET 요청이 들어오면 기본 메시지를 반환하도록 수정
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "네이버 블로그 자동 포스팅 API입니다."})

# ✅ 블로그 글 작성 (POST 요청만 허용)
@app.route("/", methods=["POST"])
def post_to_naver():
    try:
        data = request.json
        title = data.get("title", "제목 없음")
        content = data.get("content", "내용 없음")

        headers = {
            "X-Naver-Client-Id": NAVER_CLIENT_ID,
            "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {
            "blogId": NAVER_BLOG_ID
        }

        payload = {
            "title": title,
            "contents": content
        }

        response = requests.post(NAVER_BLOG_API_URL, headers=headers, params=params, data=payload)
        response_data = response.json()

        if response.status_code == 200:
            return jsonify({"message": "네이버 블로그 포스팅 성공!", "response": response_data})
        else:
            return jsonify({"message": "네이버 블로그 포스팅 실패!", "error": response_data}), 400

    except Exception as e:
        return jsonify({"message": "서버 오류 발생!", "error": str(e)}), 500

# ✅ Vercel에서 실행할 수 있도록 Flask 앱을 `app`으로 설정
if __name__ == "__main__":
    app.run()
