#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import json

def get_status():
    #cosm read-only auth
    feed_id=86779
    api_key="X2T6DmTX1EjUyXWEKx8dBPk37nAx6JCTGCKLfDkjjd5l1ly4"

    #get current status from cosm
    url="http://api.xively.com/v2/feeds/%s.json?datastreams=%s" % (feed_id,"hacklab_status")
    headers = {'X-ApiKey':api_key}

    #fail silently on http/connection errors to cosm and
    #return that the hacklab is closed.

    try:
        req = requests.get(url, headers=headers)
        data = json.loads(req.text)
        current_value = data['datastreams'][0]['current_value']
    except:
        current_value="0"

    return current_value

if __name__=='__main__':
    status = get_status()
    if status=="1":
        print("It's open.")
    else:
        print("It's closed.")
