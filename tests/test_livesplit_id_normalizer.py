import os
import unittest

from livesplit_id_normalizer.livesplit_id_normalizer import normalize

TESTS_PATH = os.path.dirname(os.path.realpath(__file__))
FIXTURES_PATH = os.path.join(TESTS_PATH, "fixtures")


class TestLivesplitIdNormalizer(unittest.TestCase):
    def test_normalize(self):
        run1_path = os.path.join(FIXTURES_PATH, "run1.xml")
        normalize(run1_path)
