# Dockerfile ejemplo para producción + local
FROM python:3.11

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn whitenoise

COPY . /code/

RUN python manage.py collectstatic --noinput

# CMD en JSON, más seguro
CMD ["gunicorn", "blogDataModel.wsgi:application", "--bind", "0.0.0.0:8000"]