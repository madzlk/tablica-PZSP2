FROM node:21.6.1-alpine

COPY package*.json /app/

COPY . /app/

WORKDIR /app

RUN npm install

CMD ["npm", "run", "dev"]