# How to user docker to containerize python application?
## Example 1
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
docker buid -t iris-container .
```
 Now you can uninstall the packages from your computer  
 and the program from docker container