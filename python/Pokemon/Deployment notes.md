## To deploy run the docker file:


docker build -t pokemon-web .

docker network create pokemon-network
docker network ls


docker run -d \
	--rm \
	--name postgres \
	--network pokemon-network \
	-p 5432:5432 \
	-e POSTGRES_PASSWORD=mypassword \
	-v postgres_volume:/var/lib/postgresql/data \
	postgres:14.19-alpine3.21

docker run -d \
	--rm \
	--name my-pgadmin \
	--network pokemon-network \
	-p 80:80 \
	-e PGADMIN_DEFAULT_EMAIL=robert.rj.harte@protonmail.com \
	-e PGADMIN_DEFAULT_PASSWORD=P@ssword \
	dpage/pgadmin4:9.9.0

docker run -d \
	--rm \
	--name pokemon \
	--network pokemon-network \
	-p 5000:5000 \
    pokemon-web:latest



for docker-compose:

docker-compose -f docker-compose.yaml up
docker-compose -f docker-compose.yaml stop
docker-compose down