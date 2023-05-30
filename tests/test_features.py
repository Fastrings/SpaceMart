import unittest, random
from main import fast_forward
from src.quiz_parser import pick_categories, pick_question, CATEGORIES
from src.spacemart import SpaceMart

class TestFeatures(unittest.TestCase):

    def setUp(self):
        self.mart = SpaceMart(150000)

    def test_quiz_pick_categories(self):
        selection = pick_categories()
        for item in selection:
            self.assertIn(item, CATEGORIES)
        self.assertEqual(len(set(selection)), len(selection))

    def test_quiz_pick_question(self):
        random_category = random.choice(CATEGORIES)
        question, categ, answer, choices = pick_question(random_category)
        self.assertEqual(categ, random_category)
        self.assertIn(answer, choices)
        self.assertNotEqual(question, "")

    def test_fast_forward(self):
        self.assertEqual(self.mart.days, 1)
        fast_forward(20, self.mart)
        self.assertEqual(self.mart.days, 21)
        self.assertGreater(self.mart.budget, 150000)