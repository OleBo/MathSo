# General Purpose
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# Jupyter Specifics
from IPython.display import HTML
from ipywidgets.widgets import interact, IntRangeSlider, FloatSlider, Layout

#%matplotlib inline

style = {'description_width': '150px'}
slider_layout = Layout(width='99%')

def main(p = 0.4, q = 0.04, r = 0.02, s = 2, y0_0 = 105, y0_1 = 8, range = [0, 15]):

    f = lambda t, y: [p*y[0] - q*y[0]*y[1], r*y[0]*y[1] - s*y[1]]
    lv=solve_ivp(f,range,[y0_0,y0_1],method='DOP853',t_eval=np.linspace(range[0],range[1],200))

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax1.plot(lv.t   ,lv.y[0,:] , label=r'rabits')
    ax1.plot(lv.t   ,lv.y[1,:] , label=r'foxes')
    ax1.legend()
    ax1.set_title('Lotka-Volterra model: population over time')
    ax1.set_xlabel('time')
    ax1.set_ylabel('population')

    ax2.plot(lv.y[0,:]   ,lv.y[1,:] , label=r'rabits vs foxes')
    ax2.legend()
    ax2.set_title('Lotka-Volterra model: population cycles')
    ax2.set_xlabel('rabits')
    ax2.set_ylabel('foxes')

    plt.show()

def interactive():
    interact(main, 
        p=FloatSlider(min=0, max=24, step=0.01, value=0.4, description='Birth Rate of Rabbits', style=style, layout=slider_layout),
        q=FloatSlider(min=0, max=24, step=0.01, value=0.04, description='Death Rate of Rabbits', style=style, layout=slider_layout),
        r=FloatSlider(min=0, max=24, step=0.01, value=0.02, description='Birth Rate of Foxes', style=style, layout=slider_layout),
        s=FloatSlider(min=0, max=24, step=0.01, value=2., description='Death Rate of Foxes', style=style, layout=slider_layout),
        y0_0=FloatSlider(min=1, max=200, step=1, value=105., description='Initial population Rabbits', style=style, layout=slider_layout),
        y0_1=FloatSlider(min=1, max=100, step=1, value=8., description='Initial population Foxes', style=style, layout=slider_layout),
        range=IntRangeSlider(min=0 ,max=50 , step=1, value=[0, 15], description='time interval', style=style, layout=slider_layout),
    );

if __name__ == "__main__":
    # execute only if run as a script
    interactive()