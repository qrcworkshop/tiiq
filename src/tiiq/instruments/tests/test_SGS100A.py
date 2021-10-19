from qiboicarusq.instruments_TII.RohdeSchwarz_SGS100A import RohdeSchwarz_SGS100A

LO_qrm = RohdeSchwarz_SGS100A("LO_qrm", 'TCPIP0::192.168.0.7::inst0::INSTR')
LO_qrm.set_power(15)
LO_qrm.set_frequency(7.789e9)
LO_qrm.on()

print (LO_qcm.getName())
print (LO_qcm.getIP())
print (LO_qcm.getPower())
print (LO_qcm.getFrequency())

LO_qcm = RohdeSchwarz_SGS100A("LO_qcm", 'TCPIP0::192.168.0.8::inst0::INSTR')
LO_qcm.set_power(12)
LO_qcm.set_frequency(8.9e9)
LO_qcm.on()

print (LO_qcm.getName())
print (LO_qcm.getIP())
print (LO_qcm.getPower())
print (LO_qcm.getFrequency())