We have a little web service for monitoring processes on a remote machine. Web service provides the following endpoints:

   - **/processes** - returns a list of running processes with information about memory consumption % and number of running threads, 
   the endpoint accepts query string arguments **mem-above** and/or **threads-above**, 
   when **mem-above** is provided the endpoint returns only those processes that have memory consumption above the specified number, 
   when **threads-above** is provided the endpoint returns only those processes which number of threads exceedes the number specified. 
   The service can accept both of the arguments in the same request and will combine them with logical AND.
   - **/processes/\<pid\>** - returns information for the process with a given **\<pid\>**
   - **/processes/\<pid\>/kill** - accepts POST requests and terminates the process with a given **\<pid\>**

Please, write end-to-end tests to verify that service is functioning correctly. You can assume the following while writing tests:

   - the service is already running at the moment your tests executed
   - tests are running on the same machine

If you make other assumptions, please, let us know about them when you send us a solution.

We prefer a cross-platform solution, but we aware that working with processes could be different from platform to platform, 
so in case your implementation is platform-dependend, please, let us know the platform when you send us a solution.

To launch the service:

   1. Install dependencies:
     
```shell script
pip install -r requirements.txt
   ```     
   
   2. Run the service:
   
```shell script
python3 psweb.py
   ```    

You can access the service at ```http://localhost:8080```


>>>>>>>>>>>>> The above has been writen by Holoplot <<<<<<<<<<<<<<
Now if you don't want to install python and its required library and just interested to see how to start this app, please try below:
To build the image, run:
```shell script
docker build -t psweb-app-image:0.1 .
   ```  
Then, you should have an image with this name: psweb-app-image. To run it:
```shell script
docker run -p 8080:8080 --name psweb-app psweb-app-image:0.1
   ```  
Then, open http://localhost:8080/ on your browser to see how this app works.
