import unittest
from unittest.mock import MagicMock, patch
from func import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.resource')
    def test_lambda_handler(self, mock_dynamodb_resource):
        # Mock DynamoDB table
        mock_table = mock_dynamodb_resource().Table()

        # Define the initial 'views' value
        initial_views = 0

        # Mock the get_item method to return the initial 'views' value
        mock_table.get_item.return_value = {
            'Item': {
                'id': '1',
                'views': initial_views
            }
        }

        # Invoke lambda_handler
        event = {}
        context = {}
        response = lambda_handler(event, context)

        # Check if views incremented correctly
        expected_views = initial_views + 1
        self.assertEqual(response, expected_views)

if __name__ == '__main__':
    unittest.main()