## v0.4

I have implemented this now on Docker - run the below to run the image.

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