from pycbc.waveform import get_td_waveform


class lisa_waveform(HpHc):

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
                
        hp, hc = get_td_waveform(**self.source_parameters)
        tm = hp.sample_times.numpy() + self.source_parameters['tc']
        hp, hc = self.source2SSB(hp, hc)
        self._interp_hphc(tm, hp, hc, t, kind="spline")
        
        return (self.hp, self.hc)
        
        



