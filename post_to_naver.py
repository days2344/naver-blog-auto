import requests

# 네이버 블로그 API 설정
CLIENT_ID = "YOUR_NAVER_CLIENT_ID"
CLIENT_SECRET = "YOUR_NAVER_CLIENT_SECRET"
BLOG_ID = "YOUR_NAVER_BLOG_ID"

def post_to_naver(title, content):
    """
    네이버 블로그에 게시글을 자동으로 올리는 함수
    """
    api_url = f"https://openapi.naver.com/blog/writePost.json"
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
        "Content-Type": "application/json",
    }
    data = {
        "title": title,
        "content": content,
        "blogId": BLOG_ID
    }

    response = requests.post(api_url, json=data, headers=headers)
    return response.json()

# 테스트용 실행 코드
if __name__ == "__main__":
    test_title = "테스트 제목"
    test_content = "이것은 자동화된 블로그 포스트입니다."
    result = post_to_naver(test_title, test_content)
    print(result)
