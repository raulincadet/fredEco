=============
Description
=============

This package allows its users to retrieve data provided by FRED® API and information related to them, such as their source. In this regards, the package allows to search for series list from a category or by keywords. This product uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis.

===========
Features
===========

* Retrieve a time series, when indicating its code;
* Retrieve several time series, indicating their codes;
* Search for all time series related to the keywords indicated by the user;
* Find all time series of a category of series, by indicating the ID of the category;
* Find the dates of all release of a time series;
* Find the information related to a time series, such as the notes where the source of data can be found.

================
Installation
================
.. code-block:: bash

    $ pip install fredeco


===============
Dependencies
===============
* `pandas <https://pandas.pydata.org/>`_
* `numpy <https://numpy.org/>`_
* `requests <https://requests.readthedocs.io/en/latest/>`_
* `datetime <https://docs.python.org/3/library/datetime.html>`_


=========
Usage
=========
Each user of ``fredeco`` should have his own FRED® API key. To accomodate a new user of ``fredeco``, the following function allow her/him to to request a FRED® API key:

.. code-block:: python
   :linenos:

    from fredeco.fredKey import request_api_key
    request_api_key()

To retrieve data, the user of `fredeco` should indicate the ID of an indicator, such as GDP for the US Gross Domestic Product, and GDPCA for the Canadian Gross Domestic Product. One or several indicators can be retreived as follows. Remember that each user should have her/his own API key as explained previously in this section. The API key written bellow is not a real one; it is used to illustrate the usage of the package.

.. code-block:: python
    :linenos:

    from fredeco.fredData import fred_series, fred_multi_series
    fred_api='5gzix5oy2gzx5gzx5' 

    fred_series(series='GDP',fred_api)

    fred_multi_series(series=['GDP','GDPCA'],fred_api)


`fredeco` allow its users to retrieve information about an indicator, as illustrated bellow.

.. code-block:: python
    :linenos:

    from fredeco.fredSearch import fred_info_series
    fred_api='5gzx5oiy2gzx5gzx5'

    fred_info_series(series='GDP',fred_api)


Sometimes, a user may not know the ID of an indicator for which she/he whish to retrieve data. The user may use keywords to search for indicators, as follows:


.. code-block:: python
    :linenos:

    from fredeco.fredSearch import fred_search
    fred_api='5gzx5oiy2gzx5gzx5'

    fred_search(text='Price index',fred_api)


`fredeco` allows its users to quickly explore key statistics and information related to data retrieved, as follows, where `df` is a data frame of one or several indicators retrieved from FRED® API. The `explore()` function does not require the user to add a FRED® API key.


.. code-block:: python
    :linenos:

    from fredeco.fredData import explore
    
    explore(df) 


=========================
License and terms of use
=========================

* `fredeco` created by Raulin L. Cadet. It is licensed under the terms of the MIT license.
* By using the package `fredeco`, you are also agreeing to be bound by the FRED® API Terms of Use. The link to these Terms of Use is: `Here <https://fred.stlouisfed.org/docs/api/terms_of_use.html>`_. 