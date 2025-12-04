from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension
import glob
import os

# setup.py directory
ROOT = os.path.dirname(__file__)

EXT_REL = os.path.join("pointnet2", "_ext-src")
EXT_ABS = os.path.join(ROOT, EXT_REL)

sources = (
    glob.glob(os.path.join(EXT_REL, "src", "*.cpp")) +
    glob.glob(os.path.join(EXT_REL, "src", "*.cu"))
)

setup(
    ext_modules=[
        CUDAExtension(
            name="pointnet2._ext",
            sources=sources,                 # RELATIVE paths (required)
            include_dirs=[
                os.path.join(EXT_ABS, "include"),  # ABSOLUTE paths (allowed)
            ],
            extra_compile_args={
                "cxx": ["-O2"],
                "nvcc": ["-O2"],
            },
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
