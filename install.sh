#!/bin/bash

install_core_dep() {
  echo "Installing core dependencies  poerty"
  # pip install poetry==1.1.10 -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
}

usage() {
   echo "Usage:"
   echo "source ./install.sh [full|test|minimal]"
   echo ""
}

case $1 in
  "minimal")
    install_core_dep
    echo "Installing minimal requirements"
    poetry install --no-dev -vvv
    source .venv/bin/activate
    ;;
  "test")
    install_core_dep
    echo "Installing test requirements"
    poetry install -vvv
    source .venv/bin/activate
    ;;
  "full"|"")
    #Default to "full" if no arguments are given
    install_core_dep
    echo "Installing all requirements"
    poetry install -vvv
    source .venv/bin/activate
    #Additional packages used during development, but not needed to execute code
    echo "Installing development requirements"
    pip install -U pre-commit black==20.8b0 flake8==4.0.1 isort==5.9.3 -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
    pre-commit install

    export PYTHONPATH=$PYTHONPATH:$PWD
    ;;
  *)
    usage
    ;;
esac
