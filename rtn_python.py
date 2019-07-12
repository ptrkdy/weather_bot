# credit http://eviatarbach.com/2013/05/07/recursive-transition-networks/

import random


def article():
    return random.choice(['a', 'the'])


def adjective():
    return random.choice(['silly', 'thankless', 'big', 'red', 'blue',
                          'green', 'strange', 'purple'])


def noun():
    return random.choice(['shampoo', 'brunch', 'milk', 'cow', 'horns',
                          'bagels'])


def preposition():
    return random.choice(['without'])


def verb():
    return random.choice(['gobbled', 'sneezes'])


def relative_pronoun():
    return random.choice(['that'])


def walk_graph(graph, node='begin', sentence=None):
    if sentence is None:
        sentence = []
    if node == None:
        return ' '.join(sentence)
    if graph[node][0]:
        sentence.append(graph[node][0]())
    return walk_graph(graph, random.choice(graph[node][1]), sentence)


ornate = {'begin': [None, ['article', 'adjective', 'noun']],
          'article': [article, ['adjective', 'noun']],
          'adjective': [adjective, ['adjective', 'noun']],
          'noun': [noun, ['end']],
          'end': [None, [None]]}

fancy = {'begin': [None, ['ornate']],
         'ornate': [lambda: walk_graph(ornate), ['relative', 'preposition', 'end']],
         'preposition': [preposition, ['fancy1']],
         'fancy1': [lambda: walk_graph(fancy), ['end']],
         'relative': [relative_pronoun, ['verb1', 'fancy2']],
         'verb1': [verb, ['fancy3']],
         'fancy3': [lambda: walk_graph(fancy), ['end']],
         'fancy2': [lambda: walk_graph(fancy), ['verb2']],
         'verb2': [verb, ['end']],
         'end': [None, [None]]}

print(walk_graph(fancy))
