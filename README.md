# Persian News Titles Generation using Ngram Language Models
* In this project I implemented two Ngram Language Models (bigram and trigram) for generating Persian news titles.
* For creating the dataset, I crawled Titles from some Persian news websites archive sections. The dataset contains 2500 titles which can be seen in title-scraper/title.txt. The crawling process has been done using the Scrapy package in python3.
* frequent.txt contains the most frequent keywords in the dataset. 
* I split the titles in the training set and the test set having been placed in the dataset directory.
* The `DataProceesor` class is for the data preprocessing phase and the `NgramLanguageModel` class is for generating the title.
* I used the negative log-likelihood metric to evaluate the models.
