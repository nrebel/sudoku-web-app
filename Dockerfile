FROM python:latest
RUN pip3 --user install pulp
RUN pip3 --user install flask
WORKDIR /app
COPY .* /app
EXPOSE 5000
RUN python3 app.py
