# muestreopython
import pandas as pd
import numpy as np
import scipy.stats as st
z=st.norm.ppf(1-0.05/2)
N=len(data.index)
numera=(z*z)*N*(0.5*0.5); denomina=(0.05*0.05*(N-1))+(z*z)*(0.5*0.5)
tamuestra=int(numera/denomina)
print(tamuestra)
