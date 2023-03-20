*** Settings ***
Resource    ../robot_framework_resources/keywords.resource
Library     ../variables/params.py   WITH NAME   Params

Test Setup    Log In
Test Teardown    Log Out

*** Variables ***
${comment_text}=  Wow, this is cute!2

*** Test Cases ***
Case
    ${comment_id}=  Add Comment    ${comment_text}
    Params.set_comment_id   ${comment_id}

