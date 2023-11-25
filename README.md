# Book api testwork
## Clone repo
```
git clone https://github.com/AuTHoRzero/book_api.git
```
## Make sure the ports are available on your PC
1. 8000
2. 5432
3. 6379

```
netstat | grep 8000
netstat | grep 5432
netstat | grep 6379
```

### If ports are busy
open the docker-compose.yml file in any text editor and change the busy port to a different port

## Open dir and build docker-compose
```
cd book_api
docker-compose build
```

## Run containers
```
docker-compose up -d
```

## Use
After these steps you can use this application, it will be available at 0.0.0.0.0:8000 on your pc

## Stop App
```
docker-compose down
```

