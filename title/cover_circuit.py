import numpy as np
import gdsCAD as cad
from stcad.source_dev.chip import Base_Chip
from stcad.source_dev.rf_dcbias_gate import RFShuntGate
import stcad.source_dev.rf_feedlines as feedline

######## Initialize chip
chip = Base_Chip('cover_circuit',
                 xdim=5e3,
                 ydim=2e3,
                 frame=True,
                 label=False,
                 boxwidth=100)

feedwidth = 12
gapwidth = 5
######## add launchers and feedline
launchdist = 6950 / 2
dict_feedline = {
    'length': launchdist,
    'feedwidth': feedwidth,
    'gapwidth': gapwidth,
    'launchl': 400,
    'launchgapx': 400,
    'curved': False,
    'orientation': 'up',
    'layer': 1
}

name = 'Launchers'
rffeedline = feedline.Feedline(name, dict_feedline, feedline=False)
rf_feed_hor = rffeedline.gen_feedline()

chip.add_component(rf_feed_hor, (0, 0))

### Define shunt cavity part
dict_cavity = {
    'length': 10e3,
    'feedlength': 200,
    'centerwidth': feedwidth,
    'gapwidth': gapwidth,
    'shunt': (155, 300, 310, 500, 300, 480),
    'holedim': (80, 70),
    'position': (-launchdist / 2., 0),
    'nbends': 3,
    'launchdist': launchdist,
    'shuntgate': True,
    'gatestub': 100,
    'ymax': 20e3
}
# to calculate the available space into which to fit the resonator
dict_cavity['xmax'] = launchdist - dict_cavity['feedlength'] - dict_cavity[
    'shunt'][0] - dict_cavity['holedim'][0]

name_cav = 'Shunt cavity'
cav = RFShuntGate(name_cav, dict_cavity, shunttype=0, label=True)
cav1 = cav.gen_partial(loc='top')

chip.add_component(cav1)

#### Export
chip.save_to_gds(show=False, save=True, loc='./')
