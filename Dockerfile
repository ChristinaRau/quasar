FROM node:lts-alpine

# install quasar
RUN npm install -g quasar

# make the 'quasar' folder the current working directory
WORKDIR /workspace/prototypes/quasar

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'quasar' folder)
COPY . .

# build app for production with minification
# RUN npm run build
# CMD [  "quasar", "serve", "dist/spa" ]

EXPOSE 9000
CMD [  "npm", "run", "dev" ]