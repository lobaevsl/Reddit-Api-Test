*** Settings ***
Library          Collections
Library          RequestsLibrary
Library          JSONLibrary

Library          ../variables/params.py   WITH NAME   Params
Library          ../variables/authorization.py  WITH NAME   Auth
Library          ../reddit_api.py   WITH NAME   Api

Variables        ../variables/constants.py
Variables        ../variables/api_methods.py

*** Keywords ***
Log In
    ${token}=   Auth.get_token
    ${headers}=   Params.get_headers    ${token}
    Create Session      reddit      ${API_URL}     verify=true     headers=${headers}

Log Out
    Delete All Sessions

Find Thread
    [Arguments]    ${query}
    ${params}=  Params.get_params_search_thread    ${query}
    ${response}=     GET On Session  reddit  ${search_thread}     params=${params}

    Status Should Be    200     ${response}
    Should Contain      ${response.json()}    names

Add Comment
    [Arguments]    ${text}
    ${params}=  Params.get_params_add_comment    ${text}
    ${response}=     POST On Session    reddit    ${add_comment}    params=${params}

    Status Should Be    200     ${response}
    Should Be True      ${response.json()['success']}

    [Return]     ${response.json()['jquery'][18][3][0][0]['data']['id']}

Delete Comment
    [Arguments]    ${comment_id}
    ${response}=     POST On Session    reddit   ${delete_comment}    params=id=t1_${comment_id}
    Status Should Be    200     ${response}