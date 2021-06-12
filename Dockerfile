FROM python:slim
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 40041
COPY . .
CMD ["python", "server.py"]
