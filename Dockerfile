FROM python:3.11-alpine AS app

WORKDIR /app

RUN pip install gunicorn

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .


FROM app AS django
COPY ./entrypoint.sh /entrypoint.sh
CMD ["/entrypoint.sh"]


FROM app AS staticfiles
RUN ./manage.py collectstatic --no-input


FROM nginx:alpine AS webserver
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=staticfiles /app/static /usr/share/nginx/html/static
