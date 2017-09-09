# Python RESTful api with Domain Driven Design

This repository contains a python restful api with the following features:
+ Swagger Documentation
+ Jinja templates for REST/Json standard
+ Falcon + gunicorn for http server
+ Pony orm for relational data
+ All configs via environment variables
+ Dependency injection for configs, etc.
+ Docker ready

## Run the project
After cloning the repository, just run: `make server`

To stop the server, run: `make stop`

To share your mysql data with someone else, run the `make backup` command while server is running:
