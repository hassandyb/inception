


# ref  ==========================================
# FROM alpine:3.17

# RUN  apk update && apk upgrade && apk add nginx openssl --no-cache

# COPY ./conf/default.conf /etc/nginx/http.d/default.conf

#------------------------------------------

# RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/ss.key \
# 	-out /etc/ssl/certs/ss.crt \
# 	-subj "/C=/ST=/L=/O=1337/OU=/CN=srachdi"

#----------------------------------------
# RUN chmod -R 777 /etc/ssl/private/ss.key /etc/ssl/certs/ss.crt

# RUN mkdir -p /run/nginx /var/www/html


# EXPOSE 443

# ENTRYPOINT ["nginx","-g","daemon off;"]


# simple version using alpine   ==========================================



# FROM alpine:3.17

# RUN apk update && apk add nginx

# COPY nginx.conf /etc/nginx

# RUN mkdir -p /usr/share/nginx/html

# COPY index.html /usr/share/nginx/html/index.html

# EXPOSE 80

#  CMD ["nginx", "-g", "daemon off;"]



# simple version using debian   ==========================================



# FROM debian:11.9

# # Install Nginx
# RUN apt-get update && apt-get install -y nginx 

# # RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# # Copy custom Nginx configuration
# COPY nginx.conf /etc/nginx/nginx.conf

# # Create directory for HTML files
# RUN mkdir -p /usr/share/nginx/html

# # Copy HTML file
# COPY index.html /usr/share/nginx/html/index.html

# # Expose port 80
# EXPOSE 80

# # Command to run Nginx in the foreground
# CMD ["nginx", "-g", "daemon off;"]


 # The default dot config file ========================================



                #     server {
                #         listen 443 ssl;
                #         listen [::]:443 ssl;
                #         server_name srachdi.42.fr;

                #     error_page 404 403 500 502 503 504 /404.html;
                #     location = /404.html 
                #         {
                #             root /var/www/html;
                #         internal ;
                #     }
                #         # having a default route is a good practice
                #         root /var/www/html/wordpress;
                #         index index.php;
                #         location / 
                #         {
                #                 autoindex on;
                #                 try_files $uri $uri/  =404;
                #         }

                #         # SSL configuration
                #         ssl_certificate /etc/ssl/certs/ss.crt;
                #         ssl_certificate_key /etc/ssl/private/ss.key;
                #         ssl_protocols TLSv1.2 TLSv1.3;
                        
                #         # all php files are passed to php-fpm
                #         location ~ \.php$ 
                #         {
                #                 #404
                #                 try_files $uri =404;
                #                 fastcgi_pass wordpress:9000;
                #                 include fastcgi_params;
                #                 fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                #         }
                # # --------------------------
                #         # adminer configuration
                #         location /adminer {
                #                 root /var/www/html;
                #                 try_files /adminer/adminer.php  =404;
                #                 fastcgi_pass adminer:5000;
                #                 include fastcgi_params;
                #                 fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                #         }
                #         # website configuration
                #     location /website {
                #         root /var/www/html;
                #         index index.html;
                #         try_files /website/index.html  =404;
                #     }
                # }



