### Prediction of Placement Result

#### Overview 

In this project, we'll look at the placements record and try to build a classifier to predict whether a given profile likely to be get placed or not.

#### Data used

Placement_Data_Full_Class.csv - Download from kaggle datasets (https://www.kaggle.com/sevdanurgenc/placement-data-full-class)

#### Data Description

##### Shape - (215, 15)

##### Data columns (total 15 columns):
sl_no - int64<br>
gender -  object<br>
ssc_p - float64<br>
ssc_b - object<br>
hsc_p - float64<br>
hsc_b - object<br>
hsc_s - object<br>
degree_p - float64<br>
degree_t - object<br>
workex - object<br>
etest_p - float64<br>
specialisation - object<br>
mba_p - float64<br>
status - object<br>
salary -float64<br>

#### Folders

* /app/ - Python files for the deployment of the trained machine learning model as an API using `FastAPI( )`
* /model/ - Jupyter Notebook for training the model and the trained model in pickle format
* /Data/ - Data used for training the model in csv format

#### Install the required packages

> pip install -r requirements.txt

#### To start the API server

> python ./app/app.py

Now open the browser and open http://localhost:8000/docs or http:/127.0.0.1:8000/docs

It will display the Swagger UI Homepage as below: 

![Screenshot (37)](https://user-images.githubusercontent.com/22251571/133881964-04760d0a-4056-4b0a-89c1-66f2970e0f12.png)
![Screenshot (38)](https://user-images.githubusercontent.com/22251571/133881970-c8d868ab-d1ff-410e-b2f9-d93ac5d8ac2e.png)
![Screenshot (39)](https://user-images.githubusercontent.com/22251571/133881971-174b9a7b-c8e5-4923-a015-5dc6e5da1389.png)

