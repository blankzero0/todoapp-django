FROM python:3.11-alpine AS app

WORKDIR /app

RUN pip install gunicorn

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


FROM app AS django
COPY ./entrypoint.sh /entrypoint.sh
EXPOSE 8000
CMD ["/entrypoint.sh"]


FROM app AS staticfiles
RUN ./manage.py collectstatic --no-input


FROM nginxproxy/nginx-proxy:alpine AS webserver
COPY serve-static.conf /etc/nginx/vhost.d/default
COPY --from=staticfiles /app/static /usr/share/nginx/html/static
