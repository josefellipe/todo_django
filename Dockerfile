FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo.wsgi:application"]
