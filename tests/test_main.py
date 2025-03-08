# tests/test_main.py
import unittest
import os
from utils import calculate_similarity

class TestPlagiarismChecker(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_files')
    
    def test_identical_files(self):
        orig = os.path.join(self.test_dir, 'orig.txt')
        self.assertAlmostEqual(
            calculate_similarity(orig, orig), 
            1.0, 
            delta=0.01
        )
    
    def test_empty_files(self):
        empty = os.path.join(self.test_dir, 'empty.txt')
        self.assertEqual(calculate_similarity(empty, empty), 1.0)
    
    def test_partially_modified(self):
        orig = os.path.join(self.test_dir, 'orig.txt')
        copy = os.path.join(self.test_dir, 'orig_0.8_add.txt')
        similarity = calculate_similarity(orig, copy)
        self.assertTrue(0.75 <= similarity <= 0.85)
    
    # 更多测试用例...

if __name__ == '__main__':
    unittest.main()
