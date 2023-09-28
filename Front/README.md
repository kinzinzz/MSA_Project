# CMD

- npx create-react-app 프로젝트명 --template typescripts
- 프로젝트 폴더안에서 npm start(http://localhost:3000/)
- stdin 설정
- docker-compose down -v
- window의 경우 environment: - CHOKIDAR_USEPOLLING=true

# Errors
- The href attribute requires a valid value to be accessible
  =><a href="#!">test</a> <a href="{() => false}">test</a>
      