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
