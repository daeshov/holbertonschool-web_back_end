# Builds a docker image for a node js
build:
	docker build -t nodejs .

# Runs the dev-box image in a container
run:
	docker run -it --rm --name nodejs

stop:
	docker stop nodejs

# Remove all docker containers
clean:
	docker container prune -f

# Remove all docker images, containers, and volumes
nuke:
	docker system prune -af
