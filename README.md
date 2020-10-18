# ChallengeCloudSec
Mercado Livre - Desafio

Esta API tem como objetivo:

- Um endpoint GET que devolve todos os IPs de TOR obtidos das fontes externas
detalhadas (https://www.dan.me.uk/tornodes , https://torstatus.blutmagie.de)

- Um endpoint POST que receba um IP e o agregue à uma base de dados onde se
encontram todos os IPs que não queremos que apareçam no output do endpoint 3

- Um endpoint GET que devolve os IPs obtidos das fontes externas EXCETO os que
se encontram na base de dados (IPs carregados utilizando o endpoint 2)

## Pré requisitos

- Python3 
- Git 
- Flask
- flask_sqlalchemy
- flask_migrate
- flask_script
- flask_marshmallow
- marshmallow_sqlalchemy
- flask-jwt-extended

## Deploy 

Docker Deploy

```bash
docker-compose up
```

## Quick Start Using Pipenv

``` bash
# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install -r requirements.txt

## Como fazer as migrações
```sh
main.py db init
main.py db migrate
main.py db upgrade
```

# Create DB
```sh
$ python
from main import db
db.create_all()
exit()
```

# Run Server (http://localhst:5001)
```sh
python main.py
```

## Endpoints
```sh
* GET     /api/
* GET     /api/:id
* POST    /api/:id
* PUT     /api/:id
* DELETE  /api/:id
```
