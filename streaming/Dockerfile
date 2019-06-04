FROM debian:buster-slim

RUN apt-get update -y --fix-missing \
  && apt-get install -y \
    build-essential \
    libgflags-dev \
    libsnappy-dev \
    zlib1g-dev \
    libbz2-dev \
    liblz4-dev \
    python3-pip \
    librocksdb-dev

ENV LD_LIBRARY_PATH=/usr/local/lib PORTABLE=1

RUN pip3 install python-rocksdb

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /opt/
COPY . ./streaming/

ARG STREAM_NAME=streaming.transparency
ENV STREAM_NAME="${STREAM_NAME}"

ARG KAFKA_HOST=kafka://kafka:9092
ENV KAFKA_HOST="${KAFKA_HOST}"

ARG DBHOST=mongodb
ENV DBHOST="${DBHOST}"

CMD ["faust", "-A", "streaming.app", "worker"]