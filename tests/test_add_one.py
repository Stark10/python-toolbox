from unittest import TestCase
from python_toolbox.add_one import add_one


class Test(TestCase):
    def test_add_one(self):
        return self.assertEqual(add_one(45), 46)
