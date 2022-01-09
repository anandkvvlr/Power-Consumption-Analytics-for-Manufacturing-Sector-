#     Power-Consumption-Analytics-for-Manufacturing-Sector-
## Project Background
### Energy Management 
Energy Management is the process of tracking and optimizing energy consumption to conserve usage in the Industry. Energy consumption by various units are monitored timely and the valuable insights helps in understanding the pattern and hence timely user intervention can save a lot of energy.
### Overview of Beverage Industry
The beverage Industry also known as drink industry is the one which manufactures drinks. It produces alcoholic such as distilled spirits, wine and brewing as well as non-alcoholic drinks such as fruit juices, tea or coffee and other flavored drinks etc.

### Benefits of Energy Management in Beverage Industry
  It increases overall productivity of the manufacturing plant.
  It helps to detect malfunctioning electrical devices timely.     
  It is eco-friendly practice so makes the technology more constructive.

### Aim:
⮚	Main aim of this project is to manage the energy consumption by the overall plant
⮚	To monitor the energy consumption on real time basis by individual plant units and overall plant using IoT sensor.
⮚	To find whether at any instance energy consumption is low or high
⮚	To find whether all the electric motors are working at optimum performance.
⮚	To minimize power losses and overloading

### Business objective:
⮚	Minimize: Energy losses, overloading  
⮚	Maximize: Energy efficiency
Business Constraint:
⮚	To improve the performance of large amounts of data.
⮚	Security of the data and working of the IoT sensor.

### Flow of process in Beverage Plant:
![image](https://user-images.githubusercontent.com/88075268/148675787-eff7a993-54d0-406a-afec-007e2035ec2f.png)

### Project Dataset:
Data is collected on real time basis with the help of IoT sensor installed in the various electric motors in each of unit of the manufacturing plant. For every 10 seconds the data of energy consumption by all these individual units is obtained from the IoT sensor.
•	Calculation = ((energy in kWh x 1000)/60 x 60) x 10 
Electrical Energy consumed by individual motors installed in individual unit of the production system acts as independent variables and another meter is installed at the outlet of production system that measures overall electricity consumption acts as a target variable.

The features present in the data are:
![image](https://user-images.githubusercontent.com/88075268/148675822-d049a196-b48c-4a24-bfd4-e9b6380a6437.png)

##     INITIATION AND DATA PREPARATION
### High level Flowchart of the process:
![image](https://user-images.githubusercontent.com/88075268/148675858-0dc1511d-69fb-47cc-b6ee-1c08f4a9db0c.png)

### Detailed Project Architecture:
![image](https://user-images.githubusercontent.com/88075268/148675885-b14145ac-a8cb-4e8c-8978-a3836ef261bb.png)

# Data Preparation:
This preprocessing step involves exploratory data analysis, data visualization, checking null and duplicate values, outlier treatment , removing undesirable nominal features such as “Timestamp” and usage of binning to convert output variable “allplant” into categorical variable so that data can be made to be used for classification model.

# Exploratory Data Analysis:
This step is used to identify and summarize the main characteristics in a data set through data analysis and investigation. We used data visualizations to better understand how best to manipulate data sources, to determine which statistical techniques are most appropriate for data analysis, and for choosing the right features for a model.
EDA includes fallowing steps:
	Details About Data
	Data cleaning 
	Statistical Insights 
	Univariate analysis 
	Bi-variate/Multivariate analysis
# Data Cleansing:
●	Nominal Features: The “Timestamp” is just nominal data which is only showing the timestamp of the monitoring and as no relevance with other features, so it is removed from the dataset.
●	Missing Values: There are no missing values and null values in the dataset.
●	Outliers: Here in this Dataset, There are outliers in the features like “RCM” and “allplant” so the outliers were replaced with the max threshold of the feature.
●	Binning: The target variable “allplant” is continuous data and to make the data compatible to classification problem it is then converted to categorical by the concept of binning. “allplant” is converted into two categories namely high and low. From 250 to 358 watts per 10 seconds is treated as one category i.e. low consumption and from 358 watts per 10 seconds onwards it is treated as another category i.e. high consumption

# Statistical Insights: 

Below is the count, mean, standard deviation, minimum and maximum values and the quantiles of the data.
![image](https://user-images.githubusercontent.com/88075268/148676308-f16c2100-1f3a-4328-9d94-faaede474e1b.png)
	There is not much difference between 75th %tile and max values.
	Thus observations suggests that there is no Outliers in our data set.


