*** Settings ***
Documentation    Reddit API test
...              1. Find thread by key
...              2. Write a comment
...              3. Remove a comment
Resource         variables.resource
Variables        ../variables.py

*** Test Cases ***
Get Thread And Comment
