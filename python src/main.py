#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

from flask import escape

import urllib.request


project_id = 'hackher413-petid-231219'
model_id = 'ICN6006971135356890352'

def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1beta1.PredictionServiceClient()

    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned


# [START vision_quickstart]
import io
import os
import json
# Imports the Google Cloud client library
# [START vision_python_migration_import]
from google.cloud import vision
from google.cloud.vision import types
# [END vision_python_migration_import]

def run_quickstart(request):
    
    #URL from Firebase
    request_json = request.get_json()
    request_args = request.args
    
    if request_json and 'url' in request_json:
        url = request_json['url']
    elif request_args and 'url' in request_args:
        url = request_args['url']
    else:
        url = 'error'
    
    with urllib.request.urlopen(url) as response:
        picture = response.read()
    
    return json.dumps(get_prediction(picture, project_id, model_id))

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources/dogpic.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    
export GOOGLE_APPLICATION_CREDENTIALS=f8e13e305119f9b2aacd9136b5582def511b3cfe