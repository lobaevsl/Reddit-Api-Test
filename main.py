import robot
import variables
import reddit_api


reddit_api.authenticate()
variables.params_search = {'query': f'r/Minecraft'}
variables.params_comment = {'thing_id': f't3_{variables.POST_ID}',
                            'text': 'I LIKE PYTHON! WOW'}

robot.run('TestCases/reddit.robot')
