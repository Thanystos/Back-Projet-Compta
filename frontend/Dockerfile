# Étape 1 : build du front
FROM node:20 AS builder
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# Étape 2 : serveur nginx
FROM nginx:1.25

# Copie du build dans nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Copie de la config nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
