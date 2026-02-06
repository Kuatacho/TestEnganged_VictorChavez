# Build stage
FROM node:20-alpine AS builder
WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install --silent

COPY . .
RUN npm run build --silent

# Production stage
FROM nginx:stable-alpine
# Clear default nginx html to avoid showing default page
RUN rm -rf /usr/share/nginx/html/*

# Copy built static files into nginx html directory
COPY --from=builder /app/dist/frontend/browser/ /usr/share/nginx/html/

# Copy custom nginx config to enable SPA fallback and proxy /api
COPY nginx.conf /etc/nginx/conf.d/default.conf

# If Angular built a CSR index inside /browser, use it as index.html for SPA
RUN if [ -f /usr/share/nginx/html/browser/index.csr.html ]; then cp /usr/share/nginx/html/browser/index.csr.html /usr/share/nginx/html/index.html; fi

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
