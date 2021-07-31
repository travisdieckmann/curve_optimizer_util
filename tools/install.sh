#!/usr/bin/env bash

echo "Installing Curve Optimizer Utility..."
start_dir=$(pwd)

echo "Download and install mprime"
mkdir -p ~/.local/share/mprime
cd ~/.local/share/mprime
curl http://www.mersenne.org/ftp_root/gimps/p95v303b6.linux64.tar.gz -o p95v303b6.linux64.tar.gz
tar -xzf p95v303b6.linux64.tar.gz
cd ~/.local/bin
ln -s ../share/mprime/mprime mprime
cd ${start_dir}

echo "Install Python dependencies"
pip install -q git+https://github.com/travisdieckmann/python-mprime.git@0366b1ef0910cb135705a3cffd01459ae2b85711
pip install -q git+https://github.com/travisdieckmann/curve_optimizer_util.git

echo "Curve Optimizer Utility is now installed!"