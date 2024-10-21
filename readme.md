## Configuração do ambiente

- Criar ambiente virtual python
- Ativar ambiente virtual `.\.venv\Scripts\activate`
- instalar django `pip install django`
- iniciar projeto no diretorio atual `django-admin startproject core .`
- iniciar app `python manage.py startapp meu_app`

## Configurando Django

- Inserir app criado no arquivo `settings.py` do core na sessção `INSTALLED_APPS`

## executar app

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## testes

`python manage.py test `


## Docker - Criar Container

```bash
docker-compose up --build

# para realizar as migrations
docker-compose up -d
docker-compose exec web bash
python manage.py createsuperuser
python manage.py migrate
exit

```

## Docker - compartilhar container docker hub

```bash
# compartilhar conteiner no dockerhub
docker tag <nome-da-imagem-local>:<tag> <seu-usuario>/<nome-do-repositorio>:<tag>
docker push <seu-usuario>/<nome-do-repositorio>:<tag>

docker tag produtor-django-web:latest jaacampos/produtor-django-web:v0.1
docker tag postgres:13 jaacampos/produtor-django-web-psql:v0.1

docker push jaacampos/produtor-django-web:v0.1
docker push jaacampos/produtor-django-web-psql:v0.1
docker login -u jaacampos
```

## Docker aws (Container Registry (ECR))

```bash
# para baixar utilitário aws-cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# inserir chave IAM
aws configure

# após configurar repositório no ECR, copiar comandos de push (foram armazenamos em no arquivo buid.sh)
docker tag <nome-da-imagem-local>:<tag> <seu-usuario>/<nome-do-repositorio>:<tag>
docker push <seu-usuario>/<nome-do-repositorio>:<tag>

```

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 396913712383.dkr.ecr.us-east-1.amazonaws.com
docker build -t brainfarms .
docker tag brainfarms:latest 396913712383.dkr.ecr.us-east-1.amazonaws.com/brainfarms:latest
docker push 396913712383.dkr.ecr.us-east-1.amazonaws.com/brainfarms:latest