"""
    Sample file demonstrate the Kyanite python client to send/receive Robot data.
    author: Anusha Withana
"""

''' Import the client '''
from KHUBRobotClient import KHUBRobotClient


def on_info_response(*args):
    ''' Define a function to receve info data '''
    print('on_info_response', args)


def on_ops_response(*args):
    ''' Define a function to receve ops data '''
    print('on_ops_response', args)


"""
    Initialize connection
    Attributes:
    name: Name of the sensor/robot/client
    server:Name or IP address of server .
    port:Port address of server .
"""
roboClient = KHUBRobotClient('S1', '10.21.115.215', 9090)

"""
  Trigger callback for a information event to receive data.
  Attributes:
      callBack: Call back function name .
"""
roboClient.onInfo(on_info_response)

"""
  Trigger callback for a operation event to receive data.
  Attributes:
      callBack: Call back function name .
"""
roboClient.onOps(on_ops_response)

"""
  Send the Info as JSON data to the server.
  Attributes:
      data: Data to be sent (JSON) format: http://d.pr/n/45fn .
"""
roboClient.sendInfo(
  {'event': 'position',
        'data': {
            'x': 5,
            'y': 5
        },
        'triggered_at': '2016-06-31 18:20'
})


"""
  Send the Operation as JSON data to the server.
  Attributes:
      data: Data to be sent (JSON) format: http://d.pr/n/45fn .
"""
roboClient.sendOps(
  {'event': 'position',
        'data': {
            'x': 5,
            'y': 5
        },
        'triggered_at': '2016-06-31 18:20'
})


''' Waiting function, only used for demo since the terminal client escapes imediately '''
roboClient.wait(20)
