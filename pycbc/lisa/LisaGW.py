from ldc.waveform.waveform import HpHc    

class LisaGW(HpHc):
    
    
    def __init__(self, p):
        self.source_name = 'test'
        self.source_type = '?'
        self.approximant = 'whatever'
        self.reference_frame = "SSB" # default
        self.p = p
        self.set_param(self.p)
        
    def check_param(self):
        pass
    
    def info(self):
        
        """ Return default units
        """
        
        units = {'EclipticLatitude': 'rad',
                 'EclipticLongitude': 'rad',
                 'mass1': 'Msun',
                 'mass2': 'Msun',
                 'tc': 's',
                 }
        
        return units
    
    def compute_hphc_td(self, t):
                
        from pycbc.waveform import get_td_waveform
        
        hp, hc = get_td_waveform(**self.source_parameters)
        tm = hp.sample_times.numpy() + self.source_parameters['tc']
        hp, hc = self.source2SSB(hp, hc)
        self._interp_hphc(tm, hp, hc, t, kind="spline")
        
        return (self.hp, self.hc)
        
        
class LisaProjectedGW:

    def __init__(self, config):

        from ldc.lisa.orbits import Orbits
        from ldc.lisa.projection import ProjectedStrain
        
        self.config = config
        self.lisa_orbits = Orbits.type(self.config)
        self.projector = ProjectedStrain(self.lisa_orbits)




        



