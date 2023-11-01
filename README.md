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

# Execução com Kubernetes

```sh
minikube delete # ensure any previous cluster get deleted
```

```sh
minikube start
```

```sh
eval $(minikube docker-env) # make current session use docker inside minikube, need to run for every terminal session or minikube restart
```

```sh
docker build --tag tutorial_python_brasil_2023 .
```

```sh
kubectl apply -f kubernetes
```

```sh
kubectl get pods
```

```sh
kubectl apply -f kubernetes/locust
```

```sh
minikube service web --url
```

Copie a URL retornada para usar no parâmetro "Host" do Locust.

```sh
minikube service locust-service
```

Inicie o teste do locust com os seguintes parâmetros:

- Number of users: 10
- Spawn rate: 10
- Host: URL do service web 

Verifique na aba "Statistics" que todas as requisições são bem sucedidas e então simule um deploy do componente web: 

```sh
kubectl rollout restart deployment web
```

Execute o comando abaixo repetidas vezes para ver os pods sendo criados e terminados sem gerar interrupções.

```sh
kubectl get pods
```

Verifique que não houveram falhas no locust.

# Feature flags

Verifique que o estado atual do switch é `false`: http://{{HOST_WEB}}:{{PORTA_WEB}}/switches/

Para habilitá-lo, crie um superusuário:

```sh
make createsuperuser
```

Vá até o admin de switches: http://{{HOST_WEB}}:{{PORTA_WEB}}/admin/waffle/switch/ e crie o switch `MY_AWESOME_SWITCH` marcando o checkbox `Active`.

Verifique que o estado atual do switch mudou para `true`: http://{{HOST_WEB}}:{{PORTA_WEB}}/switches/

Podemos usar esse switch tanto pra controle de fluxo no próprio Django, quanto para o frontend.

# Migrations
