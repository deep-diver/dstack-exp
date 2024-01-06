#!/bin/bash

curl -X POST --location https://my-awesome-run.deep-diver-main.cloud.dstack.ai/generate \
    -H 'Content-Type: application/json' \
    -d '{ \
          "inputs": "What is Deep Learning?", \
          "parameters": { \
            "max_new_tokens": 20 \
          } \
        }'