FROM ubuntu:20.04

RUN apt update

RUN apt install -y tzdata

RUN apt install -y wget build-essential libbz2-dev libdb-dev \
    libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
    libncursesw5-dev libsqlite3-dev libssl-dev \
    zlib1g-dev uuid-dev tk-dev

RUN cd /tmp && \
    wget https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tgz && \
    tar -xvzof Python-3.9.16.tgz && \
    cd Python-3.9.16 && \
    ./configure --enable-optimizations --prefix=/usr/local/ && \
    make && \
    make install

RUN apt -y install python3-pip
RUN apt autoremove -y

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt
