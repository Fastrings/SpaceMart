import numpy as np
import json, os

CATEGORIES = ['animals', 'brain-teasers', 'celebrities', 'entertainment', 'for-kids', 'general', 'geography', 'history', 'hobbies','humanities',
              'literature', 'movies', 'music', 'newest', 'people', 'rated', 'religion-faith', 'science-technology', 'sports', 'television',
              'video-games', 'world']

def pick_categories():
    categories = np.random.choice(CATEGORIES, size=4, replace=False)
    return list(categories)
    
def pick_question(category):
    path = os.path.join('questions', category)
    path += ".json"
    with open(path, 'r', encoding='utf-8') as file:
        questions = json.load(file)
    q = np.random.choice(questions)
    question, categ, answer, choices = q['question'], q['category'], q['answer'], q['choices']
    return question, categ, answer, choices