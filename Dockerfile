FROM quay.io/jupyter/minimal-notebook

USER root
RUN apt-get update && apt-get install -yq tree && rm -rf /var/lib/apt/lists/*
USER $NB_UID

COPY ./archgit /home/jovyan/work/

# docker build --tag=archgit .
# docker run --rm -p 8888:8888 archgit
