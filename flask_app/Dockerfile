FROM python:3.12-slim

RUN useradd -m flask

WORKDIR /home/flask

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R flask:flask /home/flask

USER flask

EXPOSE 5000

CMD ["python", "app.py"]