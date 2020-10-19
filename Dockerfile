FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

COPY . /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libxslt-dev \ 
&& pip3 install pip==10.0.1

RUN pip3 install lxml


RUN pip3 install -r requirements.txt


EXPOSE 5001

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
