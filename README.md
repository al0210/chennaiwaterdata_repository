# Chennai Water Data


**Project Description**

The project involves collecting, parsing, cleaning and visualizing data using a number of methods with Python programming at its core. The topic of interest was Chennai's Water Data collected from the government website, Chennai Metro Water. The focus was towards collecting two types of data - rainfall data and lake level data of reservoirs. The next step was to store the data into a database before displaying the data and visualizing it using an appropriate chart. The data was queried to understand some of what could be understood from the information it gives. 

The data was collected from https://chennaimetrowater.tn.gov.in/ with the use of web scraping through Python. The python package - BeautifulSoup was used to parse the information from the data web pages. The library pandas was used to create data frames to store the data temporarily before being written into a .csv file. Similar programs were written to collect all the required data from the website. 

Seven .csv files were created post web scraping - one containing the lake level data accross all the five main reservoirs (Poondi, Cholavaram, Red Hills, Chembarambakkam and Veeranam) in the month of December every year, one containing the monthly rainfall level in Chennai, and five files containing the monthly lake level data of each of the five aforementioned reservoirs. Each of these datasets gave corresponding information from the year 2003 till 2021. 

The csv files were further read, connected and stored into a MySQL database. The libraries MySQLdb and mysql.connector were used in ensuring this process. Each of the seven databases were inserted into the database schema in MySQL. An eigth table was also created in the database schema containing the sum of the total rainfall and total lake level in each year. This was done for the sake of querying the data. 

The micro web framework flask was imported into python in order to help create the required web interface. The databases were connected again to the program using mysql.connector before the application were defined and created using flask. The html and css codes were simultaneously written to design the web application and display the project outputs. The values returned from the python program was collected in the html code using Jinja2 Engine. The data was further visualized in the web interface using chart.js.

The home page of the application contains a brief description of the website and the links for each of the other pages. There are eight other pages - seven for displaying and visualizing each of the tables stored in the database, and one for the query mechanism. The data visualization is represented in the form of bar charts which were formed in the backend with the help of Chart-js. 

Overall, the web application is a good start and there is room for a lot of improvements and additions. 



**Directory Structure**

The directory contains five folders with all the project documents and one README file which contains the guide to the project. The following is a brief description of each component in the directory. 

**1. Database** - This folder contains a .sql file - chennaiwater_db.sql - containing all the databases developed and used during the course of the project. 

**2. Datastore** - This folder contains 15 files in all - 8 .py files and 7 .csv files. The .py files contain the codes which were developed to write the data into the database schema. The .csv files are the ones from which the data was read into the .py files before connecting with the mysql database. 

i) Lake Level Yearly MySQL.py - Contains the code which was used to develop the database table - 	table_yearlylakelevels

ii) Lake Levels Monthly Chembarambakkam MySQL.py - Contains the code which was used to develop the database table - 	table_chembarambakkam_monthlylakelevel

iii) Lake Levels Monthly Cholavaram MySQL.py - Contains the code which was used to develop the database table - 	table_cholavaram_monthlylakelevel

iv) Lake Levels Monthly Poondi MySQL.py - Contains the code which was used to develop the database table - 	table_poondi_monthlylakelevel

v) Lake Levels Monthly Red Hills MySQL.py - Contains the code which was used to develop the database table - 	table_redhills_monthlylakelevel

vi) Lake Levels Monthly Veeranam MySQL.py - Contains the code which was used to develop the database table - 	table_veeranam_monthlylakelevel

vii) Monthly Lake Level Chembarambakkam.csv - Contains the data of monthly lake level in the reservoir Chembarambakkam

viii) Monthly Lake Level Cholavaram.csv - Contains the data of monthly lake level in the reservoir Cholavaram

ix) Monthly Lake Level Poondi.csv - Contains the data of monthly lake level in the reservoir Poondi

x) Monthly Lake Level Red Hills.csv - Contains the data of monthly lake level in the reservoir Red Hills

xi) Monthly Lake Level Veeranam.csv - Contains the data of monthly lake level in the reservoir Veeranam

xii) Monthly Rainfall Level MySQL.py - Contains the code which was used to develop the database table - 		table_monthlyrainfalllevel

xiii) Monthly Rainfall Level.csv - Contains the data of monthly rainfall level in Chennai

xiv) TableSum MySQL.py - Contains the code which was used to develop the database table - 		table_sum

xv) Yearly Lake Level Reservoirs.csv - Contains the data of yearly lake level (in December) in the reservoirs - Poondi, Cholavaram, Red Hills, Chembarambakkam, Veeranam

**3. Web Interface** - This folder contains the .py file which has the code for the development of the web interface. 

**4. Web Scraper** - This folder contains 14 files - 7 .py files and 7 .csv files. The 7 .csv files are the same files that are also contained in the folder - Datastore. The 7 .py files each contain the code which was developed to scrape data from the web and develop the .csv files. 

i) Lake Levels All.py - Contains the code which was used to scrape the yearly lake level data of five reservoirs and writing them onto the .csv file - Yearly Lake Level Reservoirs.csv

ii) Lake Levels Monthly Chembarambakkam.py - Contains the code which was used to scrape the monthly lake level data of Chembarambakkam reservoir and writing them onto the .csv file - Monthly Lake Level Chembarambakkam.csv

iii) Lake Levels Monthly Cholavaram.py - Contains the code which was used to scrape the monthly lake level data of Cholavaram reservoir and writing them onto the .csv file - Monthly Lake Level Cholavaram.csv

iv) Lake Levels Monthly Poondi.py - Contains the code which was used to scrape the monthly lake level data of Poondi reservoir and writing them onto the .csv file - Monthly Lake Level Poondi.csv

v) Lake Levels Monthly Red Hills.py - Contains the code which was used to scrape the monthly lake level data of Red Hills reservoir and writing them onto the .csv file - Monthly Lake Level Red Hills.csv

vi) Lake Levels Monthly Veeranam.py - Contains the code which was used to scrape the monthly lake level data of Veeranam reservoir and writing them onto the .csv file - Monthly Lake Level Veeranam.csv

vii) Rainfall Levels Monthly All.py - Contains the code which was used to scrape the monthly rainfall level data in Chennai and writing them onto the .csv file - Monthly Rainfall Level.csv

**5. templates** - This folder contains all the 9 .html files of the developed web application. 

i) chembarambakkam.html - Contains the code run to develop the page containing information about Chembarambakkam reservoir

ii) cholavaram.html - Contains the code run to develop the page containing information about Cholavaram reservoir

iii) home.html - Contains the code run to develop the page containing information about the home page of the web application

iv) lakelevel.html - Contains the code run to develop the page containing information about the lake levels of the five main reservoirs - Poondi, Cholavaram, Red Hills, Chembarambakkam and Veeranam

v) poondi.html - Contains the code run to develop the page containing information about Poondi reservoir

vi) query.html - Contains the code run to develop the page containing information about queries about the data

vii) rainfall.html - Contains the code run to develop the page containing information about the rainfall level in Chennai

viii) redhills.html - Contains the code run to develop the page containing information about Red Hills reservoir

ix) veeranam.html - Contains the code run to develop the page containing information about Veeranam reservoir

**6. README.md** - Describes the project, the directory structure, build instructions and list of dependencies for running the project. 


**Build Instructions**

This section contains the instructions that one needs to follow in order to run this programs successfully. 

1. First of all, one must require to have python installed and need to run all the given codes in a suitable IDE to develop the project. 

2. MySQL is another pre requisite to have in order to store the data scraped into databses and further use them to show information in the web interfaces. 

3. All the libraries listed in the next sextion - list of dependencies - need to be installed in python before running the respective programs

4. The files being called and accessed like the .csv and .html files need to be present in the required location in order to be accessed while programming. Csv files need to be present in the same folder as the .py files which contain reading from or writing to the .csv. .html files need to be present in the folder 'templates' which Jinja2 Engine needs to process and develop the requirements for the web application. 


**List of dependencies**

1. BeautifulSoup

2. requests

3. pandas

4. MySQLdb or mysql.connector

5. Flask

6. csv (library)


