FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

RUN mkdir /code

WORKDIR /code

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3.11
RUN apt install -y python3-pip
RUN apt install -y nvidia-cuda-toolkit
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

COPY Pipfile Pipfile.lock /code/

RUN pipenv sync

RUN export XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/lib/cuda
