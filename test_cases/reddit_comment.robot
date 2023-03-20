*** Settings ***
Resource    ../robot_framework_resources/keywords.resource
Library     ../variables/params.py   WITH NAME   Params

Test Setup    Log In
Test Teardown    Teardown

*** Variables ***
${comment_text}=  Wow, this is cute!5е2345324
${comment_id}

*** Test Cases ***
Case Add Comment
    ${id}=  Add Comment    ${comment_text}

    Set Global Variable    ${comment_id}    ${id}

*** Keywords ***
Teardown
    Delete Comment  ${comment_id}
    Log Out
