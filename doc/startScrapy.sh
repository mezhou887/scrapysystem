#!/bin/bash

/Users/zhoumaoen/redis/bin/redis-server /Users/zhoumaoen/redis/etc/redis.conf &
scrapyd &
/Users/zhoumaoen/MongoDB/bin/mongod --dbpath /Users/zhoumaoen/data/mongodb &
