FROM python:3.7-alpine3.9
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "/main.py"]
COPY main.py /main.py