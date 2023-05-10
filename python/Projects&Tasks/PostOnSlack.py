"""
A simple slack message sender
"""
import json
import requests

msg = { "text": "Hello This Is Engy From Python"}

webhook ='https://hooks.slack.com/services/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'
requests.post(webhook, data = json.dumps(msg))                        
