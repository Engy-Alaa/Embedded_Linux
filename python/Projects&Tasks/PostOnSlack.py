"""
A simple slack message sender
"""
import json
import requests

msg = { "text": "Hello This Is Engy From Python"}

webhook ='WEBHOOK_TOKEN'
requests.post(webhook, data = json.dumps(msg))                        
