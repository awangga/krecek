#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 06:19:33 2019

@author: awangga
from paper
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4485252/
docs
https://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html
https://nipy.org/nibabel/nifti_images.html


./vim3/crcns_vim-3/data/ p1001-p1011
nii and npy file
"""
# In[1]:
import numpy as np
import config as c
import nibabel as nib
# In[2]:
img = nib.load(c.dir+'/p1001/p1001_2_MM_166_DYN_SENSE_3_1.nii')
img.shape
# In[3]:
img.get_data_dtype()
# In[4]:
hdr=img.header
print(hdr)
hdr.get_xyzt_units()
# In[5]:

isinya=np.load(c.dir+'/p1001/p1001_ul_sens_fmri_run_01_seq.npy')

# In[6]: