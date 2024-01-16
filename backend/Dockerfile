FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

ENTRYPOINT [ "/code/entrypoint.sh" ]

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]