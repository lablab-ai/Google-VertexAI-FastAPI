Backend API for ALEX

To deploy new version

```
gcloud functions deploy alice_function --source=. --trigger-http --region=europe-west2 --runtime=python38
```
## Running locally with Docker compose
in root folder do   
`docker-compose build`  
`docker-compose up`


## Running locally
install uvicorn with `pip install uvicorn`  
```
uvicorn main:app --reload
```

#### API Key
`5IDgEcqRThMEWbZFUZ2kh4`

#### API Url
https://alex-api-zclpkhrrea-nw.a.run.app

#### API Docs
https://alex-api-zclpkhrrea-nw.a.run.app/redoc

#### Swagger
https://alex-api-zclpkhrrea-nw.a.run.app/docs


## Publishing to AWS
### Install/configure `kubectl` (once):
https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html
### Build a Docker image:
`docker build -t 681269368063.dkr.ecr.eu-north-1.amazonaws.com/alex-api .`
### Push a Docker image:
`docker push 681269368063.dkr.ecr.eu-north-1.amazonaws.com/alex-api`\
(https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)
### Apply the k8s config:
`kubectl apply -f kubernetes/config.yaml`
