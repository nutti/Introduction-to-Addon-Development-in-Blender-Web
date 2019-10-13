FROM ubuntu:18.04

WORKDIR /root

RUN env
RUN apt-get update -y -qq
RUN apt-get install -y \
            ruby=1:2.5.1 \
            ruby-dev=1:2.5.1 \
            nodejs=8.10.0~dfsg-2ubuntu0.4 \
            npm=3.5.2-0ubuntu4 \
            pandoc=1.19.2.4~dfsg-1build4 \
            git=1:2.17.1-1ubuntu0.4 \
            git-lfs=2.3.4-1
RUN npm install -g gulp@4.0.2
RUN gem install bundler -v 2.0.2
