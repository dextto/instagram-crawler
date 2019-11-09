# 실행 방법
1. secret.py.dist 파일을 secret.py로 바꾸고 인스타 계정/비번을 입력
2. 적당한 hashtag로 검색
3. 메이크업 얼굴 사진 위주로 올리는 사람 계정명을 선택
4. 아래 명령어로 output.json에 결과를 받는다. -n 옵션을 크게 변경하자.
```
python crawler.py posts_full -u azncosmeticz -n 10 --fetch_likes_plays -o output.json 
```
5. output.json에 적혀있는 url과 like로 이미지를 다운로드 한다.
```
python download.py
```

# 파일명 형식
순서_좋아요개수