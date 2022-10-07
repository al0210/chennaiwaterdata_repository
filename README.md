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


**Build Instructions**


**List of dependencies**


