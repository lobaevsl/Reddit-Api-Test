*** Settings ***
Documentation    Reddit API test
...              1. Find thread by key
...              2. Write a comment
...              3. Remove a comment
...              variables.py SHOULD BE filled

Library          Collections
Library          RequestsLibrary
Library          JSONLibrary

Variables        ../variables.py

Suite Setup    Create Session      reddit      ${API_URL}     verify=true     headers=${headers}

*** Test Cases ***
Case
# Find thread
    ${response}=     GET On Session  reddit  ${api_method_search_thread}     params=${params_search}

    Status Should Be    200     ${response}
    Should Contain      ${response.json()}    names

# Comment
    ${response}=     POST On Session    reddit    ${api_method_add_comment}    params=${params_comment}
    Status Should Be    200     ${response}
    Should Be True      ${response.json()['success']}

    Set Suite Variable    ${comment_id}     ${response.json()['jquery'][18][3][0][0]['data']['id']}

# Delete comment
    ${response}=     POST On Session    reddit   ${api_method_delete_comment}    params=id=t1_${comment_id}
    Status Should Be    200     ${response}