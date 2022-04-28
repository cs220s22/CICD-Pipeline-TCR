FROM python:slim

COPY requirements.txt .

RUN python3 -m venv .venv
RUN .venv/bin/pip3 install -r requirements.txt

COPY app.py .

CMD [".venv/bin/python3", "app.py"]
