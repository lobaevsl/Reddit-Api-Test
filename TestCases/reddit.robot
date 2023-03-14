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


*** Test Cases ***
Get Thread
    Create Session      reddit      ${API_URL}     verify=true     headers=${headers}

    ${resp_reddit}=     GET On Session  reddit  /api/search_reddit_names     params=${params_search}

    Status Should Be    200     ${resp_reddit}
    Should Contain      ${resp_reddit.json()}    names

Comment
    Create Session      reddit      ${API_URL}     verify=true     headers=${headers}

    ${resp_reddit}=     POST On Session    reddit    /api/comment    params=${params_comment}
    Status Should Be    200     ${resp_reddit}
    Should Be True      ${resp_reddit.json()['success']}

    Set Suite Variable    ${comment_id}     ${resp_reddit.json()['jquery'][18][3][0][0]['data']['id']}

Delete Comment
    Create Session      reddit      ${API_URL}     verify=true     headers=${headers}

    ${resp_reddit}=     POST On Session    reddit   /api/del    params=id=t1_${comment_id}
    Status Should Be    200     ${resp_reddit}