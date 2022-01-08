
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The purpose of this project to explore sentiment analysis and NLP by analyzing a dataset of tweets. Sentiment analysis is a common task of NLP which takes in input and classifies and categorizes the data into a sentiment. More information [here](https://en.wikipedia.org/wiki/Sentiment_analysis)

The process of Sentiment Analysis includes (but is not limited too):
1. Tokenization - Involves breaking down a statement into individual words and characters
2. Cleaning data - Removing special characters and converting words into its canonical form through stemming and/or lemmatization (two common types of normalization)
3. Removing Noise - Removing stop words -> any words that do not add value to the analysis of the statement
4. Classification - Classifying words into their connotation -1 (negative), 0 (neutral) or +1 (positive)
5. Calculation - Calculating the over all score of the statement.

The above 5 steps may vary depending on what is it you are trying to achieve

### Built With

This project follows and expands on the the "How To Perform Sentiment Analysis in Python 3 Using the Natural Language Toolkit (NLTK)" tutorial created by Shaumik Daityari from Digital Ocean

* [Tutorial] (https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk)
* [Python](https://www.python.org/)
* [NLTK](https://www.nltk.org/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* [Python](https://www.python.org/)
* [NLTK](https://pypi.org/project/nltk/)
  ```sh
    pip install nltk
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

### References
[A Quick Guide To Sentiment Analysis](https://www.youtube.com/watch?v=O_B7XLfx0ic&ab_channel=edureka%21)
[How To Perform Sentiment Analysis in Python 3 Using the Natural Language Toolkit (NLTK)](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk)
