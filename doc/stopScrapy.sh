#!/bin/bash

/Users/zhoumaoen/redis/bin/redis-cli shutdown  &
kill `ps -ef | grep scrapyd | grep -v grep | awk '{print $2}'` &
kill `ps -ef | grep mongo | grep -v grep | awk '{print $2}'` &