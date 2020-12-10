# gRPC - Docker sample

```
docker network create grpc_net
```

```
docker run --rm -it -d --net grpc_net --name grpc-server grpc-server
```

```
docker run --rm -it -d --net grpc_net -p 5000:5000/tcp grpc-client:latest
```