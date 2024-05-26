FROM node:21.6.1-alpine

WORKDIR /app

COPY package.json ./

COPY package-lock.json ./

RUN npm install -g npm@latest

RUN npm ci --silent

RUN npm install react-scripts@3.4.1 -g --silent

COPY . /app/

CMD ["npm", "run", "dev"]
