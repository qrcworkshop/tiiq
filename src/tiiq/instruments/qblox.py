"""
class for interfacing with Qblox QRM and QCM
"""


from tiiq.instruments.abstract import Instrument

from pulsar_qcm.pulsar_qcm import pulsar_qcm
from pulsar_qrm.pulsar_qrm import pulsar_qrm

# Connect to modules
qcm = pulsar_qcm("qcm", "192.168.0.2")  # This module uses the default IP address.
qrm = pulsar_qrm("qrm", "192.168.0.3")  # This module's IP address was changed.


class Pulsar_QCM(Instrument):
    _ip_address = None
    _qcm = None


    _clock_type = "Internal"
    _gain = None
    _offset = None
    _phase = None
    _sequencers = []
    _paths = []
    _ports = []
    Out1 = None
    Out2 = None
    Out3 = None
    Out4 = None


	# Contructora

    def __init__(self, ip_address):
        #initialization of QRM object with ip
        self._ip_address = ip_address
        self._qcm = pulsar_qcm("qcm", ip_address)

        super().__init__()
        pass


	#Modificadoras

    def set_reference_clock_external (self):
    #set external reference clock QRM and QCM

	def setup (self, params):
	#Function for setting up the QRM waveforms

	def upload_waveforms(self):
	#Function for upload waveforms in QRM

	def upload_sequence(self, type, params):
	#Upload the sequence to the QRM necessary for experiment defined in type (Raby, T1, T2...)

	#Destructoras

	def reset (self):
	#reset QRM

	def stop_sequencers(self):
	#stop current sequence running in QRM

	def close_connections(self):
	#close connection to QRM



class Pulsar_QRM(Instrument):
    _ip_address = None
    _qrm = None

    _clock_type = "Internal"
    _gain = None
    _offset = None
    _phase = None
    _sequencers = []
    _paths = []
    _ports = []
    Out1 = None
    Out2 = None
    In1 = None
    In2 = None

	# Contructora

    def __init__(self, ip_address):
        #initialization of QRM object with ip
        self._ip_address = ip_address
        self._qrm = pulsar_qrm("qrm", ip_address)

        super().__init__()
        pass

	#Modificadoras

    def set_reference_clock_external (self):
    #set external reference clock QRM and QCM

	def setup (self, params):
	#Function for setting up the QRM waveforms

	def upload_waveforms(self):
	#Function for upload waveforms in QRM

	def upload_sequence(self, type, params):
	#Upload the sequence to the QRM necessary for experiment defined in type (Raby, T1, T2...)

	#Destructoras

	def reset (self):
	#reset QRM

	def stop_sequencers(self):
	#stop current sequence running in QRM

	def close_connections(self):
	#close connection to QRM
