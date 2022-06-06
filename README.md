# Stockless

## Setup

Create a `environment` file, that contains all application *environment* variables
```shell
cp .env.example .env
```

### Docker Compose
```bash
docker-compose up --build
```

Now head over to `http://127.0.0.1:5001/` or `http://127.0.0.1:5001/health-check`, and you should see your hello world *greeting*.
