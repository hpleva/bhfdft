#import numpy
from setuptools import setup
#from distutils.extension import Extension
#from Cython.Distutils import build_ext
# from Cython.Build import cythonize

"""
ext_modules = [Extension(
    name="bhfdft",
    sources=[""],
    include_dirs=[numpy.get_include()],
    language="c++",
    extra_compile_args="-fopenmp".split(),
    )]
"""

setup(
    name="bhfdft",
    version=0.5,
    description="(Non)relativistic HF/DFT atomic solver using a B-spline basis",
    author="hpleva",
    author_email="henrik.levamaki@gmail.com",
    license="MIT",
    packages=["bhfdft"],
    #package_data={"pyemto.emto_parser": ["*.json", "LICENSE.txt"],
    #               "pyemto": ["contributors.txt", "Documentation.html"]},
    #install_requires=["numpy>=1.10.3", "scipy>=0.17.1", "matplotlib>=1.5.1"],
    #extras_require={"emto_parser": ["pandas>=0.20.3"],
    #                "emto_input_generator": ["pymatgen>=4.4.0"]},
    #cmdclass={'build_ext': build_ext},
    #ext_modules=ext_modules,
    #setup_requires=['pytest-runner', ...],
    #tests_require=['pytest', ...],
    )
