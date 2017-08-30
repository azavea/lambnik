FROM python:2.7-slim

COPY ./requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
  && rm /tmp/requirements.txt

COPY . usr/src
WORKDIR /usr/src/

CMD ["python", "/usr/src/test.py"]
