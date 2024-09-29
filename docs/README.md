# Publaze.com

The simple way to turn your youtube channel into a functioning website.

# Installation
There are many ways to run this.

* Docker compose
* Docker
* kubernetes
* Python
* IBM Clode Code Engine
* Google Cloud Platform
* Amazon Web Services Elastic Container Service with Fargate
* Amazon Web Services App runner 
* Azure App Services
* and many mores

Create an .env 
```
YOUTUBE_API_KEY=<youtube api key>
YOUTUBE_CHANNEL_ID=<youtube channel id>
FLASK_APP=/app/main
FLASK_ENV=development
FLASK_DEBUG=true
FLASK_RUN_HOST=0.0.0.0
CONFIGURATION_FILE=../configuration.yaml
```

Docker compose
```
docker compose up -d
```

# See it in action
[Snack Attack Squad](https://www.snackattacksquad.com/)
