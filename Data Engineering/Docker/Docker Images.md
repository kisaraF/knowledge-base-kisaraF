# Docker Images

Dockefile is a set of instructions on how to install dependencies requires for an application to work and execute them.

Always the Dockerfile while will be started from a base OS or another image based on an OS.

`RUN` command will execute a command to install dependency based on the image.

Pay attention to the below sample Dockerfile

```Dockerfile

FROM Ubuntu

RUN apt-get update && apt-get -y install python

RUN pip install flask flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```