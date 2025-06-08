![Running Django on Render](https://github.com/stick35em10/django_app/raw/main/images/running_django_on_render.png)

Deploy a Django App on Render
This guide walks through deploying a Django Python app on Render. You can use your existing Django project or create one from scratch.

![Running Django on Render](django_app/images/running_django_on_render.png)

If you're new to Django, we recommend first reading the official guide to Writing your first Django project.

![Running Django on Render](images/running_django_on_render.png)

Updating an existing Django project
To prepare an existing Django project for production on Render, we'll make a couple adjustments to its configuration:

![Running Django on Render](../images/running_django_on_render.png)

We'll update your project to use a Render PostgreSQL database instead of a SQLite database.
We'll configure the WhiteNoise package to serve your project's static files.
We'll define a build script to run with each deploy.
Use a Render PostgreSQL database
As part of deploying your project, we'll also deploy a Render PostgreSQL database to serve as its backing datastore. To enable this, let's add a couple of packages to your project:

Package	Description
psycopg2	This is the most popular Python adapter for communicating with a PostgreSQL database.
DJ-Database-URL	This enables you to specify your database details via the DATABASE_URL environment variable (you'll obtain your database's URL from the Render Dashboard).
Run the following commands to install these packages:

$ pip install psycopg2-binary

$ pip install dj-database-url

# Add these dependencies to your requirements.txt file:
$ pip freeze > requirements.txt
Open settings.py in your project's main directory (e.g., mysite/settings.py).

Make the following modifications:

# Import dj-database-url at the beginning of the file.
import dj_database_url 
# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://postgres:postgres@localhost:5432/mysite',
        conn_max_age=600
    )
}
Set up static file serving
Django provides a dedicated module for collecting your project's static files (HTML, CSS, JavaScript, images, and so on) into a single place for serving in production. This module supports moving files from one place to another, relying on the end web server (such as Render's default web server, or a tool like NGINX) to serve them to end users.

In this step, we'll set up WhiteNoise to serve these static assets from Render's web server.

The following instructions summarize the setup described in the WhiteNoise documentation.

Add WhiteNoise as a dependency (adding Brotli support is optional, but recommended):

$ pip install 'whitenoise[brotli]'
$ pip freeze > requirements.txt
Open settings.py in your project's main directory (e.g., mysite/settings.py).

Add the following to the MIDDLEWARE list, immediately after SecurityMiddleware:

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    ...
]
Still in settings.py, find the section where static files are configured.

Make the following modifications:

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
STATIC_URL = '/static/'

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
All set! We're ready to serve static content from our Django project on Render.

Create a build script
Whenever you deploy a new version of your project, Render runs a build command to prepare it for production. Let's create a script for Render to run as this build command.

Create a new file called build.sh in your project's root directory and paste in the following:

#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
Make sure the script is executable before adding it to version control:

chmod a+x build.sh
We'll configure Render to run this build script whenever a new deploy is initiated.

We'll run your project with Uvicorn and Gunicorn. Add these dependencies to your project:

pip install gunicorn uvicorn
pip freeze > requirements.txt
Try running your project locally!

Replace mysite in the command below with your project's name.

python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker
Visit http://localhost:8000 in your browser to verify that your project is up and running.

Commit all changes and push them to your repository. Your project is ready to deploy to Render!