#!/bin/bash

ps -ef | grep redis | grep -v grep
ps -ef | grep scrapyd | grep -v grep
ps -ef | grep mongo | grep -v grep