# ML-predictions
Alec H, Andrew P, Celena B, Dan T, Vilma D.

A full-stack, hosted application that predicts a vehicle's price.


# Intro

The purpose of this project was to develop a machine learning model with a real world application. For this we started with a dataset containing almost six million car entries scraped from the CIS auto website, developed a model on the cleaned data and used Flask and HMTL to allow users to interact with and recieve estimations of car value based on the Model Predictions.


# Data Set 

![CIS_Automotive_Sample](https://www.kaggle.com/cisautomotiveapi/large-car-dataset)


### COLUMNS

'body_class' - If the vehicle was a Sedan, Truck, or SUV.

'brand_name' - The manufacturer of the Vehicle

'model_name' - The Model of the Vehicle

'model_ID' - A unique ID for the Model

'model_year' - The year of Manufacture

'mileage' - Mileage at the time of Sale

'ask_price' - Price listed for sale

'msrp' - Manufacturer Suggested Retail Price

'color' - color

'engine_cylinders' - Number of cylinders

'fuel_type_primary' - Gas/Diesel

**====== Target ======**

'ask_price' - Price listed for sale

# Method

First step was to clean the information and in doing so we ended up with a sample of 400,000 entries across all three body classes.
Correlation matrices were made for the data as a whole and then for each Manufacturer. The data as a whole produced little correlation. It was after observing the weights assigned through the training of the model that we were able to see just how important some columns were to calculating the overall ask price of a vehicle.

![All Body Type Corr](visualizations/full_data_correlation.png)

Initially a model was trained using all data with an accuracy of 78%, however after noticing the change in correlation weight three models were produced, each trained on all of the data matching one of three bodyclasses. Each indidual model tested higher when allowed to train over data particular to it's own bodyclass.

Once the models were produced, a front end web page was set up to allow for data to be recieved from the user. Afterwards, a flask app was developed to load in the information that would be needed to evaluate the user data per model based on the user-input. 



#### Pre-Processing:

discuss columns removed and why. see top 10 features of graph, discuss 12 day timeline and restrictions due to time



## +++++++++++++++++++++++++++ Model +++++++++++++++++++++++++++

discuss the model used, perameters accuracy and steps taken to achieve model

consider possible changes to improve model
more data, more features, etc

# Analysis
## Results:

list the model results either using snipped photos or type it out

# Conclusion

EDIT THIS - IT IS FROM A DIFFERENT PROJECT

EDIT THIS - IT IS FROM A DIFFERENT PROJECT

EDIT THIS - IT IS FROM A DIFFERENT PROJECT

EDIT THIS - IT IS FROM A DIFFERENT PROJECT

A surprising outcome of this project was seeign that the most accurate model was much simplier than the initial User_model containing much fewer neurons, but keeping with the 3 layer construction.

One of the aspects of machine learning is testing models with just the right hyperparameters. Unsurprisingly the model that had the most tuning proved to show the highest accuracy and lowest loss, however the varaition of those values between the models is very slight and lacks significance. Taking the time to construct a means of hypertuning and comparing results per epoch of model with differing activation fuctions, layers, and neurons will always be preferred to an educated guess when defining model complexity because the iterative changes can be observed as the model tests data and the process will be much more time-efficient when compared to hand tuning.
Guesses, even when educated can make for a nice starting point when considering complexity but should be pared with adequate reasoning to avoid the wasting of resources.



