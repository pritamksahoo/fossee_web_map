[![HitCount](http://hits.dwyl.io/brandon-8019/fossee_web_map.svg)](http://hits.dwyl.io/brandon-8019/fossee_web_map)

# Mapper
[Python](https://python.fossee.in/fellowship2018/) | [Summer Fellowship 2018](https://fossee.in/fellowship) | [Fossee](https://fossee.in/) | [IIT Bombay](http://www.iitb.ac.in/en)
> An web app for letting user upload their data (.csv format) and get a better visualization.
### What 'data' will contain :
* College/School Name (Only in INDIA)
* District Name
* State Name
* Address
* Email
* International Dial Code 
* etc.
### Requirements :
```
* Django
* Python
* virtualenv
* pip
* pandas 
* numpy
* fuzzywuzzy
```
## About this project in a nutshell :
**Mapper** is all about plotting user's *data statistics*. It will fetch the data user uploads, **process** it, and finally, plot it on **INDIA MAP** and **PIE CHART**. 
> *Data processing* will be done by [cleaning the data](#data-cleaning) and [error handling](#error-handling).
# Data cleaning
We are considering the following two factors -
* If any row contains a **null** entry in place of **College Name**, the whole record will be dropped.
* If there are duplicate rows, one will be kept, others will be removed.
> We are using **Pandas** library for [data processing](https://www.dataquest.io/blog/pandas-python-tutorial/). It is an open-source, BSD-licensed Python library providing high-performance, easy-to-use data structures and data analysis tools for Python programming language.<br><br>In our case, we are mainly focussing on pandas' **DataFrame** object to handle users' data.
# Error Handling
