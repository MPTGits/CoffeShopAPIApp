# ![image](https://user-images.githubusercontent.com/37246713/228130394-f73003a1-4b28-454e-b3cf-59918f77292e.png)
# CoffeShopAPI

## Frameworks and software used
* Python 3.11
* Docker 4.17.0


## Setup

To build the Docker containers that contain the Postgress database and python server execute the following command in the main directory:

```
docker-compose up --build 
```

If 'Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)' and 'listening on IPv4 address "0.0.0.0", port 5432' come up in the logs that means that the database and python server are both running and you can now query your API by making a request to 'http://0.0.0.0:8000/<endpoint>'.
