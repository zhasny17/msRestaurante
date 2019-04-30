FROM hrinfo/mspython:latest
MAINTAINER HR INFO
WORKDIR /mspython
COPY . /mspython

ENTRYPOINT ["python3"]
CMD ["app.py"]