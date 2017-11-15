# django-react-template
This repo is used to document my progress as I learn to hook react.js up with the django framework

- [Objective](#objective)
- [Babel](#babel)
- [Webpack](#webpack)
- [Redux](#redux)
- [Installing on Ubuntu](#installing-on-ubuntu)
- [Deploying on Ubuntu](#deploying-on-ubuntu)
- [Managing Multiple Django Settings](#managing-multiple-django-settings)
- [Managing Multiple Webpack Configs](#managing-multiple-webpack-configs)
- [Keeping Production Passwords Out of Source Control](#keeping-production-passwords-out-of-source-control)
- [TODO](#todo)

# Objective
When learning react I used create-react-app to automatically generate a project for me. I realized that while I was able to learn React, I wasn't exactly sure of what Babel or Webpack did. This led to issues when trying to incorporate a Django backend into an existing React app I had written. So the purpose of this repo is to document my progress as I learn what Babel/Webpack do, how to configure them, and how to hook up react.js with Django and will hopefully serve as a reference to anyone else in a similar situation. The end result of this repo should be a small sample web application using Django, Django Rest Framework, and React.js that users can use as a reference point when creating apps with a similar stack.

Notes: I realize that with enough googling, I could probably find a repo or vm instance that has a preset sample application, but I think it's necessary to always try to understand the tech you're using.


# Babel

Babel is a package that transforms ES6 (new javascript) into JS compatible with current browsers. Using babel plugins, babel can support numerous build/test systems.

## Babel packages used

    .babel-core // main babel node library
    .babel-loader // babel plugin for support w/ webpack
    .babel-plugin-react-transform // support for react
    .babel-plugin-transform-class-properties // support for class properties in react
    .babel-preset-es2015 // support for es2015 features, preset compiles all dependencies together, rather than installing one by one
    .babel-preset-react // support for react, jsx
    .babel-preset-stage-0 // support for new features that are not yet finalized, stage 0 is the earliest stage, 3 being the last and closest to being accepted into standard


# Webpack

Webpack is a module bundler for front-end applications. It puts all assets into a dependency graph, from which you can reference those assets in your application. Webpack has been adopted as the main build tool by the React dev community. It replaces the need for inserting all scripts manually into your templates:

And also replaces bundling css, js, etc. using grunt (although it does not replace grunt completely as bundling css, js is not the only thing grunt is for).

For more in depth information I would recommend reading [Webpack Concepts](https://webpack.js.org/concepts/)

# Redux

At its core, Redux helps manage state in Single Page Applications by preventing different parts of the code from mutating the page model state directly. By using concepts called Actions and Reducers, parts of the page create a traceable Action object that gets sent to a Reducer which returns the new state of the model, based on the Action object.

Redux accomplishes this through its three principles:

1. State has a single source of truth
2. State is read only
3. Changes to the state are through pure function

### Is Redux necessary?

While Redux can help immensely in managing state for complex Single Page Applications, it is not necessary for all apps. Simple RSS reader applications, or 'read-only' applications like a blog website may not need Redux to manage its state because the state can only be changed by a small number of sources. However, because Redux works so nicely with React it may be worth looking into incorporating into your web apps when you anticipate your application becoming more complex and needing to scale in the future.

### Redux Resources

[Redux Page](http://redux.js.org/)

[Redux with React](http://redux.js.org/docs/basics/UsageWithReact.html)

[You Might Not Need Redux by Dan Abramov](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367)

# Installing on ubuntu
These steps assume you have a fresh ubuntu server

1. Update and upgrade ubuntu packges:

 `sudo apt-get update`
 `sudo apt-get upgrade`

2. Install node from correct distribution:

  Follow instructions at https://github.com/nodesource/distributions#debinstall

 - Ubuntu has an old version of node in its package manager, so installing from the proper distribution gives us the updated version of node

3. Install pip:
 `sudo apt-get install python-pip`

4. Install virtualenv with pip:
 `sudo pip install virtualenv`

5. Create a virtualenv for this project:
 `virtualenv projectname`

6. Install git and clone this repo

 `sudo apt-get install git`

 `git clone https://github.com/Arjay123/django-react-playground.git`

7. Navigate to root directory of project and install packages from requirements.txt:
 `pip install -r requirements.txt`

8. Navigate to app directory Install npm packages from package.json:
`npm install`

9. Make django database migrations:

 `python manage.py makemigrations`
`python manage.py migrate --run-syncdb`

10. Seed database with sample data using custom command:
`python manage.py database_init`

11. Run django dev server:
`python manage.py runserver 0.0.0.0:8000`

12. Run webpack watch:
`npm run watch`

13. Check that you can access the server at `SERVER.IP.ADDRESS:8000` in your web browser

# Deploying on Ubuntu

For deployment to an ubuntu server I would recommend switching the database engine from SQLite to PostgreSQL, follow this [tutorial]( https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04). 

Note that when switching over from SQLite to PostgreSQL, I ran into an issue when migrating the database. To solve this, I ran the migrate command with a --run-syncdb argument.
`python manage.py migrate --run-syncdb`

[More info on --run-syncdb](https://docs.djangoproject.com/en/1.11/ref/django-admin/)


### Apache

I use apache with mod_wsgi to deploy my projects, reference the [Django Docs](https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/modwsgi/) for more info on how to set up your apache config file. See [apache_config](apache_config) for an example on how to set up your Apache config file to work with Django and Virtualenv.

### Bundling and Serving React

To bundle your React.js app, using the npm commands specified in [package.json](app/package.json). For production, use `npm run build`, and for staging use `npm run stage`.

Then collect your files into Django's static folder using `python manage.py collectstatic`

This allows your React app to be served by Apache.

# Managing Multiple Django Settings

While I was trying to deploy my Django application on a staging server, I noticed I had to change a lot of my development settings in order to get it to work (i.e. DEBUG=False, ALLOWED_HOSTS, etc.). Then when going back to development mode I had to change these settings back, which was wildly inconvenient. However, I came across a solution in the book [Two Scoops of Django](https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342) which used multiple settings files (development, production, staging, etc). 

In order to use the different settings files from the command line, you simply specify the path to your settings file as an argument.
`python manage.py test --settings app.settings.dev_settings`
Combining all the settings files in a [settings](app/app/settings) directory provides a little bit of organization as well.

### NOTE:

When using multiple settings files in deployment, you will need to specify in [wsgi.py](app/app/wsgi.py) which files to use by setting the environment variable `DJANGO_SETTINGS_MODULE`


# Managing Multiple Webpack Configs

Similarly, there are settings that need to be changed when changing environments. Creating multiple [webpack](app/webpack) configs solves this problem. In order to select which config file to use, add the argument --config PATHTOCONFIGFILE. You can even add this argument into your [package.json](app/package.json) file and run the npm commands from the terminal without having to specify which config file every time.

One example of the benefits of separating your config files is specifying the API_URL base your React app will reference. In my [development](app/webpack/dev.config.js) file, my API_URL uses localhost/127.0.0.1, where as in my [production](app/webpack/prod.config.js) settings I would use the domain name of my web application.

# Keeping Production Passwords Out of Source Control

An easy way to do this is to create a local file with your production secrets and add it to the .gitignore file. For example in my [Django Production Settings](app/app/settings/prod_settings.py), I pull my PostgresSQL password from a local file.

# TODO
- [x] DjangoCon US 2016 - Django and React: Perfect Together by Jack McCloy: https://www.youtube.com/watch?v=zYHv6U86X0Y

> I watched this talk to get a baseline idea of how Django hooks up to React and take notes on things that I need to learn further before attemping to create my own app.

- [x] What is Babel?
- [x] What is Webpack?
- [x] What is Redux, is it needed for django-react?
- [x] Create Djano Rest Framework sample app
- [x] Install instructions
- [x] Deployment
- [x] Deployment sample files
- [x] Managing multiple Django Settings
- [x] Managing multiple Webpack Configs
- [x] Keeping secrets out of source control
