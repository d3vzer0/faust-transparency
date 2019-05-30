FROM python:3.6

RUN apt-get update && apt-get install -y build-essential python3-dev
RUN apt-get install -y build-essential libsnappy-dev zlib1g-dev libbz2-dev libgflags-dev liblz4-dev
RUN apt-get install -y librocksdb-dev

RUN cd /tmp \
  && curl -sL rocksdb.tar.gz https://github.com/facebook/rocksdb/archive/v6.0.2.tar.gz > rocksdb.tar.gz \
  && tar fvxz rocksdb.tar.gz \
  && cd rocksdb-6.0.2 \
  && make shared_lib \
  && make install-shared


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get remove -y \
  build-essential \
  && rm -rf /tmp

WORKDIR /opt/
COPY . ./streaming/


ARG STREAM_NAME=streaming.transparency
ENV STREAM_NAME="${STREAM_NAME}"

ARG KAFKA_HOST=kafka://kafka:9092
ENV KAFKA_HOST="${KAFKA_HOST}"

CMD ["faust", "-A", "streaming.app", "worker"]