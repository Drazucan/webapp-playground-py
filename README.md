# webapp-playground-py
A repo to practice web development in the Python language. Exploring db connections and libraries withh a GIS focus.


## Building 

```commandline
docker build -t playapp-py --build-arg BASE_IMAGE=python:3.13-slim .
```

# Running 
```commandline
# Isolated Running
docker run --rm -p 8080:8080 playapp-py:latest

# Running the postgis container

# Running with a postgis container present
docker run --rm -p 8080:8080 -e DB_HOST=postgres --add-host postgres:$(docker inspect $(docker ps --format "{{.Image}}|{{.Names}}" | grep postgis | awk -F '|' '{print $2}') | jq .[0].NetworkSettings.Networks.bridge.IPAddress | sed 's/\"//g') playapp-py:latest


```


# Testing 
```commandline
curl "http://localhost:8080"
curl "http://localhost:8080/v1/users"
```

OR 
```commandline
pytest
```

## Docs
Run local and go to http://localhost:8080/docs/