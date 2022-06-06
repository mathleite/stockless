# Command Utils

### UP all containers
with container logs:
```shell
docker-compose up --build
```
without logs:
```shell
docker-compose up --build -d
```

### Stop containers
stop and remove containers:
```shell
docker-compose down -t 1
```
only stop:
```shell
docker stop $(docker ps -aq) -t 1
```

### Show logs from X container
```shell
docker logs :id_container
```

### List running containers
```shell
docker ps
```