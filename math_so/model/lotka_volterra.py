"""This module implements the Lotka/Volterra (predator-prey) model."""
# pylint: disable=too-many-arguments
# General Purpose
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# Jupyter Specifics
from ipywidgets.widgets import interact, IntRangeSlider, FloatSlider, Layout

style = {'description_width': '150px'}
slider_layout = Layout(width='99%')


def main(alpha=0.4, beta=0.04, gamma=0.02, delta=2, y0_0=105, y0_1=8,
         my_range=None):
    r"""Lotka-Voltera model

    Lotka–Volterra model is a pair of first-order nonlinear differential
    equations, frequently used to describe the dynamics of biological systems
    in which two species interact, one as a predator and the other as prey. The
    populations change through time according to the pair of equations:

    .. math:: \frac{dy_1}{dt} &= \alpha y_1 - \beta y_1 y_2
    .. math:: \frac{dy_2}{dt} &= \gamma y_1 y_2 - \delta y_2

    where
    - :math `y_1` is the number of prey (for example, rabbits);
    - :math `y_2` is the number of some predator (for example, foxes);
    - :math `\frac{dy_1}{dt}` and :math `\frac{dy_2}{dt}` represent the
    instantaneous growth rates of the two populations;
    - :math `\alpha,\beta,\gamma,\delta` are positive real parameters
    describing the interaction of the two species.

    Parameters
    ----------

    alpha : number
        prey growth
    beta : number
        prey predation
    gamma : number
        predator growth
    delta : number
        predator loss
    y0_0 : number
           initial prey population
    y0_1 : number
           initial predator population
    my_range : array
               integration range

    Returns
    -------

    graph object
    """
    if my_range is None:
        my_range = [0, 15]

    lvm = solve_ivp(
        lambda t, y:
            [alpha*y[0] - beta*y[0]*y[1], gamma*y[0]*y[1] - delta*y[1]],
        my_range,
        [y0_0, y0_1],
        method='DOP853',
        t_eval=np.linspace(my_range[0], my_range[1], 200)
    )

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax1.plot(lvm.t, lvm.y[0, :], label='prey')
    ax1.plot(lvm.t, lvm.y[1, :], label='predator')
    ax1.legend()
    ax1.set_title('population over time')
    ax1.set_xlabel('time')
    ax1.set_ylabel('population')

    ax2.plot(lvm.y[0, :], lvm.y[1, :], label='predator vs prey')
    ax2.plot(delta/gamma, alpha/beta, 'o', label='fix point')
    ax2.legend(loc='lower right')
    ax2.set_title('phase space')
    ax2.set_xlabel('prey')
    ax2.set_ylabel('predator')
    fig.suptitle('Lotka-Volterra model')

    plt.show()


def interactive():
    """ interactive call of `main`
    """
    interact(main,
             alpha=FloatSlider(min=0.01, max=24, step=0.01, value=0.4,
                               description='Birth Rate of Prey',
                               style=style, layout=slider_layout),
             beta=FloatSlider(min=0.01, max=24, step=0.01, value=0.04,
                              description='Death Rate of Prey',
                              style=style, layout=slider_layout),
             gamma=FloatSlider(min=0.01, max=24, step=0.01, value=0.02,
                               description='Birth Rate of Predator',
                               style=style, layout=slider_layout),
             delta=FloatSlider(min=0.01, max=24, step=0.01, value=2.,
                               description='Death Rate of Predator',
                               style=style, layout=slider_layout),
             y0_0=FloatSlider(min=0.01, max=200, step=0.01, value=105.,
                              description='Initial population Prey',
                              style=style, layout=slider_layout),
             y0_1=FloatSlider(min=0.01, max=100, step=0.01, value=8.,
                              description='Initial population Predator',
                              style=style, layout=slider_layout),
             my_range=IntRangeSlider(min=0, max=50, step=1, value=[0, 15],
                                     description='time interval',
                                     style=style, layout=slider_layout),
             )


if __name__ == "__main__":
    # execute only if run as a script
    interactive()
