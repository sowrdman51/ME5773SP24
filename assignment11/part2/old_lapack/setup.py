from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np

mkl_include_dir = '/apps/intel/oneapi/mkl/latest/include'  # Adjust as necessary

ext_modules = [
    Extension(
        'module',
        sources=['module.pyx'],
        include_dirs=[np.get_include(), mkl_include_dir],
        libraries=['mkl_rt'],  # Depending on your MKL setup, this might need adjustment
        extra_compile_args=['-m64', '-mkl'],
        extra_link_args=['-m64', '-lmkl_rt']
    )
]

setup(
    name='CythonMKLMODULE',
    ext_modules=cythonize(ext_modules)
)
