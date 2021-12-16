In addition to these assumptions:

   - the service is already running at the moment your tests executed(on port 8080)(Go to the parent folder in src folder and read the readme file on how to start the service)
   - tests are running on the same machine

in the last test, it has been assumed that we have at least one process that has threads more than 5. Otherwise, the test would fail.

Tests are run within a docker container. Therefore, make sure docker is up and running by:

```shell script
docker --version
   ```     
In case you need to install it, please see https://docs.docker.com/get-docker/.

To run tests:

   1. Go to psweb-solution directory and build the docker image by:
     
```shell script
docker build -t test-image .
   ```     
   
   2. Start the docker container:

```shell script
docker run -it --name test-container --rm test-image
   ```    

   3. Then, run tests inside the docker container:

```shell script
pytest tests/
   ```    

NOTE: It has been only tried to build an MVP as quick as possible. I didn't put time to write helper methods nor integrating a test report.

I am really happy that I didn't put so much time on this challenge. Because exactly the moment I wanted to integrate a test report like https://reportportal.io/, this thought passed my mind that what if the person who wants to run these tests does not understand anything about docker!!? 
And this exactly happened, I was told that they were not able to run these tests :)). Anyway good for me!
