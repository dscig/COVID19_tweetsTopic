# Risk Communication in Asian Countries: <br> COVID-19 Discourse on Twitter
Implementation details including codes in Python. You can find the orignal paper "Risk Communication in Asian Countries: COVID-19 Discourse on Twitter" at the following link: http://arxiv.org/xxxx.

##### Please cite as:
Park S, Han S, Kim J, Molaie MM, Vu HD, Singh K, Han J, Lee W, and Cha M <br>
Risk Communication in Asian Countries: COVID-19 Discourse on Twitter <br>
arXiv preprint arXiv:2020.XXXX, 2020. <br>


### Data
#### The raw dataset
We have crawled the Twitter dataset by using the existing Twint Python library and Twitter search APIs. The Twint Python library is an advance twitter scraping tool, written in Python. The detailed information about the scraper is explained at https://github.com/twintproject/twint.

Plese refer to the below code snippet to find an example usage case:
- "./code/.pdf"

Should you wish to get the raw dataset that we have crawled, please directly contact the author via shaun.park@kaist.ac.kr for a detailed instruction. The below table is the statistics of the crawled tweets.

![](./image/stat_crawled_tweets.png)

In particular, we have set up the following keywords/hashtags by country to crawl tweets related to COVID-19.

```
[South Korea]
- corona: 코로나
- wuhan pneumonia: 우한 폐렴

[Iran]
- corona: #کرونا
- coronavirus: #کروناویروس
- wuhan: #ووهان
- pneumonia: #سینه‌پهلو

[Vietnam]
- corona
- n-cov
- covid
- acute pneumonia: viêm phổi cấp

[India]
- corona: कोरोना
- wuhan pneumonia: वूहान निमोनिया
```

Also, Below are the column names and the corresponding descriptions of the dataset:

```
- id (type == int64): 
- conversation_id (int64):
- created_at (datetime64):
- date (datetime64):
- time (object):
- timezone (object):
- user_id (int64):
- username (object):
- name (object):
- place (object):
- tweet (object):
- mentions (object):
- urls (object):
- photos (object):
- replies_count (int64):
- retweets_count (int64):
- likes_count (int64):
- hashtags (object):
- cashtags (object):
- link (object):
- retweet (bool): 
- quote_url 
- video (int64):
- near (object):
- geo (object):
- source (object):
- user_rt_ud (object):
- user_rt (object):
- retweet_id (object):
- reply_to (object):
- retweet_date (object):
- translate (object):
- trans_src (object):
- trans_dest (object):
```


### Pipeline
Please refer to the manuscript to find the detailed explanations for the below four modules.

![](./image/pipeline_topic_model.png)

```
[Required Packages]
The code has been tested running under Python 3.6.6. with the following packages installed (along with their dependencies):
- numpy == 1.16.0
- pandas == 0.23.4
```

#### 1. Pre-processing Data
For the detailed tweet pre-processing and tokenizing process, please refer to the below file including code snippet and correponding explanation:
- "./code/.pdf"

```
[South Korea]
We have used the below Korean-specific stopwords and tokenizers.
- pre-processing: find "./code/korean_stopwords.txt"
- tokenizing: utilized the MeCab-Ko tokenizer (http://eunjeon.blogspot.com/)
- Please refer to the below code snippet to find an example usage case: "./code/.pdf"

[Iran]
We have used the below Farsi-specific stopwords and tokenizers.
- pre-processing: find "./code/farsi_stopwords.txt"
- tokenizing: utilized the 

[Vietnam]
We have used the below Vietnamese-specific stopwords and tokenizers.
- pre-processing: find "./code/vietnamese_stopwords.txt"
- tokenizing: utilized the 

[India]
We have used the below Hindi-specific stopwords and tokenizers.
- pre-processing: find "./code/hindi_stopwords.txt"
- tokenizing: utilized the 
```

#### 2. Decide Topical Phases
For spliting topical phases, plese refer to the below code snippet:
- "./code/.pdf"

For deciding the phases, plese refer to the below code snippet:
- "./code/.pdf"

#### 3. Model Topics
We have used the Tomotopy module (https://bab2min.github.io/tomotopy/v0.6.2/en/). Please refer to the below code snippet to find an example usage case:
- "./code/.pdf" <br> <br>


Should you have any questions or comments, please contact us at the following email address: shaun.park@kaist.ac.kr.
