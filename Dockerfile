# Serve o site estático da Rosa Locks com nginx (imagem minúscula).
FROM nginx:alpine
COPY . /usr/share/nginx/html
# remove arquivos que não precisam ir pro público
RUN rm -f /usr/share/nginx/html/Dockerfile \
          /usr/share/nginx/html/nginx.conf \
          /usr/share/nginx/html/build.py \
          /usr/share/nginx/html/LEIA-ME.md
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
