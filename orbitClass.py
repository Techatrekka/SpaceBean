from astropy import units as u
from astropy.time import Time, TimeDelta
from poliastro.bodies import Earth, Jupiter, Sun
from poliastro.twobody import Orbit
from poliastro.threebody import restricted
from poliastro.ephem import Ephem
from poliastro.plotting.static import StaticOrbitPlotter
from poliastro.frames import Planes
from poliastro.plotting import StaticOrbitPlotter
from poliastro.plotting.misc import plot_solar_system
from poliastro.util import norm, time_range
from matplotlib import pyplot as plt
import numpy as np


class OrbitClass:
    
    C_DEFAULT_RADIUS = 1
    C_DEFAULT_ANGLE = 0
    EPOCH = Time("2021-10-02 15:00", scale="tdb")
    def __init__(self):
        self.set_asteroid()
        self.set_earth()
        self.plotter = StaticOrbitPlotter()
        self.plotter.set_attractor(Sun)
        self.render_plot()
    #function to create an asteroid with
    def set_asteroid(self,radius=C_DEFAULT_RADIUS,phase=0):
        semiMaj = radius*u.AU
        ecc = 0 *u.one
        incl = 0 *u.deg
        raan = 0 *u.deg
        argp = 0 *u.deg
        nu = phase*u.deg
        orb = Orbit.from_classical(Sun, semiMaj, ecc, incl, raan, argp, nu)
        self.asteroid =orb 
        return

    def set_earth(self, phase = 0):
        self.earth = Ephem.from_body(Earth,self.EPOCH)
        self.EarOrb = Orbit.from_ephem(Sun, self.earth, self.EPOCH)
        return

    def render_plot(self):

        #plotter.set_body_frame(Jupiter)
        #plt.cla()
        self.plotter = StaticOrbitPlotter()
        self.plotter.set_attractor(Sun)
        self.plotter.plot(self.asteroid, color="#A32")
        self.plotter.plot(self.EarOrb, color ="#00C")

        ax = plt.gca()
        ax.get_legend().remove()
        plt.savefig("OrbitPol.png", bbox_inches="tight")
        plt.close()
        #plt.render_plot().savefig("OrbitPol")
        return
        
        
    def get_angle(self):
        refvec = [1,0,0]
        AstPos=self.asteroid.rv()
        EarPos=self.EarOrb.rv()
        DiffVec = AstPos[0] - EarPos[0]

        crossprod = np.cross(AstPos[0],DiffVec)
	#print(crossprod)
        chirality = -1
        #print( np.dot(crossprod,refvec).value)
        if(np.dot(crossprod,refvec).value <= 0):
            chirality =1
        
        AstDot = 0
        for i in range(0,2):
            AstDot += AstPos[0][i] * DiffVec[i]
        cosIn = AstDot/(norm(AstPos[0])*norm(DiffVec))
        angle = chirality*np.arccos(cosIn)
        

        return angle.value
    
    def get_sun_coords(self):
        ang = self.get_angle()
        return (20*np.cos(ang),0,20*np.sin(ang))     
    
    
def test_code():
    x = OrbitClass()
    x.set_earth()
    x.set_asteroid(phase=1.5*np.pi)
    print(x.get_angle())
    print(x.get_sun_coords())
    x.render_plot().savefig("OrbitPol_%s.png"%(str(1).zfill(8)))

#test_code()
