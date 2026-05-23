FROM python:3.11

WORKDIR /app

COPY . /app

RUN chmod +x build.sh

RUN ./build.sh

EXPOSE 8000

CMD ["gunicorn", "foodproject.wsgi:application", "--bind", "0.0.0.0:8000"]