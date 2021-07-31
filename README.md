# AMD Curve Optimizer Utility

## Credits

This project was inspired by these fine projects from-which much of the code you'll find here has been derived:
- https://github.com/fhoekstra/thread_switcher
- https://github.com/chestm007/python-mprime

## Disclaimer

USE AT YOUR OWN RISK! The use of this project or utility should not cause harm to your computer or any component(s). However, the project author nor the project maintainers make any guarantees against such harm and therefor cannot and will not be held liable for any damages. This project should not be considered conclusive evidince to the stability of any particular system tuning or configuration.

## Installation

### Easy Install

Installation is streamlined by the use of the install.sh script which you can execute simply:
```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/travisdieckmann/curve_optimizer_util/main/tools/install.sh)"
```

### Manual Install

Install mprime:
```shell
mkdir -p ~/.local/share/mprime
cd ~/.local/share/mprime
curl http://www.mersenne.org/ftp_root/gimps/p95v303b6.linux64.tar.gz -o p95v303b6.linux64.tar.gz
tar -xzf p95v303b6.linux64.tar.gz
cd ~/.local/bin
ln -s ../share/mprime/mprime mprime
cd ${start_dir}
```

Install python-mprime:
```shell
pip install -q git+https://github.com/travisdieckmann/python-mprime.git@0366b1ef0910cb135705a3cffd01459ae2b85711
```

Install curve_optimizer_util:
```shell
pip install -q git+https://github.com/travisdieckmann/curve_optimizer_util.git
```

## Usage

Start AMD Curve Optimizer Utility on your command prompt:
```shell
curve-optimizer-util
```

## Contributing

Feel free to fork and open a pull-request back to this project!
