*** Settings ***
Resource    ../robot_framework_resources/keywords.resource
Library     ../variables/params.py   WITH NAME   Params

Test Setup    Setup
Test Teardown    Log Out

*** Variables ***
${comment_text}=    Comment to be removed hahaha
${comment_id}=  231

*** Test Cases ***
Case Delete Comment
    Delete Comment    ${comment_id}

*** Keywords ***
Setup
    Log In
    Wait Until Keyword Succeeds    5x   5 sec    Add Comment And Get Id

Add Comment And Get Id
    ${params}=   Params.get_params_add_comment    ${comment_text}
    ${response}=     POST On Session    reddit    ${add_comment}    params=${params}

    Status Should Be    200     ${response}
    Should Be True      ${response.json()['success']}

    Set Global Variable    ${comment_id}       ${response.json()['jquery'][18][3][0][0]['data']['id']}