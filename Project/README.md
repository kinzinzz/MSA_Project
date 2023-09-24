### CMD

docker-compose exec backend bash(또는 sh)

docker-compose exec "image이름" bash

source 경로/bin/activate bash 가상환경 활성화

postgres init => env POSTGRES_INITDB_ARGS="--auth-host=scram-sha-256" 또는 migrate.sh 작성할 것

환경변수 확인: python > import os > on.environ["변수명"]

alpine 가상환경 활성화 . venv/bin/activate

migrations 초기화
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

dockerfile 변경내용 반영 안될 때
docker-compose up --build --force-recreate -d