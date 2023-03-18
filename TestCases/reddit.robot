*** Settings ***
Documentation    Reddit API test
...              1. Find thread by key
...              2. Write a comment
...              3. Remove a comment
...              variables.py SHOULD BE filled

Library          Collections
Library          RequestsLibrary
Library          JSONLibrary
Library          ../variables/params.py   WITH NAME   Params

Variables        ../variables/constants.py
Variables        ../variables/api_methods.py

Suite Setup      Create Session      reddit      ${API_URL}     verify=true     headers=

*** Variables ***



*** Test Cases ***
Case
    Find Thread
    ${comment_id}=  Comment
    Delete Comment  ${comment_id}

*** Keywords ***
Find Thread
    ${response}=     GET On Session  reddit  ${search_thread}     params=${params_search}

    Status Should Be    200     ${response}
    Should Contain      ${response.json()}    names

Comment
    ${response}=     POST On Session    reddit    ${add_comment}    params=${params_comment}
    Status Should Be    200     ${response}
    Should Be True      ${response.json()['success']}

    [Return]     ${response.json()['jquery'][18][3][0][0]['data']['id']}

Delete Comment
    [Arguments]    ${comment_id}
    ${response}=     POST On Session    reddit   ${delete_comment}    params=id=t1_${comment_id}
    Status Should Be    200     ${response}