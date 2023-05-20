# Blog
____
**Get started**


1. Clone repository

2. Install requirements:

    `pip install -r requirements.txt`

3. Migrate command:

    `python manage.py migrate`

4. (optional) Insert blog publications into db (default = 10 publications):

    `python manage.py generate_publications`

5. Start a redis via docker:

    `docker run -p 6379:6379 -it redis/redis-stack:latest` 

6. Runserver command:

    `python manage.py runserver`
