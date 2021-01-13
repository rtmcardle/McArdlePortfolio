# Data Mining
This directory showcases the production of various decision making models using large amounts of data.

## [Model Development](ModelDevelopment/)
This directory contains a [ModelDevelopment](ModelDevelopment/ModelDevelopment.py) class that is capable of generating predictive models for both the [Wisconsin Breast Cancer Data Set][1] (a classification model) and a sample of data from the [NAM Forecast System][2] from 2017-2018 associated with a timeseries of detected solar radiation (a regression model).

## [Naive Bayes Text](NaiveBayesText/)
This directory contains an [AuthorClassification](NaiveBayesText/AuthorClassification.py) class which is capable of performing Naive Bayes classification on paragraph-length samples of writing in order to identify the author of the passage. The classifier uses a sample of texts from [Project Gutenberg][3] to create both the training corpus and the testing set. 

## [Time Series Stats](TimeSeriesStats/)
This directory contains a wrapper class which is able to isolate the relevant time-series data for a given date range from a sample of observations from the [Florida Automated Weather Network][4] taken from 2017-2019. The wrapper reports a set of statistics over the provided attribute for the range of data. Created for an assignment intended to familiarize oneself with the [Pandas][5] library and large-scale data management. 





[1]: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
[2]: https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/north-american-mesoscale-forecast-system-nam
[3]: https://www.gutenberg.org/
[4]: https://fawn.ifas.ufl.edu/data/
[5]: https://pandas.pydata.org/
