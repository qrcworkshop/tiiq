'''
experimento.py (Rabi, T1...)
- Defines variable (settings HW, parametros de waveforms para QRM, QCM)
- Defines secuencia QRM y QCM --> Rabi_seq (Joel trabajando)
- Instancias instrument controller(params)
- ic.setup(parametros)
- ic.upload_waveforms_sequence(params)
- ic.play()
	- ejecutar waves en HW
	- plotting en tiempo real 
 
ic.stop
ic.exit

plot resultados
'''
from tiiq.instruments.instrument_controller import InstrumentController

ic = InstrumentController()

QRM_settings = {
	"data_dictionary": "quantify-data/",
	"ref_clock": "external",
	"start_sample": 130,
	"hardware_avg": 1024,
	"integration_length": 600,
	"sampling_rate": 1e9,
	"mode": "ssb"
        }
ic.setup(LO_qcm_freq= 8.3e9, LO_qcm_power= 10, LO_qrm_freq= 7.778e9, LO_qrm_power=13, QRM_settings= QRM_settings)
