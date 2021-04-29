# Data-Science-with-Foursquare-API-
[Project for EE393 Python for Engineers](https://github.com/eminkartci/Company_Competitor_Simulation_Demo/blob/main/EE393_Semester_Project_Map_SimpleGUI_CompanyObject_Version3.ipynb)

### Contributers:

| Name  | Surname   | Student No  | Department  |
|---|---|---|---|
| [Emin](https://www.eminkartci.com)  | Kartci  | S014877  | EE Engineering  |
|Ozan | Yurtsever | S015164 | EE Engineering |
|Yamaç Demirkan| Yılmaz |S018368 |Computer Science|
|Muhammed Ali |Kumaşoğlu| S018505|EE Engineering |

### Member & Task Table

| Emin Kartci  | Ozan Yurtsever   | Muhammed A. Kumaşoğlu  | Yamaç D. Yılmaz  | Egemen İşcan |
|---|---|---|---|---|
|Company Object          | Mapping by using Folium            | Calculation of the distances | README File | Searching Foursquare API |
|Customer Object         | Restricting the user about location                      | Sorting the companies wrt distances | Company Object Financial Calculations | Getting Data from Foursquare |
|Financial Calculations  | Company Input GUI                         | Filtering & Converting Foursquare Output to our objects  | Price vs Cost Plot | Searching Preminum Foursquare API | 
|Financial Plots         | Foursquare Data Request                       | Mapping the companies | Company Comparison Plot | Converting data to csv file |
|Simulation Conditions         | Presenting outputs to the MAP                 | Financial Reports & integrating with mapping | Motivated the team | Reading & Preparing Data |
|Company Inputs GUI         | Customer Class                    | - | Searching Foursquare API Output | Trade Simulation |
|PV & FV Analysis - GUI         | -                | - | - | Integrating the codes |
|ReadME         |-                               | - | - | - |
|Creating Support&Decision Reports         | -     | - | - |- |
|Saving Support&Decision Reports         | -       | - | - |- |
|Demonstrating Sample Case        | -              | - | - |- |

In this project we have tried to demonstrate our **data analysis, stochastic simulation and map creation skills** with Python. In order to achieve this task, we obtained coffee shop data from the **Foursquare Places API**. Then we created various hypotethical scenarios to create some business problems and solve them.

We shall now briefly explain how each and every one of the files in the project repository function, one by one.

## Company.py 

In this class, we describe all the functionalities of a real company like its name, location, sales volume etc. Then, **we implemented all the necessary functions to prepare an income statement of the company**. Also, we can determine its **break-even point, present value and future value with additional functions we have implemented**. Overall, one can understand what would it take establish a company from scratch with high-precision statistics and information.

### DETAILED EXPLANATION ARE PROVIDED AT THE FILE

## Customer.py

In this class, we define all the attributes and functionalities of a real customer.**We give an ID to represent each distinct customer, then we set their location, cash and range to the relevant company on a random basis**.

### DETAILED EXPLANATION ARE PROVIDED AT THE FILE

## datacollection_api.ipynb

Using the Foursquare Places API, we have come up with a large dataset which we can analyze and synthesize. We chose New York as our target city to work on. Then, we got the **venues in New York in JSON format**, parsed them and come up with a very large DataFrame. As a result, we have turned this **DataFrame to a CSV file** to use it in other classes.

## EE393_Semester_Project_Map_SimpleGUI_CompanyObject_Version3.ipynb

This class is actually a **graphical user interface** which contains the **attributes and a general report** of a company. It **displays everything in the Company.py in a GUI**.

### DETAILED EXPLANATION ARE PROVIDED AT THE FILE

## GetClosestCompanies.py

This class uses **Distance.ipynb** which we implemented in a seperate file. In this class, we get a set of inputs from the user as latitude and longitude. Once we get them, according to the set of input, **we come up with the nearest companies to that specific latitude and longitude** and **print their name, latitude, longitude and the calculated distance to the set of latitude and longitude the user entered.

### DETAILED EXPLANATION ARE PROVIDED AT THE FILE

## Map.py

It represents the visualization of the found possible **"rival"** companies.

### THIS FILE IS CONNECTED WITH EE393_Semester_Project_Map_SimpleGUI_CompanyObject_Version3.ipynb IPYNPFILE

## Near_Class.ipynb 

It **prints all the necessary information about the possible "rival" companies** like their tip count, their photo count on the Web, their ratings, their likes etc.

### THIS FILE IS CONNECTED WITH EE393_Semester_Project_Map_SimpleGUI_CompanyObject_Version2.ipynb IPYNPFILE

## SimulationExecution.py

It executes the **simulation based on default competitors**.From that, it **calculates and prints the companies, creates the customers in a random manner, and plots the break-even point to guide the user whether to establish such a company in these circumstances or not**.


## SimulationLibrary.py

It contains all the necessary implementations of the simulation environment such as **defining the competitors, creating the customers, calculating the distances between "rival" companies, creating the customer choices** etc.

## newyorkcoffeewithdetails.csv
It contains the **CSV as a result of datacollection_api.ipynb**.



