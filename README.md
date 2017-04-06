# Basic Site Framework

A basic platform based on Django for powering a website. It has very minimal CMS capabilities.

## Features:
 - Bootstrap integration
 - DB driven menu with auto "active" menu items.
 - Basic blog with list and post views
 - Basic page manager with auto routing based on slugs
 - Custom django template tags for meta data, menu listing, content presentation, content lists, and position and route based widgets.

# Setup and Configuration

1. Download the package from github.
2. Install postgres if you do not already have it installed.
3. Create a postgres database for the site.
4. Update the basic-site-framework/basic-site-framework/settings.py file to include the database connection settings.
5. Install bower, Python 3, pip3 with you OS package manager.
6. Install virtualenv with pip3 `pip3 install virtualenv`
7. Create a virtualenv `virtualenv venv --python=python3`
8. Activate the virtualenv `source venv/bin/activate`
9. Install the required python libraries `pip3 install -r requirements.txt`
10. Migrate the database and install the base data `python manage.py migrate` from the base-site-framework/base-site-framework directory
11. Create a super user for the site `python manage.py createsuperuser`
12. Go to base-site-framework/staticwork and run `bower install`
13. Collect the static js, css, and image files with `python manage.py collectstatic`
14. Set up a web hosting deamon for the django app, or run the app in dev mode by changing `DEBUG=False` to `DEBUG=True` in settings.py


### NOTES
Setup steps 10-13 can be completed by running the `./setup.sh` script, it will automatically insert dummy data too.