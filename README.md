# webapp-playground-py
A repo to practice web development in the Python language. Exploring db connections and libraries withh a GIS focus.


## Building 

```commandline
docker build -t playapp-py --build-arg BASE_IMAGE=python:3.13-slim .
```

# Running 
```commandline
docker run --rm -p 8080:8080 playapp-py:latest
```


# Testing 
```commandline
curl "http://localhost:8080"
```

OR 
```commandline
pytest
```