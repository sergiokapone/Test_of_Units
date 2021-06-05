import unittest
from count_inseries import get_num_count
class NumbersCaseTest(unittest.TestCase):
    """Тести для функції get_num_count з count_inseries.py """
    def test_5_num_in_1_100(self):
        """Перевіряємо скільки 5-рок в межаах від 1 до 100"""
        counts = get_num_count(5, 1, 100) 
        self.assertEqual(counts, 20)
        
if __name__== "__main__":
    unittest.main()