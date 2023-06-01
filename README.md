# blog2.0
____
**Get started**

- Clone repository
- Install requirements:

    `pip install -r requirements.txt`

- Create and fill `.env` file, where `POSTGRES_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT` are your settings.  
Example: `.env.example`. You can use the variables copied from there for testing.
- Start a postgres instance via docker:

    `docker run -p 5432:5432 -e POSTGRES_PASSWORD=password postgres`,  
where `password` is your `POSTGRES_PASSWORD`. 

- Migrate command:

    `python manage.py migrate`

- Insert blog publications into db (default = 10 publications):

    `python manage.py generate_publications`

- Runserver command:

    `python manage.py runserver`
