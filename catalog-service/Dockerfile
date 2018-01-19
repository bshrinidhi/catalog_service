FROM python:3.4-alpine

COPY . /catalog
WORKDIR /catalog

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
