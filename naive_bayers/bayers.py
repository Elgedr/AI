import csv
import math

each_topic_words = {}
topic_all_words = {}
unique_words = set()
topic_articles_amount = {}


def testing():
    correct_topics = 0
    incorrect_topics = 0
    articles_amount = training()
    topic_possibility = {}

    with open("bbc_test.csv", encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            for theme in topic_articles_amount.keys():
                topic_possibility[theme] = math.log(topic_articles_amount[theme] / articles_amount)
            for word in text.split():
                word = word.lower()
                if len(word) >= 5:
                    for theme in topic_possibility.keys():
                        if word in each_topic_words[theme].keys():
                            formula = (each_topic_words[theme][word] + 1) / (topic_all_words[topic] + len(unique_words))
                        else:
                            formula = 1 / (topic_all_words[theme] + len(unique_words))
                        topic_possibility[theme] = topic_possibility[theme] + math.log(formula)
            max_possibility = 0
            max_possibility_topic = ""
            for theme in topic_possibility.keys():
                if max_possibility == 0 or topic_possibility[theme] > max_possibility:
                    max_possibility = topic_possibility[theme]
                    max_possibility_topic = theme
            if max_possibility_topic != topic:
                incorrect_topics += 1
            else:
                correct_topics += 1
            topic_possibility.clear()
    print("accuracy: " + str((100 * correct_topics) / (correct_topics + incorrect_topics)))


def training():
    all_articles = 0
    with open("bbc_train.csv", encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            all_articles += 1
            if topic in topic_articles_amount.keys():
                topic_articles_amount[topic] += 1
            else:
                topic_articles_amount[topic] = 1
            for word in text.split():
                word = word.lower()
                if len(word) >= 2:
                    unique_words.add(word)
                    if topic in topic_all_words.keys():
                        topic_all_words[topic] += 1
                        if word in each_topic_words[topic].keys():
                            each_topic_words[topic][word] += 1
                        else:
                            each_topic_words[topic][word] = 1
                    else:
                        each_topic_words[topic] = {word: 1}
                        topic_all_words[topic] = 1
    return all_articles


if __name__ == '__main__':
    testing()
