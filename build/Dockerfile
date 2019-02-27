FROM ubuntu:16.04

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

# install python
RUN apt-get install -y python3.6 python3.6-dev python3-pip python3.6-venv

# update pip
RUN python3.6 -m pip install pip --upgrade && \
    python3.6 -m pip install wheel

# install cmake
RUN apt install wget
RUN apt remove -y cmake \
    && wget https://cmake.org/files/v3.7/cmake-3.7.1.tar.gz \
    && tar xzf cmake-3.7.1.tar.gz \
    && cd cmake-3.7.1/ \
    && ./configure \
    && make \
    && make install

# clone openstudio repo
RUN git clone  https://github.com/NREL/OpenStudio.git \
    && cd OpenStudio \
    && git reset --hard 544f363db560f6cc0561938fc4ae282923401c7a

# make build directory
RUN cd OpenStudio \
    && mkdir -p build \
    && cd build

WORKDIR /OpenStudio/build

COPY . .

# configure cmake
#RUN cmake \
#    -DBUILD_SHARED_LIBS=ON \
#    -DBUILD_OS_APP=OFF \
#    -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
#    -DBUILD_PYTHON_BINDINGS=ON \
#    ../openstudiocore

# make and catch iddfactory error
#RUN chmod +x ./make_bindings.sh
#RUN ./make_bindings.sh