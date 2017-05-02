import skidl
from ..library import altera_sklib

class max10(object):
    def __init__(self, partnumber):
        assert partnumber.upper()=='10M02SCE144', 'Part Number not supported'

    def circuit(self, port):
        circuit_nets = {}
        gnd = skidl.Net('GND')
        decoupling_caps = []
        fpga = skidl.Part(lib=altera_sklib.altera,
                name='10M02SCE',
                footprint='EQFP144')
        #Power related pins
        for pin in fpga.pins:
            if "GND" in pin.name:
                pin += gnd
            elif "VCC" in pin.name:
                if pin.name not in circuit_nets.keys():
                    circuit_nets[pin.name] = skidl.Net(pin.name)
                decoupling_caps.append(skidl.Part('device', 'C',
                    value='100n', footprint='Capacitors_SMD:C_0805'))
                pin += circuit_nets[pin.name]
                decoupling_caps[-1][1] += circuit_nets[pin.name]
                decoupling_caps[-1][2] += gnd

