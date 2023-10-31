start:
	minikube start

build_base_image:
	docker build --tag=tutorial_python_brasil_2023 --file=Dockerfile .

deploy: build_base_image
	kubectl apply -f kubernetes

restart_web:
	kubectl rollout restart deployment web

dashboard:
	minikube dashboard