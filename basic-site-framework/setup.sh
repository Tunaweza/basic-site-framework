python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata pages.json
python manage.py loaddata blog.json
python manage.py loaddata menu.json
python manage.py loaddata snippets.json
cd staticwork/
bower install
cd ..
python manage.py collectstatic
