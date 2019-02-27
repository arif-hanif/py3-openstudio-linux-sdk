FROM python:3.6

RUN mkdir -p /usr/src

# Copy the app to container
COPY ./py3_openstudio_linux_sdk /usr/src/openstudio

RUN export LD_LIBRARY_PATH=/usr/src/openstudio:$LD_LIBRARY_PATH

WORKDIR /usr/src