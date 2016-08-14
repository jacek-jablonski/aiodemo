# aiothttp REST API demo
A sample python rest api using aiohttp and some other choice libraries to optimize for speed without adding a too much additional complexity.

Notable compromises:
- [schematics](https://github.com/schematics/schematics) provides serialization but no ORM
- [asyncpg](https://github.com/MagicStack/asyncpg) provides fast, binary, async access to Postgres, but is young and the documentation provides only the basics.
- [ujson](https://github.com/esnme/ultrajson) is very fast but, does not allow for customizing the serialization of unknown types, it just serializes an "unserializable" object to a dict containing each of its properties.

## Getting Started

### Requirements
- Docker

### Build images
Run the following commands to build the needed Docker images

```
docker build -t aiodemo:latest .
cd docker/db/
docker build -t aiodemodb:latest .
```

### Running the demo
In the project root, use `docker-compose` to get everything running

```
docker-compose up -d db
docker-compose up -d web
```

To validate everything is running correctly, we will check the version

First get your docker host machine ip, on mac this is probably found using
one of these commands `docker-machine ip` or `dlite ip`.  Then run the
following command substituting your ip for the `<docker_host>`

```
curl -H "Authorization: abc123" http://<docker_host>:8080/version
```

Note that for demonstration purposes, all endpoints require token authorization
and the token is `abc123`.