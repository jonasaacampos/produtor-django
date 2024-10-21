<p align="center">
<a href='https://github.com/jonasaacampos'><img src='https://img.shields.io/badge/feito%20com%20%E2%9D%A4%20por-jaac-cyan'></a>
<a href='https://www.linkedin.com/in/jonasaacampos'><img src='https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8'></a>
</p>

<p align="center">
   <a href='https://github.com/jonasaacampos'>
      <img alt="" src="https://img.shields.io/static/v1?color=blue&label=Python&message=Full-Stack&style=for-the-badge&logo=Python"/>
      </a>
</p>



<h1>Brain Farms</h1>

<img alt="logo desc..." src="static\img\repo_logo.png" width=150 align=right>



<h2>Fazendas inteligentes</h2>

![](https://img.shields.io/badge/python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/django-informational?style=flat&logo=django&logoColor=white&color=green_)
![](https://img.shields.io/badge/docker-informational?style=flat&logo=docker&logoColor=white&color=navy)
![](https://img.shields.io/badge/AWS-informational?style=flat&logo=amazon&logoColor=white&color=red)
![](https://img.shields.io/badge/postgre-informational?style=flat&logo=postgresql&logoColor=white&color=black)
![](https://img.shields.io/badge/mysql-informational?style=flat&logo=mysql&logoColor=white&color=pink)
![](https://img.shields.io/badge/javascript-informational?style=flat&logo=javascript&logoColor=white&color=gold)
![](https://img.shields.io/badge/HTML-informational?style=flat&logo=html5&logoColor=white&color=blue)
![](https://img.shields.io/badge/CSS-informational?style=flat&logo=css3&logoColor=white&color=pink)

> Cadastro de produtores rurais, com dashboards e listagem de cadastros gerados em tempo real.
>
> O projeto foi desenvolvido em python ([prova de conceito](https://github.com/jonasaacampos/cadastro-produtor-rural)) e django foi utilizado como framework web para produção.
>
> Foram escritos testes unitários, e criado configurações de infraestrutura para a execução em containers **docker**. Os containeres foram disponbilizado publicamente no dockerhub ([aplicação](https://hub.docker.com/repository/docker/jaacampos/produtor-django-web/general)) e ([banco de dados PostgreSql](https://hub.docker.com/repository/docker/jaacampos/produtor-django-web-psql/general)).
>
> Foi criado um repositório privado na AWS (Elastic Container Register), e criado um script de automação para criação e upload dos contâineres
>
> O **deploy** foi realizado em uma instância EC2 da AWS, sendo executado em imagens docker.

-------------

<h3>Índice</h3>

- [Obtendo o projeto](#obtendo-o-projeto)
  - [Popular Banco de dados](#popular-banco-de-dados)
- [Demo](#demo)
- [Checklist de Implementação](#checklist-de-implementação)
  - [Cadastro de Produtor Rural](#cadastro-de-produtor-rural)
  - [Requisitos de Negócio](#requisitos-de-negócio)
  - [Dashboard](#dashboard)
- [Requisitos Técnicos](#requisitos-técnicos)
  - [Front-end](#front-end)
  - [Back-end](#back-end)
- [Desejável](#desejável)
- [Contato](#contato)


## Obtendo o projeto

Baixe este reposiório `https://github.com/jonasaacampos/produtor-django`

**Execução Local (branch dev)**

- [ ] Crie um ambiente virtual python (No vs code, [faça isso](https://gist.github.com/jonasaacampos/b53a591b67321c1896d684178ca5fc2c))
- [ ] Instale as dependências `pip install -r requirements.txt`
- [ ] Inicie o banco de dados `python manage.py migrate`
- [ ] Crie o superusuário `python manage.py createsuperuser`

**Execução em container (branch main)**

- [ ] Gere as imagens e execute o container `docker-compose up -d`
- [ ] Acesse o container `docker-compose exec web bash` (IDE WEB) ou  `docker-compose exec bash`
- [ ] Inicie o banco de dados `python manage.py migrate`
- [ ] Crie o superusuário `python manage.py createsuperuser`
- [ ] Saia do container `exit`

**testes**

-  Execute os testes com o comando `python manage.py test `

### Popular Banco de dados

Para preencher a aplicação com dados aleatórios, execute o script `fake_data_gen.py` na raiz do projeto. 

Por padrão são geradas 10 inserções de usuário e 10 Inserções de Fazenda.

-----

## Demo

Veja ao vivo clicando **[aqui](http://34.207.220.87:8000)**


| Usuário       | Senha     |
|---------------|-----------|
| brainfarmer   | teste1234 |


## Checklist de Implementação

<details><summary><b>Requisitos</b></summary>

### Cadastro de Produtor Rural

- [x] Implementar cadastro de produtor rural com os seguintes campos:
  - [x] CPF ou CNPJ
  - [x] Nome do produtor
  - [x] Nome da Fazenda
  - [x] Cidade
  - [x] Estado
  - [x] Área total em hectares da fazenda
  - [x] Área agricultável em hectares
  - [x] Área de vegetação em hectares
  - [x] Culturas plantadas (Soja, Milho, Algodão, Café, Cana de Açucar)

### Requisitos de Negócio

- [x] Possibilidade de cadastrar produtores rurais
- [x] Possibilidade de editar produtores rurais
- [x] Possibilidade de excluir produtores rurais
- [x] Validação de CPF e CNPJ digitados incorretamente
- [x] Validação para garantir que a soma de área agricultável e vegetação não seja maior que a área total da fazenda
- [x] Permitir que cada produtor plante mais de uma cultura em sua fazenda

### Dashboard

- [x] Exibir total de fazendas em quantidade 
- [x] Exibir total de fazendas em hectares (área total)
- [x] Gráfico de pizza por estado
- [x] Gráfico de pizza por cultura
- [x] Gráfico de pizza por uso de solo (Área agricultável e vegetação)

## Requisitos Técnicos

### Front-end

- [x] Utilizar Python
- [x] Criar pelo menos um teste unitário por componente (Opcional)
- [x] Criação das estruturas de dados "mockados"

### Back-end

- [x] Salvar os dados em um banco de dados Postgres
- [ ] Implementar endpoints para:
  - [ ] Cadastrar produtores rurais
  - [ ] Editar produtores rurais
  - [ ] Excluir produtores rurais
- [x] Retornar os totais para o dashboard
- [x] Criação das estruturas de dados "mockados"

## Desejável

- [x] Aplicar conceitos como SOLID, KISS, Clean Code, API Contracts, Tests, Layered Architecture

</details>


<details>
<summary> <b>Funcionalidades Futuras</b> </summary>

- [ ] Endpoints para interação com a aplicação
- [ ] Configuração de repositório para `Continous Integraion - CI`
- [ ] Inserção de gráficos dinâmicos dentro para o dashboard
- [ ] Atualização de relatórios estáticos de forma assíncrona

</details>



-----
<!-- CONTACT -->
## Contato

**Author:** Jonas Araujo de Avila Campos

<p align='center'>
  <a href='https://github.com/jonasaacampos'>
    <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'/>
  </a>
  <a href='https://www.linkedin.com/in/jonasaacampos/'>
    <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'/>
  </a>
</p>

-----