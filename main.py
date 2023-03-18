import robot
import reddit_api


reddit_api.authenticate()

robot.run('TestCases/reddit.robot')
