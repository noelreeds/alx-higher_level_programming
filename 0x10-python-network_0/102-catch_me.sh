#!/bin/bash
# causes the server to respond with a custom message
curl -sX PUT -d "You got me!" 0.0.0.0:5000/catch_me
