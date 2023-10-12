FROM node:slim as dev

RUN apt update && apt install -y openssl procps

RUN npm i -g @nestjs/cli \
    npm i @prisma/client

USER node
