FROM python:3.11

WORKDIR /code

# Copia y instala requisitos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn whitenoise

# Copia el resto del proyecto
COPY . /code/

# Ejecuta collectstatic
RUN python manage.py collectstatic --noinput

# CMD usando python -m gunicorn (evita problemas de PATH)
CMD ["python", "-m", "gunicorn", "blogDataModel.wsgi:application", "--bind", "0.0.0.0:8000"]