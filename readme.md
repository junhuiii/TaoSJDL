# 淘数据 Scraper
 <hr />
Scraper Bot that scrapes data from [淘数据](https://taosj.com/)

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

## Setup
* Upon cloning the repository, 4 directories need to be created, namely
    * /src/TaoSJ Meta/
    * /src/download-dump/
    * /tf-es-dumping (TaoSJ Data backup)/
    * /src/TaoSJ Data/
* Proceed to config.toml and input the relevant login details for the 淘数据 account. You will have to purchase the service. This is not a free scraper.

## Usage

## Project Status
* As of 03/01/2022
* For personal use
* In the midst of refactoring and cleaning up code

## Room for Improvement

## Contact
* Do drop me an email at aujunhui88@gmail.com for any suggestions or improvements to the project

