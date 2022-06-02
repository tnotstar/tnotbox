#!/bin/sh

ARGV_X=${1:-123}
ARGV_Y=${2:-456}

curl "http://localhost:3000/graphql" \
    -X "POST" \
    -H "Content-Type: application/json" \
    -d "{ \"query\": \"{ add(x:${ARGV_X}, y:${ARGV_Y}) }\" }" \

# EOF
