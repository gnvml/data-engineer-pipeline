ARG debian_buster_image_tag=8-jre-slim
FROM openjdk:${debian_buster_image_tag}

# -- Layer: OS + Python 3.7

ARG shared_workspace=/api

COPY . ${shared_workspace}

WORKDIR ${shared_workspace}

RUN apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    apt-get install -y python3-pip && \
    pip3 install -r requirements.txt

# -- Runtime

EXPOSE 80
ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0", "--port", "80"]