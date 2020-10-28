# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from glob import glob
import nrrd #pip install pynrrd, if pynrrd is not already installed
import nibabel as nib #pip install nibabel, if nibabel is not already installed
import numpy as np

baseDir = os.path.normpath('E:/slicer/')
files = glob(baseDir+'/*.nrrd')

for file in files:
#load nrrd 
  _nrrd = nrrd.read(file)
  data = _nrrd[0]
  header = _nrrd[1]

#save nifti
  img = nib.Nifti1Image(data, np.eye(4))
  nib.save(img,os.path.join(baseDir, file+'.nii.gz')) 