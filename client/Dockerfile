
# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
ARG API_BASE_URL
COPY package*.json ./
ENV API_BASE_URL=${API_BASE_URL}
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY --from=build-stage /app/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]