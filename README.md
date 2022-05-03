# PersianNewsTiltleGeneration-NgramLanguageModel
* In This Project I was implemented a Ngram Language Model(bigram and trigram) for Generating Persian News Titles.
* For creating the dataset, I crawled Titles from isna and irna websites archive sections. the size of dataset is about 2500 titles which you can see in title-scraper/title.txt. crawling has been done using scrapy in python3.
* frequent.txt is most frequent keywords in the dataset. 
* I split the titles in the training set and the test set having been placed in dataset directory.
* DataProceesor class is for data preprocessing phase and NgramLanguageModel class is for implementing bigram and trigram models.
* I used negrating log likehood metric for evaluating the Models.
