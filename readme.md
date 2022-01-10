# 淘数据 Scraper
 <hr />
Scraper Bot that scrapes data from 淘数据

## Table of Contents
 <hr />

* [General Info](#general-information)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)

## General Information
This project is part of my intern work at Teng Fuh Holdings Pte. Ltd. This scraper
helps to automate the downloading process for my other project, which is to upload the
downloaded data into a sqlite database for further data analysis. This project currently being
updated, although the program already works. It has allowed me to download 400+ xls files
from [淘数据](https://taosj.com/) automatically, which saves me around 5 to 6 hours of manual work per week on average.

## Features
* Scraper uses Selenium that logs into 淘数据 and downloads the sales figures and revenues of created SKUs within the 'TaoSJ Meta' Directory.
* Links with tf-es-dumping repository which creates a backup of the files in 'tf-es-dumping(TaoSJ Data backup)' before deleting and updating the TaoSJ Data directory in tf-es-dumping repository with the new TaoSJ Data folders

## Screenshots
* Script asks for user confirmation to start the selenium bot to login and scrape from 淘数据 ![Start selenium bot](screenshots/scraping_from_taosj.png?raw=true)
* Selenium bot will atuomatically login to 淘数据 based on user provided credentials and start scraping based on meta files created in 'TaoSJ Meta' Directory ![Selenium bot downloading](screenshots/selenium_bot.png?raw=true)
* Files will then be downloaded into 'TaoSJ Data' Directory, and a print statement will be shown in the console. ![Files downloaded](screenshots/files_downloaded_to_TaoSJ_Data.png?raw=true)
  
## Setup
* Upon cloning the repository, 4 directories need to be created, namely
    * /src/TaoSJ Meta/
    * /src/download-dump/
    * /tf-es-dumping (TaoSJ Data backup)/
    * /src/TaoSJ Data/
* Proceed to config.toml and input the relevant login details for the 淘数据 account. You will have to purchase the service. This is not a free scraper.
* For each product, a xlsx/xls file must be created in the 'TaoSJ Meta' Directory with the information of the product, namely
  * Product Name
  * Product ID
  * Product
  * Brand
  * Category
* Refer to <folder> for sample product information
* Relevant brand folder must also be created in 'TaoSJ Data' Directory, reference the brand and if it is of a different category, a new sub-directory as well
* This path must then be updated in config.toml under file_dest

## Usage
* In order to start the scraper, one has to run the selenium_bot.py file, which will look for all the Product-IDs of the products that you have created in 'TaoSJ Meta' directory, before asking for confirmation to scrape the data
* The scraper will then run until all the available products' revenue data has been downloaded, before asking the user for permission to rename and update the TaoSJ Data folder accordingly
* When ready to update the data in tf-es-dumping, open the tf_es_integration.py folder and run the script, it will create a backup of the data present in tf-es-dumping/TaoSJ Data/, before deleting and copying over the updated information
* This will then allow you to use the data and update the sqlite database in tf-es-dumping and proceed on with storing the data for extraction and analysis.

## Project Status
* Updated as of 03/01/2022
* For personal use
* In the midst of refactoring and cleaning up code

## Room for Improvement
* Automate setup procedure
* Implement logging

## Contact
* Do drop me an email at aujunhui88@gmail.com for any suggestions or improvements to the project

