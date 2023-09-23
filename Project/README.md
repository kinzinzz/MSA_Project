### CMD

docker-compose exec backend bash(또는 sh)

docker-compose exec "image이름" bash

source 경로/bin/activate bash 가상환경 활성화

postgres init => env POSTGRES_INITDB_ARGS="--auth-host=scram-sha-256" 또는 migrate.sh 작성할 것

환경변수 확인: python > import os > on.environ["변수명"]

alpine 가상환경 활성화 . venv/bin/activate