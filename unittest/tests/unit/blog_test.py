from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_blog_obj_create(self):
        obj = Blog('Title', 'Ashish')
        self.assertEqual('Title', obj.title)
        self.assertEqual('Ashish', obj.author)
        self.assertListEqual([], obj.posts)

    def test_repr(self):
        obj = Blog('Title', 'Ashish')
        self.assertEqual('Ashish has Title', obj.__repr__())

        obj2 = Blog('Title2', 'Ashish2')
        self.assertEqual('Ashish2 has Title2', obj2.__repr__())
