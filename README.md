# How to user docker to containerize python application?
## Example 1: using the telnet
### In order to do containerization docker should be preinstalled and running.
Run the `main.py` that 
> Note: telnet is deprecated feature or insecure to enable it on windows:
> * search feature
> * select `telnet` and click ok
>>This is just for demonstration purposes.
### Run the following in windows cmd
```shell
telnet 127.0.0.1 9997
```
you will see the first column of the iris data.
### Now run the following to build the container
```shell
docker build -t iris-container .
```
 Now you can uninstall the packages from your computer  
 and run the program from docker container by following cmd.
 ```shell
 docker run -p 9997:9997 iris-container
 ```
See results from docker container
```shell
telnet 127.0.0.1 9997
```
You can deactivate the telnet.
## Example 2: FastAPI
> create `main.py` and run it from local computer
### now, we will run from docker container
1. create `requirements.txt`
2. create `Dockerfile`
3. build the container 
```shell
docker build -t fast-api .
```
4. run the container
```shell
docker run -p 8000:8000 fast-api
```
5. you can also rename the container name by port
```shell
docker run -p 8000:8000 --name fastapi-container fast-api
```
> where `fast-api` is image name\
> and `fastapi-container` is the container name.
> switch to `127.0.0.1:8000` to see result
