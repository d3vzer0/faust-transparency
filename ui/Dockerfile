# Dockerfile as described on
# https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html

# Installs the ui project deps during initial dep-stage
FROM node:11.13.0 as dependency-stage
WORKDIR /app
COPY package*.json ./
RUN npm install

# Stage building the Vue app
FROM dependency-stage as build-stage

ARG VUE_APP_BASEAPI
ENV VUE_APP_BASEAPI ${VUE_APP_BASEAPI}

COPY . .
RUN npm run build

# Runs output of build-stage and hosts content
# via nginx service
FROM nginx:1.13.12-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]