# Docker Compose Test

This volume allows you to edit files on the host and see them updated in the container in real time.

This volume setting from the `docker-compose.yml` file *doesn't* save any data from the containers to the host:

    web:
        build: .
        ports:
            - '5000:5000'
        volumes:
            - .:/code
