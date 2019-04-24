from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_obj(self):
        obj = Post("Test", "Cont")

        self.assertEqual('Test', obj.title)
        self.assertEqual('Cont', obj.content)

    def test_json(self):
        obj = Post("Test", "Cont")

        self.assertDictEqual({'Title': 'Test', 'Content': 'Cont'}, obj.json())

