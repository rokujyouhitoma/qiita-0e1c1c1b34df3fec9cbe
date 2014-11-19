from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("train", ["train.pyx"])]

setup(
  name = 'Train App',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)
