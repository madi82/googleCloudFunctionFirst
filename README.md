# serverless
For this project we will use below tools
1. Pycharm
2. Postman
3. Github Desktop
4. Firbase Console - Firestore
5. GCP- Google Cloud Functions

First run command to see python version
``python3 -V``

# Create virtual environment now
First we have to install `python3-venv` with following commands

Use below command to create virtual env
```
python3 -m venv venv
```

We need to activate virtual envirnment by following command 
```
source venv/bin/activate
```

Then, we can add dependencies (packages) by putting them
in a `dev_requirements.txt` file and we then install them with:
```
pip install -r dev_requirements.txt
```
To run function locally we need to navigate inside folder
```
cd helloworld/
```
Now run below command 
```
functions-framework --target hello_world --debug
```
For closing running app
```
control^ c
```
# Now you can test it by importing postman json file into postman
```
../googleCloudFunctionFirst/googleCloudFunctionFirst.postman_collection.json
```




