#!/bin/bash

cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_OS_APP=OFF \
    -DPYTHON_EXECUTABLE=/usr/bin/python3.6 \
    -DBUILD_PYTHON_BINDINGS=ON \
    ../openstudiocore

make -j 4

catchIddFactoryError() {
  make GenerateIddFactory
  make GenerateIddFactoryRun
  make -j 4
}

trap "catchIddFactoryError" ERR

return

catchIddFactoryError

# Are static libraries required?
cp ./Products/python/*.so ./python_wrapper/generated_sources
cp ./__init__.py ./python_wrapper/generated_sources/__init__.py

python3 ./fix_python3_imports.py
