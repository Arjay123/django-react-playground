# django-react-playground
This repo is used to document my progress as I learn to hook react.js up with the django framework

- [Objective](#objective)
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

# TODO
- [x] DjangoCon US 2016 - Django and React: Perfect Together by Jack McCloy: https://www.youtube.com/watch?v=zYHv6U86X0Y

> I watched this talk to get a baseline idea of how Django hooks up to React and take notes on things that I need to learn further before attemping to create my own app.

- [x] What is Babel?
- [x] What is Webpack?
- [ ] What is Redux, is it needed for django-react?
- [x] Create Djano Rest Framework sample app
- [ ] What is django-webpack-loader?
- [x] Install instructions
