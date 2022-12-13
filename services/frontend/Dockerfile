FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm init vue@latest

COPY package.json .
COPY package-lock.json .
RUN npm install

EXPOSE 8080
CMD ["npm", "run", "dev"]

