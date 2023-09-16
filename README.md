# My-First-Twitter-API


## Requirement
* Flask
* CORS

## API Documentation

List of APIs
1. Create Tweet API
```
/api/create
```
2.  Delete Tweet API
```
/api/delete/<tweet_id>
```
## To Run 

Run the cmd from Terminal
```
>>> flask --app app run
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
Run tests from Terminal
```
>>> python3 test.py 
 .{'edit_history_tweet_ids': ['1702815938582806759'], 'id': '1702815938582806759', 'text': 'Test tweet'}
..{'deleted': True}
.
----------------------------------------------------------------------
Ran 4 tests in 0.009s

OK
```


