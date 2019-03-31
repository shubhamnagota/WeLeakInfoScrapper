# WeLeakInfo Scrapper

WeLeakInfo Scrapper is a project that can be used to check [WeLeakInfo](https://search.weleakinfo.com) for the data compromised.

- It can search for the data with the special search type
- input.txt : Input file for search
- output.xlsx : Output file generated

### Input and Output Formats

```sh
$ Input Data:
SearchTerm              SearchType [If not provided, username by default]
homer                   username
homer@gmail.com         email


$ Output Data in xlsx:
SearchTerm              SearchType              Results
homer                   username                x Results Found in y Websites
homer@gmail.com         email                   x Results Found in y Websites
```

A `input.txt` file is provided as well as a `custom_input.txt` dummy data file.

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
