FROM ubuntu

RUN apt-get update -y && apt-get install python3 -y && apt-get install g++ -y

COPY . /

ENTRYPOINT ["python3", "judger.py"]
