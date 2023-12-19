#!/bin/bash

docker ps | grep postgres_django >/dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "Container postgres_django já está em execução!"
    # Adicione o comando desejado aqui
else
    docker container run -d -p 5533:5432 \
        --name postgres_django \
        --mount type=volume,src=teste1,dst=/data \
        -e POSTGRES_USER=docker \
        -e POSTGRES_PASSWORD=docker123 \
        -e POSTGRES_DB=docker \
        postgres


    echo "Script executado com sucesso!"
fi

poetry run python manage.py makemigrations
poetry run python manage.py migrate

poetry run python manage.py runserver

