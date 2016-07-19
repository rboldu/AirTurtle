from socketIO_client import SocketIO, BaseNamespace

__author__ = "Anusha Withana"
__copyright__ = "Copyright 2016, Kyanite Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Anusha Withana"
__email__ = "wdanusha@gmail.com"
__status__ = "Development"


class KHUBConnection(object):
    """ Class to connect to the Kyanite backend server to send/receive data.
        Attributes:
        name: Name of the sensor/client
        server:Name or IP address of server .
        port:Port address of server .
        namespace: namespace at server .
    """

    def __init__(self, name, server, port, namespace):
        self.socketIO = SocketIO(server, port)
        self.msg_namespace = self.socketIO.define(BaseNamespace, namespace)
        # self.msg_namespace.emit('sname', name)

    def send(self, eventType, data):
        """
        Send the data as JSON data to the server.
        Attributes:
            eventType: Data event to be triggered at the server (String)
            data: Data to be sent (JSON) .
        """
        self.msg_namespace.emit(eventType, data)

    def onEvent(self, eventName, callBack):
        """
        Trigger callback for a given event.
        Attributes:
            eventName: Event name triggered by the server (String)
            callBack: Call back function name .
        """
        self.msg_namespace.on('ops', callBack)

    def wait(self, options):
        """Wait the thread before exiting."""
        self.socketIO.wait(seconds=options)
