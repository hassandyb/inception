FROM alpine:latest

# Install Nginx
RUN apk update && apk add nginx

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy HTML files
COPY html /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Run Nginx
CMD ["nginx", "-g", "daemon off;"]
