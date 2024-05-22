FROM node:21.6.1-alpine

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./

RUN npm ci --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY . /app/

EXPOSE 4173

# Command to run your application
CMD ["npm", "run", "dev"]
