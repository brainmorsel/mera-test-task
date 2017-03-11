# Run

    sudo docker-compose build
    sudo docker-compose up -d
    sudo docker-compose run web python manage.py migrate
    sudo docker-compose run web python manage.py createsuperuser --username admin
    sudo docker-compose restart web

    # add users at http://localhost:8000/admin/auth/user/add/
    # and put username and password into .env-client

    curl -u admin:PASSWORD http://localhost:8000/api/uptime
