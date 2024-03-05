import unittest
from app.popularity_calculator import calculate_popularity


class TestPopularityCalculator(unittest.TestCase):
    def test_missing_stargazers(self):
        repository = {'forks_count': 50}  # Missing 'stargazers_count'
        self.assertEqual(calculate_popularity(repository), 100)

    def test_zero_values(self):
        repository = {'stargazers_count': 0, 'forks_count': 0}
        self.assertEqual(calculate_popularity(repository), 0)

    def test_calculate_popularity(self):
        repository = {'stargazers_count': 100, 'forks_count': 200}
        self.assertEqual(calculate_popularity(repository), 500)


if __name__ == '__main__':
    unittest.main()
