FROM node:lts-alpine

RUN npm install -g http-server

RUN apk update && apk add git

RUN git clone https://github.com/d2emon/flask-blog.git

WORKDIR /flask-blog/front

RUN npm install

EXPOSE 8080

# RUN npm run build

# CMD ["http-server", "dist"]

CMD ["npm", "run", "serve"]
