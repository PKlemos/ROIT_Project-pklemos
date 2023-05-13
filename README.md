###**Project Description**###

The purpose of this project is to extract information from sections A, B, and C of the CNAE (National Classification of Economic Activities) from the IBGE (Brazilian Institute of Geography and Statistics) website, save this information in an excel file, and then process this data into a table using a Python script.

The Python script is written in version 3.10 and requires the openpyxl and unidecode libraries to function properly.

There is a folder called API within the project that contains a Python API capable of reading the data from the excel file and writing it to a SQLite database through the "/insert_data" endpoint. The API also allows for data retrieval through the "/view_data" endpoint. The flask and openpyxl libraries are required for the API to function properly.

##**API**##

#**/insert_data**#

This endpoint accepts POST requests with an excel file containing data to be inserted into the database. 

#**/view_data**#

This endpoint accepts GET requests and returns a JSON response containing all data from the database.

##**Requirements**##

*Python 3.10
*openpyxl
*unidecode
*flask
