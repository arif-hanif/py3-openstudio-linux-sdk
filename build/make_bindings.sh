#!/bin/bash

make -j 2

catchIddFactoryError() {
  make GenerateIddFactory
  make GenerateIddFactoryRun
  make -j 2
}

trap "catchIddFactoryError" ERR

return

catchIddFactoryError

cp ./Products/python/*.so ./python_wrapper/generated_sources

python3 ./fix_python3_imports.py
