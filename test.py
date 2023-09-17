# Unit Test Cases written by Upasana Kumar

import unittest
from unittest.mock import patch
from app import app

class TwitterAPIValidationError(Exception):
     def __init__(self, message, api_messages):            
        super().__init__(message)
        self.api_messages = api_messages

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    @patch('app.tweepy.Client')
    def test_create_tweet_success(self, mock_client):
        mock_response = {
            "edit_history_tweet_ids": [
                "1702815938582806759"
            ],
            "id": "1702815938582806759",
            "text": "Test tweet"
        }
        mock_tweepy_client = mock_client.return_value 
        mock_tweepy_client.create_tweet.return_value = mock_response
        response = self.client.post('/create', json={'text': 'Test tweet'})
        self.assertEqual(response.get_json()["statusCode"], 200)
        self.assertEqual(response.get_json(), {
            "isError": False,
            "message": "Success",
            "statusCode": 200,
            "data": {"edit_history_tweet_ids": ["1702815938582806759"], "id": "1702815938582806759", "text": "Test tweet"}
        })
    
    @patch('app.tweepy.Client')
    def test_create_tweet_failure(self, mock_client):
        mock_tweepy_client = mock_client.return_value
        mock_tweepy_client.create_tweet.side_effect = TwitterAPIValidationError("Failed", [""])
        client = app.test_client()
        response = client.post('/create', json={'text': 'Test tweet'})
        self.assertEqual(response.get_json()["statusCode"], 500)
        self.assertEqual(response.get_json(), {
            "isError": True,
            "message": "",
            "statusCode": 500,
            "data": {}
        })
    
    @patch('app.tweepy.Client')
    def test_delete_tweet_success(self, mock_client):
        mock_response = {
            "deleted": True,
        }
        mock_tweepy_client = mock_client.return_value 
        mock_tweepy_client.delete_tweet.return_value = mock_response
        client = app.test_client()
        response = client.delete('/delete/12345')
        self.assertEqual(response.get_json()["statusCode"], 200)
        self.assertEqual(response.get_json(), {
            "isError": False,
            "message": "Success",
            "statusCode": 200,
            "data": { "deleted": True}
        })

    @patch('app.tweepy.Client')
    def test_delete_tweet_failure(self, mock_client):
        mock_tweepy_client = mock_client.return_value
        mock_tweepy_client.delete_tweet.side_effect = Exception("Failed")
        client = app.test_client()
        response = client.delete('/delete/12345')
        self.assertEqual(response.get_json()["statusCode"], 500)
        self.assertEqual(response.get_json(), {
            "isError": True,
            "message": "Failed",
            "statusCode": 500,
            "data": {}
        }) 

if __name__ == '__main__':
    unittest.main()
