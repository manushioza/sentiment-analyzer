# Import libaries
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

import re
import string
import random

# Define a function to tokenize words, remove stop words, and normalize words,


def remove_noise(tweet_tokens, stop_words=()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


if __name__ == "__main__":

    # Get the tweets from the training set
    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')
    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

    # Get the list oofstop words
    stop_words = stopwords.words('english')

    # Tokenize the tweets
    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []
    # Clean the tweets by removing stop words, punctuation, and words that are not in present tense
    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    '''
    #Get the frequency of all the words in the tweets
    all_pos_words = get_all_words(positive_cleaned_tokens_list)

    freq_dist_pos = FreqDist(all_pos_words)
    print(freq_dist_pos.most_common(10))
    '''
    # Get positive and negative tweets for model training
    positive_tokens_for_model = get_tweets_for_model(
        positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(
        negative_cleaned_tokens_list)

    # Add list of positive and negative tweets to the dataset model
    positive_dataset = [(tweet_dict, "Positive")
                        for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                        for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset
    # Shuffle the dataset
    random.shuffle(dataset)

    # Split the dataset into train and test sets. DS contains 10 000 tweets, 70% is used in training and 30% is used in testing
    train_data = dataset[:7000]
    test_data = dataset[7000:]

    # Train the model using Naive Bayes Classifier algorithm
    classifier = NaiveBayesClassifier.train(train_data)

    # Test the model and print accuracy
    print("Accuracy is:", classify.accuracy(classifier, test_data))

    # Print the most informative features
    print(classifier.show_most_informative_features(10))

    custom_tweet = "I ordered just once from TerribleCo, they screwed up, never used the app again."
    print("Performing Sentiment Anaylsis on the folowing tweet" + custom_tweet)

    # Tokenize the custom tweet
    custom_tokens = remove_noise(word_tokenize(custom_tweet))
    # Classify the custom tweet
    print(" >>> "+classifier.classify(dict([token, True] for token in custom_tokens)))
