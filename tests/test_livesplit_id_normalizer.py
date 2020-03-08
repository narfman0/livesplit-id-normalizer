import os
import unittest

from livesplit_id_normalizer import livesplit_id_normalizer as norm

TESTS_PATH = os.path.dirname(os.path.realpath(__file__))
FIXTURES_PATH = os.path.join(TESTS_PATH, "fixtures")
RUN1_PATH = os.path.join(FIXTURES_PATH, "run1.xml")


class TestLivesplitIdNormalizer(unittest.TestCase):
    def setUp(self):
        self.root = norm.parse_tree(RUN1_PATH)

    def test_find_initial_run(self):
        self.assertEqual(3, norm.find_initial_run(self.root))

    def test_normalize(self):
        norm.normalize(RUN1_PATH)
