FROM ubuntu:trusty
MAINTAINER Nilesh Gule <vn_nilesh@yahoo.com>

# prevent dpkg errors
ENV TERM=xterm-256color

# set mirror to NZ
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv
