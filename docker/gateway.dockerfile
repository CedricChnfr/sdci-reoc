FROM node:alpine
WORKDIR /usr/src/app
COPY js/ ./

RUN npm install express
ENV VAR=""

CMD ["node", "test.js"]