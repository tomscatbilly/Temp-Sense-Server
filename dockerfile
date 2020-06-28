FROM ubuntu:latest
#Setup Environment
VOLUME ["/mnt/script"]
WORKDIR /mnt/script

ENV cputemp CPUTIN
ENV cpufan fan2

ENV systemp SYSTIN
ENV sysfan fan1

ENV gputemp temp1

#Install Deps
RUN apt-get update && apt-get -y install sudo
RUN sudo apt install -y python3 python3-pip curl wget lm-sensors
RUN wget "https://ctwhonnock.ddns.net/DockerWebFiles/TempSenseServer.py"
RUN sudo apt update
RUN pip3 install flask


RUN echo "Installed Depenendcies"

#Run Bot
CMD python3 TempSenseServer.py
