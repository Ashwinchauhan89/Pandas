import unittest
import pandas as pd

class TestPandasOperations(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }
        self.df = pd.DataFrame(self.data)

    def test_dataframe_shape(self):
        # Test if the DataFrame has correct shape
        self.assertEqual(self.df.shape, (4, 3))

    def test_column_names(self):
        # Test if column names are as expected
        expected_columns = ['Name', 'Age', 'City']
        self.assertListEqual(list(self.df.columns), expected_columns)

    def test_average_age(self):
        # Test if average age is calculated correctly
        expected_average = sum(self.data['Age']) / len(self.data['Age'])
        actual_average = self.df['Age'].mean()
        self.assertEqual(actual_average, expected_average)

    def test_filtering(self):
        # Test filtering rows where Age > 30
        filtered_df = self.df[self.df['Age'] > 30]
        self.assertEqual(filtered_df.shape[0], 2)  # Charlie and David

    def test_add_column(self):
        # Add a new column and test its values
        self.df['Age_plus_5'] = self.df['Age'] + 5
        expected_ages = [30, 35, 40, 45]
        self.assertListEqual(self.df['Age_plus_5'].tolist(), expected_ages)

if __name__ == '__main__':
    unittest.main()
