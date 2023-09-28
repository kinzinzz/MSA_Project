FROM node:alpine
WORKDIR /app
COPY package.json .
ENV NODE_PATH=/install/node_modules
COPY . .
EXPOSE 3000
CMD [ "npm","install","start" ]