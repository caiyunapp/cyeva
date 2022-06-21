FROM python:3.7.9-slim-stretch AS sphinx

WORKDIR /opt

RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && apt-get install -y make

RUN pip install -i "https://pypi.doubanio.com/simple/" pip -U pip setuptools wheel && \
    pip install -i "https://pypi.doubanio.com/simple/" Sphinx>=5.0.1 sphinx-rtd-theme>=1.0.0 --trusted-host "https://pypi.doubanio.com"

COPY . .

RUN make html

FROM nginx

COPY nginx/conf.d /etc/nginx/conf.d
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=sphinx /opt/build/html /html
