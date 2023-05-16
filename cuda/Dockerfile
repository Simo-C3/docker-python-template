FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

RUN mkdir /code

WORKDIR /code

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3.11
RUN apt install -y python3-pip
# RUN apt install -y nvidia-cuda-toolkit
RUN rm -rf /usr/bin/python
RUN ln -s /usr/bin/python3.11 /usr/bin/python
RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/

RUN pipenv --python 3.11
RUN pipenv install

RUN export XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/lib/cuda