# id3_algorithm.py
import math
from collections import Counter

class Node:
    def __init__(self, attribute=None, value=None, results=None, children=None):
        self.attribute = attribute
        self.value = value
        self.results = results
        self.children = children if children else {}

def entropy(data):
    total = len(data)
    counts = Counter(data)
    entropy = 0
    for label in counts:
        prob = counts[label] / total
        entropy -= prob * math.log(prob, 2)
    return entropy

def split_data(data, attribute):
    sets = {}
    for entry in data:
        value = entry[attribute]
        if value not in sets:
            sets[value] = []
        sets[value].append(entry)
    return sets

def build_tree(data, features):
    if not data:
        return Node()
    
    current_entropy = entropy([entry['has_heart_disease'] for entry in data])
    best_info_gain = 0.0
    best_criteria = None
    best_sets = None
    
    for feature in features:
        sets = split_data(data, feature)
        total_entropy = 0
        for value, subset in sets.items():
            prob = len(subset) / len(data)
            total_entropy += prob * entropy([entry['has_heart_disease'] for entry in subset])
        info_gain = current_entropy - total_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_criteria = feature
            best_sets = sets
    
    if best_info_gain > 0:
        children = {}
        for value, subset in best_sets.items():
            children[value] = build_tree(subset, [f for f in features if f != best_criteria])
        return Node(attribute=best_criteria, children=children)
    else:
        return Node(results=Counter([entry['has_heart_disease'] for entry in data]))

def predict(tree, entry):
    if tree.results is not None:
        return tree.results.most_common(1)[0][0]
    else:
        branch = tree.children[entry[tree.attribute]]
        return predict(branch, entry)
