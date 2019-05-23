# py3-openstudio-linux-sdk [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/arif-hanif/py3-openstudio-linux-sdk/blob/master/LICENSE) [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Build Status](https://travis-ci.org/arif-hanif/py3-openstudio-linux-sdk.svg?branch=master)](https://travis-ci.org/arif-hanif/py3-openstudio-linux-sdk)
Package the python bindings for openstudio for linux in python 3.

### todo
- [ ] add dockerfile to compile bindings
- [ ] add clean up python script to fix py3 relative imports
- [ ] package bundle
- [ ] how to build bindings using docker
- [ ] add tests
- [ ] add sample use of sdk
- [ ] example use of sdk and CLI in docker
- [ ] how to track versions with openstudio versions

## Installation
This package is only built for linux.
```
pip install py3_openstudio_linux_sdk
```

## Example

```
import py3_openstudio_linux_sdk as openstudio

# Generate an osm model
model = openstudio.model.Model()
space = openstudio.model.Space(model)
space.setName("New Space")

for s in openstudio.model.getSpaces(model):
    print(s)
    
# Load a osm model
osmpath = openstudio.toPath("/path/to/osm/in.osm")
model = openstudio.model.Model.load(osmpath).get()
```

## Troubleshooting
#### 1. ImportError: libopenstudio_airflow_static.so: cannot open shared object file: No such file or directory
Ensure you are using Python 3.6 and add the python bindings path to the LD_LIBRARY_PATH environmental variable in linux: 
```
export LD_LIBRARY_PATH=/usr/src/openstudio:$LD_LIBRARY_PATH
```

### Credits

- [Julien Marrec](https://github.com/jmarrec)
- [Saeran Vasanthakumar](https://github.com/saeranv)
