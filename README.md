[![HitCount](http://hits.dwyl.io/brandon-8019/fossee_web_map.svg)](http://hits.dwyl.io/brandon-8019/fossee_web_map)

# Mapper
[Python](https://python.fossee.in/fellowship2018/) | [Summer Fellowship 2018](https://fossee.in/fellowship) | [Fossee](https://fossee.in/) | [IIT Bombay](http://www.iitb.ac.in/en)
> An web app for letting user upload their **data (.csv format)** and get a better visualization.
> If you already know about this project, you can directly go to the [next part](#next-step)
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
Two types of process are going on here - 
* If any kind of error is there in **State** or **District** data; we will auto currect it for user, as it's too obvious.
* But, in case of **college names**; we will give user a list of suggestions, if the data is found to be erroneous.
> For **Approximate string searching** we are using [fuzzy string matching technique](https://github.com/seatgeek/fuzzywuzzy). It takes two strings and evaluates the percentage match between them. 
* We are using python's **fuzzywuzzy** library to accomplish this.
# Plotting 
We are providing two types of plots here - <br>
### INDIA MAP (STATE-WISE) :
We are using [Google Geochart](https://developers.google.com/chart/interactive/docs/gallery/geochart) for drawing India State-wise map by providing some characteristics variables to extract it - 
```
region : 'IN',
domain : 'IN',
.
.
.
```
### 3-D Pie Chart :
We are again taking help of [Google Pie-chart](https://developers.google.com/chart/interactive/docs/gallery/piechart) for drawing pie-chart, which nicely shows the percentage statistics for each state in a 3D fashion. 
<br>
# Next step
So, that was all about this project.
<br>Now, if you want to run this in your local machine, follow the following instructions.
