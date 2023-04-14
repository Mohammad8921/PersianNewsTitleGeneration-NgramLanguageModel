# Persian News Titles Generation using Ngram Language Models
* In this project I implemented two Ngram Language Models (bigram and trigram) for generating persian news titles.
* For creating the dataset, I crawled Titles from some persian news websites archive sections. The dataset containes 2500 titles which can be seen in title-scraper/title.txt. Crawling process has been done using scrapy package in python3.
* frequent.txt is the most frequent keywords in the dataset. 
* I split the titles in the training set and the test set having been placed in dataset directory.
* __DataProceesor__ class is for data preprocessing phase and __NgramLanguageModel__ class is for generating the title.
* I used negative log likehood metric to evaluate the models.
