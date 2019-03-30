# WeLeakInfo Scrapper

WeLeakInfo Scrapper is a project that can be used to check [WeLeakInfo](https://search.weleakinfo.com) for the data compromised.

- It can search for the data with the special serach type
- Input.txt : Input file for search
- Output.xlsx : Output file generated

### Tech

This scrapper uses a number of open source projects to work properly:

- [Python3](https://www.python.org/download/releases/3.0/) - Python3 is a programming language that lets you work quickly.
- [Selenium](https://www.seleniumhq.org/) - Selenium is a suite of tools to automate web browsers across many platforms.
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - A Python library to read/write Excel 2010 xlsx/xlsm files.

### Installation

Install the dependencies and devDependencies and start the application.
NOTE : This application has been tested on Winodws OS and Python3

```sh
$ pip install virtualenv
$ git clone https://github.com/shubhamnagota/WeLeakInfoScrapper
$ cd WeLeakInfoScrapper
$ virtualenv -p python3 env
$ env\Scripts\activate
$ pip install -r requirements.txt
$ python app.py
```
