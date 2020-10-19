FROM node:12-alpine
WORKDIR /.vscode
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]