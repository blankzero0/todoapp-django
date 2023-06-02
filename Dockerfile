FROM python:3.11-alpine AS app

WORKDIR /app

RUN pip install gunicorn

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


FROM app AS staticfiles
RUN ./manage.py collectstatic --no-input


FROM jonasal/nginx-certbot:4.2.1-alpine AS webserver
COPY proxy.conf /etc/nginx/templates/proxy.conf.template
COPY --from=staticfiles /app/static /usr/share/nginx/html/static

ENV HOST=localhost


FROM app AS django
COPY ./entrypoint.sh /entrypoint.sh
EXPOSE 8000
CMD ["/entrypoint.sh"]
