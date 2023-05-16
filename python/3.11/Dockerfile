FROM python:3.11.3

RUN mkdir /code

WORKDIR /code

RUN apt update
RUN apt install -y gcc musl-dev g++ file libffi-dev vim less

RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/

RUN pipenv install sync
