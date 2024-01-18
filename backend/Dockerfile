FROM python:3.10

WORKDIR /code

# environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# apt-get update
RUN apt-get update

# psycog2 dependencies
# RUN apt-get -y install libpq-dev python-dev
RUN pip install psycopg2

# dependencies
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt


COPY . /code/
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh


ENTRYPOINT [ "./entrypoint.sh" ] 

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "pinboard.wsgi:application"]