#!/bin/bash
# sending request to url and getting response
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
