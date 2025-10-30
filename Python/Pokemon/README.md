## v0.5

Updated the app to now connect to an external Postgres database running on another container.

To run successfully, both the pokemon container and the postgresql container need to be running.



## v0.4

Updated the app to now run with Docker - run the below to run the image.


docker run --rm -p 5000:5000 pokemon-web:latest 

## v0.3

Updated the app so that it now a web app running on flask. Pokemon which are retrieved are now stored on a database. Removed the docker file as it has not yet been implemented.
- Changed to a web app running on flask
- Data is now stored in a local sqlite database


## v0.2

The app was configured to run as a docker file.
- Added a dockerfile


## v0.1

This is a simple program which connects to the pokemon API and retrieves a random pokemon.

The response is formatted and written to a file.