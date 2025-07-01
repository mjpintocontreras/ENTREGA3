FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-11-jdk \
    wget \
    unzip \
    curl \
    git \
    nano \
    && apt-get clean

RUN wget https://downloads.apache.org/pig/pig-0.17.0/pig-0.17.0.tar.gz && \
    tar -xvzf pig-0.17.0.tar.gz && \
    mv pig-0.17.0 /opt/pig

ENV PIG_HOME=/opt/pig
ENV PATH=$PATH:$PIG_HOME/bin

WORKDIR /app
COPY . /app

RUN pip3 install matplotlib pandas

CMD ["bash"]
