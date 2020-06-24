#June 11 2020
#course_2_project

#Project Description: We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet.
#We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
#You will create a csv file, which contains columns for the Number of Retweets, Number of Replies,
#Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

#Task 1. To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace()
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(strings):
    for character in punctuation_chars:
        strings = strings.replace(character, "")
    return strings

#Task 2. Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so #you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(strings):
    for character in punctuation_chars:
        strings = strings.replace(character, "")
    return strings

def get_pos(string_sentence):
    positive_count = 0
    string_sentence = strip_punctuation(string_sentence.lower())
    split_sentence = string_sentence.split()

    for word in split_sentence:
        for positive_word in positive_words:
            if word == positive_word:
                positive_count += 1
    return positive_count

#Task 3. Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(strings):
    for character in punctuation_chars:
        strings = strings.replace(character, "")
    return strings

def get_neg(string_sentence):
    negative_count = 0
    string_sentence = strip_punctuation(string_sentence.lower())
    split_sentence = string_sentence.split()

    for word in split_sentence:
        for negative in negative_words:
            if word == negative:
                negative_count += 1
    return negative_count

#Task 4. Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.
Project_Twitter = open("project_twitter_data.csv")
Resulting_Data = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(strings):
    for character in punctuation_chars:
        strings = strings.replace(character, "")
    return strings

def get_pos(string_sentence):
    positive_count = 0
    string_sentence = strip_punctuation(string_sentence.lower())
    split_sentence = string_sentence.split()

    for word in split_sentence:
        for positive_word in positive_words:
            if word == positive_word:
                positive_count += 1
    return positive_count

def get_neg(string_sentence):
    negative_count = 0
    string_sentence = strip_punctuation(string_sentence.lower())
    split_sentence = string_sentence.split()

    for word in split_sentence:
        for negative in negative_words:
            if word == negative:
                negative_count += 1
    return negative_count

def write_data_file(Resulting_Data):
    Resulting_Data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    Resulting_Data.write("\n")

    project_twitter_lines =  Project_Twitter.readlines()
    header= project_twitter_lines.pop(0)
    for twitter_data_lines in project_twitter_lines :
        twitter_data_lines = twitter_data_lines.strip().split(',')
        Resulting_Data.write("{}, {}, {}, {}, {}".format(twitter_data_lines[1], twitter_data_lines[2], get_pos(twitter_data_lines[0]), get_neg(twitter_data_lines[0]), (get_pos(twitter_data_lines[0])-get_neg(twitter_data_lines[0]))))
        Resulting_Data.write("\n")



write_data_file(Resulting_Data)
Project_Twitter.close()
Resulting_Data.close()
