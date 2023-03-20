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
Library          ../variables/authorization.py  WITH NAME   Auth
Library          ../reddit_api.py   WITH NAME   Api

Variables        ../variables/constants.py
Variables        ../variables/api_methods.py

Test Setup    Log In
# Test Teardown    Log Out

*** Variables ***
${token}
${headers}
${search_thread_text}=  Minecraft
${comment_text}=    Like Python

*** Test Cases ***
Case
    Find Thread
    ${comment_id}=  Add Comment
    Delete Comment  ${comment_id}

*** Keywords ***
Log In
    ${token}=   Auth.get_token
    ${headers}=   Params.get_headers    ${token}
    Create Session      reddit      ${API_URL}     verify=true     headers=${headers}

Log Out
    # ???

Find Thread
    ${params}=  Params.get_params_search_thread    ${search_thread_text}
    ${response}=     GET On Session  reddit  ${search_thread}     params=${params}

    Status Should Be    200     ${response}
    Should Contain      ${response.json()}    names

Add Comment
    ${params}=  Params.get_params_add_comment    ${comment_text}
    ${response}=     POST On Session    reddit    ${add_comment}    params=${params}

    Status Should Be    200     ${response}
    Should Be True      ${response.json()['success']}

    [Return]     ${response.json()['jquery'][18][3][0][0]['data']['id']}

Delete Comment
    [Arguments]    ${comment_id}
    ${response}=     POST On Session    reddit   ${delete_comment}    params=id=t1_${comment_id}
    Status Should Be    200     ${response}
