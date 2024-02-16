import unittest
from unittest.mock import patch
import boto3
from func import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    def setUp(self):
        # Initialize DynamoDB client
        self.dynamodb = boto3.resource('dynamodb')

        # Get the actual view count from DynamoDB
        table = self.dynamodb.Table('cloudresume-test')
        response = table.get_item(Key={'id': '1'})
        self.initial_views = response['Item']['views']

    @patch('boto3.resource')
    def test_lambda_handler(self, mock_dynamodb_resource):
        # Invoke lambda_handler
        event = {}
        context = {}
        response = lambda_handler(event, context)

        # Calculate the expected view count (initial views + 1)
        expected_views = self.initial_views + 1

        # Check if views incremented correctly
        self.assertEqual(response, expected_views)

if __name__ == '__main__':
    unittest.main()
