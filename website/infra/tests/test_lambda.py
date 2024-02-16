import unittest
import sys

# Add the directory containing the lambda_handler function to the Python path
sys.path.append('/website/infra/lambda/')

# Now you can import the lambda_handler function
from func import lambda_handler
from unittest.mock import patch

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.resource')
    def test_lambda_handler(self, mock_dynamodb_resource):
        # Mock DynamoDB table
        mock_table = mock_dynamodb_resource().Table()
        mock_table.get_item.return_value = {
            'Item': {
                'id': '1',
                'views': 5
            }
        }

        # Invoke lambda_handler
        event = {}
        context = {}
        response = lambda_handler(event, context)

        # Check if views incremented correctly
        self.assertEqual(response, 6)

if __name__ == '__main__':
    unittest.main()