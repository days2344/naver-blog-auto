import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 네이버 블로그 API 설정
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_BLOG_ID = os.getenv("NAVER_BLOG_ID")

NAVER_BLOG_API_URL = "https://openapi.naver.com/blog/writePost.json"

@app.route("/", methods=["POST"])
def post_to_naver():
    """
    네이버 블로그에 글을 자동으로 게시하는 API
    """
    try:
        data = request.json  # 요청으로부터 JSON 데이터 가져오기
        title = data.get("title", "제목 없음")
        content = data.get("content", "내용 없음")

        headers = {
            "X-Naver-Client-Id": NAVER_CLIENT_ID,
            "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "title": title,
            "contents": content,
            "blogId": NAVER_BLOG_ID
        }

        response = requests.post(NAVER_BLOG_API_URL, headers=headers, data=payload)
        response_data = response.json()

        if response.status_code == 200:
            return jsonify({"message": "네이버 블로그 포스팅 성공!", "response": response_data})
        else:
            return jsonify({"message": "네이버 블로그 포스팅 실패!", "error": response_data}), 400

    except Exception as e:
        return jsonify({"message": "서버 오류 발생!", "error": str(e)}), 500

# Vercel에서 실행하기 위한 핸들러 (Flask → Serverless 환경 지원)
def handler(event, context):
    return app(event, context)
