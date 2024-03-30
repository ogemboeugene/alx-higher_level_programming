#!/bin/bash
#script to send GET request with header variable X-School-User-Id with the value 98
curl -sX GET -H X-School-User-Id:98 "$1"
