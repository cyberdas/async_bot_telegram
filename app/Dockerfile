FROM python:3.9.2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /search_bot
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python main.py