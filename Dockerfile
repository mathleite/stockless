FROM node:slim as dev

RUN apt update && apt install -y openssl procps iputils-ping

RUN npm i -g @nestjs/cli

USER node
