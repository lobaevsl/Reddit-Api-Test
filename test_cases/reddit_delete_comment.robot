*** Settings ***
Resource    ../robot_framework_resources/keywords.resource
Library     ../variables/params.py   WITH NAME   Params

Test Setup    Log In
Test Teardown    Log Out

*** Test Cases ***
Case
    ${comment_id}=  Params.get_comment_id
    Delete Comment    ${comment_id}
