*** Settings ***
Resource    ../robot_framework_resources/keywords.resource

Test Setup    Log In
Test Teardown    Log Out

*** Variables ***
${search_thread_text}=  Minecraft

*** Test Cases ***
Case
    Find Thread     ${search_thread_text}


