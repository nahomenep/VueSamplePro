FROM python:3.7

ENV LANG C.UTF-8

COPY . /var/www

WORKDIR /var/www/
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
#RUN pip install flask-sqlalchemy
CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]