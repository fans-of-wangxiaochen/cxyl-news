FROM python:alpine

COPY requirements.txt ./

RUN apk add --no-cache gcc \
                       g++ \
                       libxml2-dev \
                       libxslt-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc g++
