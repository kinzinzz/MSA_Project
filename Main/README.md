## Flask CMD

python manager.py db_init

default app name = app.py

# 중복 생성된 이미지 삭제
docker rmi $(docker images -f "dangling=true" -q)

# dockerfile 변경된 내용 compose 실행
docker compose up --build