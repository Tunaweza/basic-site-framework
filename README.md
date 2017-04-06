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
5. Install npm, Python 3, pip3 with you OS package manager.
6. Install bower with npm `sudo npm install bower -g`
7. Install virtualenv with pip3 `pip3 install virtualenv`
8. Create a virtualenv `virtualenv venv --python=python3`
9. Activate the virtualenv `source venv/bin/activate`
10. Install the required python libraries `pip3 install -r requirements.txt`
11. Migrate the database and install the base data `python manage.py migrate` from the base-site-framework/base-site-framework directory
12. Create a super user for the site `python manage.py createsuperuser`
13. Go to base-site-framework/staticwork and run `bower install`
14. Collect the static js, css, and image files with `python manage.py collectstatic`
15. Set up a web hosting deamon for the django app, or run the app in dev mode by changing `DEBUG=False` to `DEBUG=True` in settings.py


### NOTES
Setup steps 10-14 can be completed by running the `./setup.sh` script, it will automatically insert dummy data too.


# Menu
Menus can be created and displayed any where in a template. Menu items are attached to a menu and orderable, also menu items can have permissions such as public, admin only, logged in, and not logged in.

When created a menu item choose the menu that it belongs to, enter a title for the menu item that will be displayed as the link text, enter the route for the menu item, and choose the menu item visibility permissions.

Menu items will automatically have the `active` class added to the parent li when their link matches the current route.

# Pages
Pages are simply items that have a page title and content. Pages also can display meta information such as keywords, description, and author.

When creating a page enter a title for the page, a slug which will be used for the link in automatic link generation for SEO friendly urls, meta data, and page content in HTML.

Slugs should always be lowercase, alphanumaric and use `-` for ` `(spaces). 

The default routes for pages will always be the toplevel of the domain/id-slug/

example: `example.com/1-first-page`

The the id and slug for the menu routes followed by a trailing `/`.

# Blog
The blog is a very basic colection of posts.

When creating a blog post enter the title, slug, meta data, and content in the same manner as pages.

The only real difference between blog posts and pages is that the blog list page will show a list of posts.

# Snippets
Snippets are widgets that can be dislpayed on pages based upon routes and positions.

To posisiton a snippet enter the position name from one of the predefined posistions below.

 - left\_content\_col - displayed to the left of the main page content.
 - right\_content\_col - displayed to the right of the main page content.
 - jumbotron - displayed above the content at full page width
