# tutorial-python-brasil-2023

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Tutorial curto ministrado na Python Brasil 2023. Deploy e release contínuos em Django.

[Slides](https://docs.google.com/presentation/d/1GfDuo623tmMp-SIYUc4P7vATusAZdCv4PM3SwaY5df0/edit?usp=sharing)

# Pré-requisitos

- [Docker e docker-compose](https://docs.docker.com/engine/install/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Python 3.8](https://www.python.org/downloads/release/python-3818/)
  - [venv](https://docs.python.org/pt-br/3/library/venv.html)

# Execução com docker-compose

```sh
docker build --tag=tutorial-python-brasil-2023/receitas .
```

```sh
docker-compose build
```

```sh
docker-compose up -d
```

Acesse o locust em [http://localhost:8089/](http://localhost:8089/) e inicie um teste trocando:

- Number of users: 10
- Spawn rate: 10

Verifique na aba "Statistics" que todas as requisições são bem sucedidas e então simule um deploy do componente web:

```sh
docker-compose restart web
```

Verifique que parte das requisições falharam. O motivo da falha pode ser visto na aba "Failures"
