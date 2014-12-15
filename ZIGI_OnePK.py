rom onep.element.NetworkElement import NetworkElement
from onep.element.SessionConfig import SessionConfig
from onep.core.util import tlspinning

class PinningHandler(tlspinning.TLSUnverifiedElementHandler):
        def __init__(self, pinning_file):
                self.pinning_file = pinning_file
        def handle_verify(self, host, hashtype, finger_print, changed):
                return tlspinning.DecisionType.ACCEPT_ONCE

class zigiElement:

        def __init__(self,addr='localhost',username=None,password=None,pin=None,port='15002'):
                self.addr = addr
                self.username = username
                self.password = password
                self.pin = pin
                self.port = port
                self.config = SessionConfig(None)

        def tlsPinningConnect(self):
                self.config.set_tls_pinning(' ',PinningHandler(''))
                self.config.transportMode = SessionConfig.SessionTransportMode.TLS
                self.config.ca_certs = None
                self.config.keyfile = None
                self.config.certfile = None

        def Connect(self):
                self.elem = NetworkElement(self.addr,'ZIGI-OnePK-APP')
                if(self.pin == None):
                        self.tlsPinningConnect()
                        self.elem.connect(self.username,self.password,self.config)
                        print 'Device Connected..'
  
        def DisConnect(self):
                if(bool(self.elem != None) & self.elem.is_connected()):
                        self.elem.disconnect()
                        print 'Device Disconnected..'
Enter file contents here
