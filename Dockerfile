FROM python:3.9.0

WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN pip install -U --upgrade pip
RUN pip install --upgrade -r ./requirements.txt

COPY main.py ./main.py

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
