from KHUBConnection import KHUBConnection

__copyright__ = "Copyright 2016, Kyanite Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Anusha Withana"
__email__ = "wdanusha@gmail.com"
__status__ = "Development"


class KHUBRobotClient(object):
    """ Class to connect to the Kyanite backend server to send/receive Robot data.
        Attributes:
        name: Name of the sensor/client
        server:Name or IP address of server .
        port:Port address of server .
    """

    def __init__(self, name, server, port):
        self.con = KHUBConnection(name, server, port, '/robot')
        # self.msg_namespace.emit('sname', name)

    def sendInfo(self, data):
        """
        Send the information as JSON data to the server.
        Attributes:
            data: Data to be sent (JSON) .
        """
        self.con.send('info', data)

    def sendOps(self, data):
        """
        Send the Operation as JSON data to the server.
        Attributes:
            data: Data to be sent (JSON) .
        """
        self.con.send('ops', data)

    def wait(self, options):
        """Wait the thread before exiting."""
        self.con.wait(options)
        
    def onInfo(self, callBack):
        print"info"
        """
        Trigger callback for a information event to receive data.
        Attributes:
            callBack: Call back function name .
        """
        self.con.onEvent('info', callBack)

    def onOps(self, callBack):
        print "onOps"
        """
        Trigger callback for a operation event to receive data.
        Attributes:
            callBack: Call back function name .
        """
        self.con.onEvent('ops',callBack)
