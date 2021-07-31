from distutils.core import setup

with open("README.md") as f:
    readme = f.read()


setup(
    name="curve_optimizer_util",
    version="0.0.1",
    packages=["curve_optimizer_util"],
    url="https://github.com/travisdieckmann/curve_optimizer_util",
    license="GPL-2.0",
    author="Travis Dieckmann",
    author_email="tadieckmann@gmail.com",
    maintainer="Travis Dieckmann",
    maintainer_email="tadieckmann@gmail.com",
    description="AMD Curve Optimizer Test and Tune Utility",
    long_description=readme,
    install_requires=[],
    entry_points="""
        [console_scripts]
        curve_optimizer_util=curve_optimizer_util.main:main
    """,
)
