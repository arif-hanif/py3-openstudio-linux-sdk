FROM python:3.6

# Install dependencies
RUN apt-get update && apt-get install -y \
    autoconf \
    bison \
    build-essential \
    chrpath \
    cmake-curses-gui \
    cmake-gui \
    git \
    libssl-dev \
    libxt-dev \
    libncurses5-dev \
    libgl1-mesa-dev \
    libexpat1-dev \
    libpng-dev \
    libfreetype6-dev \
    libdbus-glib-1-dev \
    libglib2.0-dev \
    libfontconfig1-dev \
    libxi-dev \
    libxrender-dev \
    libgeographic-dev \
    libicu-dev \
    libffi-dev \
    libgdbm-dev \
    libqdbm-dev \
    libreadline-dev \
    libyaml-dev \
    libharfbuzz-dev \
    libgmp-dev

RUN apt remove -y libharfbuzz-dev
RUN apt-get install -y software-properties-common vim && \
    apt-add-repository -y ppa:jonathonf/texlive && \
    apt-add-repository -y ppa:jonathonf/python-3.6
RUN apt update -y
RUN apt install -y libharfbuzz-dev

RUN mkdir -p /usr/src

# Copy the app to container
COPY ./py3_openstudio_linux_sdk /usr/src/openstudio

RUN export LD_LIBRARY_PATH=/usr/src/openstudio:$LD_LIBRARY_PATH

WORKDIR /usr/src