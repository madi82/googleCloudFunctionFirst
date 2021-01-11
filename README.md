# serverless
For this project we will use below tools
1. Pycharm
2. Github Desktop
3. Firbase Console
4. Google Cloud Functions

First run command to see python version
``python3 -V``

#Create virtual envirnment now
First we have to install `python3-venv` with following commands

Use below command to create virtual env
``python3 -m venv virtualenv``

We need to activate virtual envirnment by following command 
``source virtualenv/bin/activate``

Then, we can add dependencies (packages) by putting them
in a `requirements.txt` file and we then install them with:
```
pip install -r requirements.txt
```
To run function locally we need to navigate inside folder
```
cd helloworld/
```
Now run below command 
```
functions-framework --target hello_world
```
Now you can test it by hitting below 
```
http://0.0.0.0:8080/?name=Shantanu&lastname=Madiwale
http://0.0.0.0:8080/
```
For closing running app
```
control^ c
```

We can use postman json file to import in postman and use it for testing, also if you update anything re-export and save it.
## Check if you have gcloud configured and setupped to your google account, if not refere below video
```
https://www.youtube.com/watch?v=k-8qFh8EfFA
```



