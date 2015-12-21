# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 00:30:38 2015

@author: daudt
"""

import numpy as np
import skimage as sk
import skimage.io as io
import skimage.filters as fil
import skimage.morphology as morph

# Load images
lena = sk.img_as_float(io.imread('../../lena.bmp'))
lena_uni = sk.img_as_float(io.imread('../../lena_uni.bmp'))
lena_nor = sk.img_as_float(io.imread('../../lena_nor.bmp'))
lena_ric = sk.img_as_float(io.imread('../../lena_ric.bmp'))
lena_sp = sk.img_as_float(io.imread('../../lena_sp.bmp'))

cameraman = sk.img_as_float(io.imread('../../cameraman.bmp'))
cameraman_uni = sk.img_as_float(io.imread('../../cameraman_uni.bmp'))
cameraman_nor = sk.img_as_float(io.imread('../../cameraman_nor.bmp'))
cameraman_ric = sk.img_as_float(io.imread('../../cameraman_ric.bmp'))
cameraman_sp = sk.img_as_float(io.imread('../../cameraman_sp.bmp'))

baboon = sk.img_as_float(io.imread('../../baboon.bmp'))
baboon_uni = sk.img_as_float(io.imread('../../baboon_uni.bmp'))
baboon_nor = sk.img_as_float(io.imread('../../baboon_nor.bmp'))
baboon_ric = sk.img_as_float(io.imread('../../baboon_ric.bmp'))
baboon_sp = sk.img_as_float(io.imread('../../baboon_sp.bmp'))

# Kernel
k = morph.disk(2)+0.0 # +0.0 transforms k into float64

# Apply filters
lena_uni_f = sk.img_as_float(fil.rank.mean(lena_uni,k))
lena_nor_f = sk.img_as_float(fil.rank.mean(lena_nor,k))
lena_ric_f = sk.img_as_float(fil.rank.mean(lena_ric,k))
lena_sp_f = sk.img_as_float(fil.rank.mean(lena_sp,k))

cameraman_uni_f = sk.img_as_float(fil.rank.mean(cameraman_uni,k))
cameraman_nor_f = sk.img_as_float(fil.rank.mean(cameraman_nor,k))
cameraman_ric_f = sk.img_as_float(fil.rank.mean(cameraman_ric,k))
cameraman_sp_f = sk.img_as_float(fil.rank.mean(cameraman_sp,k))

baboon_uni_f = sk.img_as_float(fil.rank.mean(baboon_uni,k))
baboon_nor_f = sk.img_as_float(fil.rank.mean(baboon_nor,k))
baboon_ric_f = sk.img_as_float(fil.rank.mean(baboon_ric,k))
baboon_sp_f = sk.img_as_float(fil.rank.mean(baboon_sp,k))

# Calculate MSE
lena_uni_mse = np.mean(np.square(lena_uni_f-lena))
lena_nor_mse = np.mean(np.square(lena_nor_f-lena))
lena_ric_mse = np.mean(np.square(lena_ric_f-lena))
lena_sp_mse = np.mean(np.square(lena_sp_f-lena))

cameraman_uni_mse = np.mean(np.square(cameraman_uni_f-cameraman))
cameraman_nor_mse = np.mean(np.square(cameraman_nor_f-cameraman))
cameraman_ric_mse = np.mean(np.square(cameraman_ric_f-cameraman))
cameraman_sp_mse = np.mean(np.square(cameraman_sp_f-cameraman))

baboon_uni_mse = np.mean(np.square(baboon_uni_f-baboon))
baboon_nor_mse = np.mean(np.square(baboon_nor_f-baboon))
baboon_ric_mse = np.mean(np.square(baboon_ric_f-baboon))
baboon_sp_mse = np.mean(np.square(baboon_sp_f-baboon))

# Calculate PSNR
lena_uni_psnr = 10*np.log10(1/lena_uni_mse)
lena_nor_psnr = 10*np.log10(1/lena_nor_mse)
lena_ric_psnr = 10*np.log10(1/lena_ric_mse)
lena_sp_psnr = 10*np.log10(1/lena_sp_mse)

cameraman_uni_psnr = 10*np.log10(1/cameraman_uni_mse)
cameraman_nor_psnr = 10*np.log10(1/cameraman_nor_mse)
cameraman_ric_psnr = 10*np.log10(1/cameraman_ric_mse)
cameraman_sp_psnr = 10*np.log10(1/cameraman_sp_mse)

baboon_uni_psnr = 10*np.log10(1/baboon_uni_mse)
baboon_nor_psnr = 10*np.log10(1/baboon_nor_mse)
baboon_ric_psnr = 10*np.log10(1/baboon_ric_mse)
baboon_sp_psnr = 10*np.log10(1/baboon_sp_mse)

# Save images
io.imsave('lena_uni_f.bmp',lena_uni_f)
io.imsave('lena_nor_f.bmp',lena_nor_f)
io.imsave('lena_ric_f.bmp',lena_ric_f)
io.imsave('lena_sp_f.bmp',lena_sp_f)

io.imsave('cameraman_uni_f.bmp',cameraman_uni_f)
io.imsave('cameraman_nor_f.bmp',cameraman_nor_f)
io.imsave('cameraman_ric_f.bmp',cameraman_ric_f)
io.imsave('cameraman_sp_f.bmp',cameraman_sp_f)

io.imsave('baboon_uni_f.bmp',baboon_uni_f)
io.imsave('baboon_nor_f.bmp',baboon_nor_f)
io.imsave('baboon_ric_f.bmp',baboon_ric_f)
io.imsave('baboon_sp_f.bmp',baboon_sp_f)