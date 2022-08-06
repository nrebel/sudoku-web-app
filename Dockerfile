FROM python:3.8.11-buster

RUN python3 -m pip install pulp
RUN python3 -m pip install flask

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y coinor-cbc

RUN ln -sf /usr/bin/cbc /usr/local/lib/python3.8/site-packages/pulp/apis/../solverdir/cbc/linux/32/cbc

WORKDIR /app

COPY ./ /app/

#RUN mkdir -p  /usr/local/lib/python3.8/site-packages/pulp/apis/../solverdir/cbc/linux/32/
#COPY /usr/bin/cbc /usr/local/lib/python3.8/site-packages/pulp/apis/../solverdir/cbc/linux/32/

EXPOSE 5000

CMD ["python3", "app.py"]
