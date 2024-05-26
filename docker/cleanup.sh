docker-compose down
docker-compose up --build

docker rmi -f $(docker images -aq)