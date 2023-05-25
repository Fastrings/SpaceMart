# SpaceMart

This project aims towards emulating a simple supermarket with real-life features such as products having expiry dates or discounts applied to certain products regularly. 

## Prerequisites

This program is developed in Python using the following libraries :
- [Random](https://docs.python.org/fr/3/library/random.html)
- [Numpy](https://numpy.org/) 
- [Json](https://docs.python.org/3/library/json.html) 
- [Unittest](https://docs.python.org/3/library/unittest.html)

If you wish to try out this program on your own computer, make sure to have Python 3 installed with those libraries.

## How to use

The program can be launched from the command line using the following command :

```bash
$ python main.py -b X
```

Here, replace *X* by the starting budget you would like to input in the program. Keep in mind that if you choose a number too low and your budget falls below 0, the program will stop.

## Main features

As mentioned previously, this program emulates real-life features of a supermarket. Although it would be impossible to emulate a real-life supermarket perfectly, I chose the following features :
- <span style="text-decoration: underline">Time</span>: This program goes forward in time, prompting the user for a decision every week
- <span style="text-decoration: underline">Sales</span>: Every week, a given number of product is sold
- <span style="text-decoration: underline">Restock</span>: Every week, the stock of available products is replenished
- <span style="text-decoration: underline">Taxes</span>: Every week, the supermarket has to pay taxes
- <span style="text-decoration: underline">Events</span>: Every day, random events can occur. They can be positive or negative for the store
- <span style="text-decoration: underline">Discounts</span>: Every week, some products are randomly picked and discounts are applied on their prices
- <span style="text-decoration: underline">Expiry Dates</span>: Products can expire after a given number of days. When that happens, their price is divided by 2 for the next 3 days. After this, if the product is still not sold, it is thrown away

## Tests

If you want to run the test suite, go to the root of the project and enter the following command :

```bash
$ python -m unittest discover -s tests
```
