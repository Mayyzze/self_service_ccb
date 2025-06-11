# Step 1 : Build frontend with Node.js
FROM node:20-alpine AS builder

WORKDIR /app

# Step 1.1 : Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy only the files necessary for the build
COPY vite.config.js ./
COPY .env .env
COPY ./public ./public
COPY ./src ./src

RUN npm run build

# Step 2: Use Nginx to serve the build
FROM nginx:alpine

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the generated build to the public folder of Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
