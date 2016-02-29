# -*- coding: utf-8 -*-
import os
import time
import numpy as np
import ctypes

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colorbar as clb
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


# ++++ Fortran function for plastic deformation ++++
import irreverisble


def plotSingle2D(comp,xtitle,ytitle,xscale,yscale):

	exp = []                           # ***** target 
	exp = np.loadtxt('ref/850-30.dat')

	fig, ax = plt.subplots(figsize=(12, 9))

	ax.plot(comp[:,0],comp[:,1],lw=3)
	ax.scatter(exp[:,0]*100, exp[:,1],s=100,zorder=5)

	ax.set_xlabel(xtitle, fontsize=35, labelpad=15)
	ax.set_ylabel(ytitle, fontsize=35, labelpad=15)
	ax.tick_params(axis='x', labelsize=25, pad = 10)
	ax.tick_params(axis='y', labelsize=25, pad = 10)

	ax.set_xscale(xscale, nonposx='clip')
	ax.set_yscale(yscale, nonposx='clip')

	ax.grid(True)
	fig.tight_layout()
	plt.show()


# --------------- material properties
T_service = 1123 
prec_stress = 50 
SS_stress = 400

# -------------- number samples, =1 in this case
no_samples = 1

# ============================== objective
# optimize these two parameters (model_parameters)
# to minimize the error between [exp] and [stress_strain]
# ==============================
model_parameters = (-180, 3.077) 


# the function, irreverisble.mechanics, is used to calculate the stress-strain curve in plastic deforamtion region 
# the outputs are 2D list (stress-strain, stress_strain) and 1 parameter (work to necking, WTN)
stress_strain, WTN = irreverisble.mechanics(prec_stress,SS_stress,T_service,model_parameters,no_samples)
stress_strain = np.array(np.trim_zeros(stress_strain)).reshape(-1,2)


plotSingle2D(stress_strain,'strain','stress','linear','linear')


