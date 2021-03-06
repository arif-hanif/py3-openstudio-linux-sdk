# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_openstudioisomodel', [dirname(__file__)])
        except ImportError:
            import _openstudioisomodel
            return _openstudioisomodel
        if fp is not None:
            try:
                _mod = imp.load_module('_openstudioisomodel', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _openstudioisomodel = swig_import_helper()
    del swig_import_helper
else:
    import _openstudioisomodel
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _openstudioisomodel.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _openstudioisomodel.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _openstudioisomodel.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _openstudioisomodel.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _openstudioisomodel.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _openstudioisomodel.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _openstudioisomodel.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _openstudioisomodel.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _openstudioisomodel.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _openstudioisomodel.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _openstudioisomodel.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _openstudioisomodel.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _openstudioisomodel.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _openstudioisomodel.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _openstudioisomodel.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _openstudioisomodel.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _openstudioisomodel.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _openstudioisomodel.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_openstudioisomodel.SHARED_PTR_DISOWN_swigconstant(_openstudioisomodel)
SHARED_PTR_DISOWN = _openstudioisomodel.SHARED_PTR_DISOWN
from .import openstudioutilities
from .import openstudioutilitiescore
from .import openstudioutilitiestime
from .import openstudioutilitiesdata
from .import openstudioutilitiesunits
from .import openstudioutilitiesplot
from .import openstudioutilitiesgeometry
from .import openstudioutilitiessql
from .import openstudioutilitiesbcl
from .import openstudioutilitiesidd
from .import openstudioutilitiesidf
from .import openstudioutilitiesfiletypes
from .import openstudiomodel
from .import openstudiomodelcore
from .import openstudiomodelsimulation
from .import openstudiomodelresources
from .import openstudiomodelgeometry
from .import openstudiomodelhvac
from .import openstudiomodelzonehvac
from .import openstudiomodelavailabilitymanager
from .import openstudiomodelplantequipmentoperationscheme
from .import openstudiomodelstraightcomponent
from .import openstudiomodelairflow
from .import openstudiomodelrefrigeration
from .import openstudiomodelgenerators

def div(*args) -> "openstudio::Vector":
    return _openstudioisomodel.div(*args)
div = _openstudioisomodel.div

def sum(*args) -> "openstudio::Vector":
    return _openstudioisomodel.sum(*args)
sum = _openstudioisomodel.sum

def dif(*args) -> "openstudio::Vector":
    return _openstudioisomodel.dif(*args)
dif = _openstudioisomodel.dif

def maximum(*args) -> "double":
    return _openstudioisomodel.maximum(*args)
maximum = _openstudioisomodel.maximum

def minimum(*args) -> "double":
    return _openstudioisomodel.minimum(*args)
minimum = _openstudioisomodel.minimum

def abs(v1: 'Vector') -> "openstudio::Vector":
    return _openstudioisomodel.abs(v1)
abs = _openstudioisomodel.abs

def pow(v1: 'Vector', xp: 'double const') -> "openstudio::Vector":
    return _openstudioisomodel.pow(v1, xp)
pow = _openstudioisomodel.pow
class ISOResults(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ISOResults, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ISOResults, name)
    __repr__ = _swig_repr
    __swig_setmethods__["monthlyResults"] = _openstudioisomodel.ISOResults_monthlyResults_set
    __swig_getmethods__["monthlyResults"] = _openstudioisomodel.ISOResults_monthlyResults_get
    if _newclass:
        monthlyResults = _swig_property(_openstudioisomodel.ISOResults_monthlyResults_get, _openstudioisomodel.ISOResults_monthlyResults_set)

    def totalEnergyUse(self) -> "double":
        return _openstudioisomodel.ISOResults_totalEnergyUse(self)

    def __init__(self):
        this = _openstudioisomodel.new_ISOResults()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudioisomodel.delete_ISOResults
    __del__ = lambda self: None
ISOResults_swigregister = _openstudioisomodel.ISOResults_swigregister
ISOResults_swigregister(ISOResults)

class SimModel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SimModel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SimModel, name)
    __repr__ = _swig_repr

    def setPop(self, value: 'std::shared_ptr< Population >') -> "void":
        return _openstudioisomodel.SimModel_setPop(self, value)

    def setLocation(self, value: 'std::shared_ptr< Location >') -> "void":
        return _openstudioisomodel.SimModel_setLocation(self, value)

    def setLights(self, value: 'std::shared_ptr< Lighting >') -> "void":
        return _openstudioisomodel.SimModel_setLights(self, value)

    def setBuilding(self, value: 'std::shared_ptr< Building >') -> "void":
        return _openstudioisomodel.SimModel_setBuilding(self, value)

    def setStructure(self, value: 'std::shared_ptr< Structure >') -> "void":
        return _openstudioisomodel.SimModel_setStructure(self, value)

    def setHeating(self, value: 'std::shared_ptr< Heating >') -> "void":
        return _openstudioisomodel.SimModel_setHeating(self, value)

    def setCooling(self, value: 'std::shared_ptr< Cooling >') -> "void":
        return _openstudioisomodel.SimModel_setCooling(self, value)

    def setVentilation(self, value: 'std::shared_ptr< Ventilation >') -> "void":
        return _openstudioisomodel.SimModel_setVentilation(self, value)

    def simulate(self) -> "openstudio::isomodel::ISOResults":
        return _openstudioisomodel.SimModel_simulate(self)
    __swig_getmethods__["logChannel"] = lambda x: _openstudioisomodel.SimModel_logChannel
    if _newclass:
        logChannel = staticmethod(_openstudioisomodel.SimModel_logChannel)

    def __init__(self):
        this = _openstudioisomodel.new_SimModel()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudioisomodel.delete_SimModel
    __del__ = lambda self: None
SimModel_swigregister = _openstudioisomodel.SimModel_swigregister
SimModel_swigregister(SimModel)

def SimModel_logChannel() -> "openstudio::LogChannel":
    return _openstudioisomodel.SimModel_logChannel()
SimModel_logChannel = _openstudioisomodel.SimModel_logChannel

class UserModel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UserModel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UserModel, name)
    __repr__ = _swig_repr

    def loadWeather(self) -> "std::shared_ptr< openstudio::isomodel::WeatherData >":
        return _openstudioisomodel.UserModel_loadWeather(self)

    def load(self, t_buildingFile: 'path') -> "void":
        return _openstudioisomodel.UserModel_load(self, t_buildingFile)

    def save(self, t_buildingFile: 'path') -> "void":
        return _openstudioisomodel.UserModel_save(self, t_buildingFile)

    def toSimModel(self) -> "openstudio::isomodel::SimModel":
        return _openstudioisomodel.UserModel_toSimModel(self)

    def valid(self) -> "bool":
        return _openstudioisomodel.UserModel_valid(self)

    def weatherFilePath(self) -> "openstudio::path":
        return _openstudioisomodel.UserModel_weatherFilePath(self)

    def terrainClass(self) -> "double":
        return _openstudioisomodel.UserModel_terrainClass(self)

    def floorArea(self) -> "double":
        return _openstudioisomodel.UserModel_floorArea(self)

    def buildingHeight(self) -> "double":
        return _openstudioisomodel.UserModel_buildingHeight(self)

    def buildingOccupancyFrom(self) -> "double":
        return _openstudioisomodel.UserModel_buildingOccupancyFrom(self)

    def buildingOccupancyTo(self) -> "double":
        return _openstudioisomodel.UserModel_buildingOccupancyTo(self)

    def equivFullLoadOccupancyFrom(self) -> "double":
        return _openstudioisomodel.UserModel_equivFullLoadOccupancyFrom(self)

    def equivFullLoadOccupancyTo(self) -> "double":
        return _openstudioisomodel.UserModel_equivFullLoadOccupancyTo(self)

    def peopleDensityOccupied(self) -> "double":
        return _openstudioisomodel.UserModel_peopleDensityOccupied(self)

    def peopleDensityUnoccupied(self) -> "double":
        return _openstudioisomodel.UserModel_peopleDensityUnoccupied(self)

    def heatingOccupiedSetpoint(self) -> "double":
        return _openstudioisomodel.UserModel_heatingOccupiedSetpoint(self)

    def heatingUnoccupiedSetpoint(self) -> "double":
        return _openstudioisomodel.UserModel_heatingUnoccupiedSetpoint(self)

    def coolingOccupiedSetpoint(self) -> "double":
        return _openstudioisomodel.UserModel_coolingOccupiedSetpoint(self)

    def coolingUnoccupiedSetpoint(self) -> "double":
        return _openstudioisomodel.UserModel_coolingUnoccupiedSetpoint(self)

    def elecPowerAppliancesOccupied(self) -> "double":
        return _openstudioisomodel.UserModel_elecPowerAppliancesOccupied(self)

    def elecPowerAppliancesUnoccupied(self) -> "double":
        return _openstudioisomodel.UserModel_elecPowerAppliancesUnoccupied(self)

    def gasPowerAppliancesOccupied(self) -> "double":
        return _openstudioisomodel.UserModel_gasPowerAppliancesOccupied(self)

    def gasPowerAppliancesUnoccupied(self) -> "double":
        return _openstudioisomodel.UserModel_gasPowerAppliancesUnoccupied(self)

    def lightingPowerIntensityOccupied(self) -> "double":
        return _openstudioisomodel.UserModel_lightingPowerIntensityOccupied(self)

    def lightingPowerIntensityUnoccupied(self) -> "double":
        return _openstudioisomodel.UserModel_lightingPowerIntensityUnoccupied(self)

    def exteriorLightingPower(self) -> "double":
        return _openstudioisomodel.UserModel_exteriorLightingPower(self)

    def daylightSensorSystem(self) -> "double":
        return _openstudioisomodel.UserModel_daylightSensorSystem(self)

    def lightingOccupancySensorSystem(self) -> "double":
        return _openstudioisomodel.UserModel_lightingOccupancySensorSystem(self)

    def constantIlluminationControl(self) -> "double":
        return _openstudioisomodel.UserModel_constantIlluminationControl(self)

    def coolingSystemCOP(self) -> "double":
        return _openstudioisomodel.UserModel_coolingSystemCOP(self)

    def coolingSystemIPLVToCOPRatio(self) -> "double":
        return _openstudioisomodel.UserModel_coolingSystemIPLVToCOPRatio(self)

    def heatingEnergyCarrier(self) -> "double":
        return _openstudioisomodel.UserModel_heatingEnergyCarrier(self)

    def heatingSystemEfficiency(self) -> "double":
        return _openstudioisomodel.UserModel_heatingSystemEfficiency(self)

    def ventilationType(self) -> "double":
        return _openstudioisomodel.UserModel_ventilationType(self)

    def freshAirFlowRate(self) -> "double":
        return _openstudioisomodel.UserModel_freshAirFlowRate(self)

    def supplyExhaustRate(self) -> "double":
        return _openstudioisomodel.UserModel_supplyExhaustRate(self)

    def heatRecovery(self) -> "double":
        return _openstudioisomodel.UserModel_heatRecovery(self)

    def exhaustAirRecirculation(self) -> "double":
        return _openstudioisomodel.UserModel_exhaustAirRecirculation(self)

    def buildingAirLeakage(self) -> "double":
        return _openstudioisomodel.UserModel_buildingAirLeakage(self)

    def dhwDemand(self) -> "double":
        return _openstudioisomodel.UserModel_dhwDemand(self)

    def dhwEfficiency(self) -> "double":
        return _openstudioisomodel.UserModel_dhwEfficiency(self)

    def dhwDistributionSystem(self) -> "double":
        return _openstudioisomodel.UserModel_dhwDistributionSystem(self)

    def dhwEnergyCarrier(self) -> "double":
        return _openstudioisomodel.UserModel_dhwEnergyCarrier(self)

    def bemType(self) -> "double":
        return _openstudioisomodel.UserModel_bemType(self)

    def interiorHeatCapacity(self) -> "double":
        return _openstudioisomodel.UserModel_interiorHeatCapacity(self)

    def specificFanPower(self) -> "double":
        return _openstudioisomodel.UserModel_specificFanPower(self)

    def fanFlowControlFactor(self) -> "double":
        return _openstudioisomodel.UserModel_fanFlowControlFactor(self)

    def roofUValue(self) -> "double":
        return _openstudioisomodel.UserModel_roofUValue(self)

    def roofSHGC(self) -> "double":
        return _openstudioisomodel.UserModel_roofSHGC(self)

    def wallUvalueS(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueS(self)

    def wallUvalueSE(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueSE(self)

    def wallUvalueE(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueE(self)

    def wallUvalueNE(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueNE(self)

    def wallUvalueN(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueN(self)

    def wallUvalueNW(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueNW(self)

    def wallUvalueW(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueW(self)

    def wallUvalueSW(self) -> "double":
        return _openstudioisomodel.UserModel_wallUvalueSW(self)

    def wallSolarAbsorptionS(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionS(self)

    def wallSolarAbsorptionSE(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionSE(self)

    def wallSolarAbsorptionE(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionE(self)

    def wallSolarAbsorptionNE(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionNE(self)

    def wallSolarAbsorptionN(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionN(self)

    def wallSolarAbsorptionNW(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionNW(self)

    def wallSolarAbsorptionW(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionW(self)

    def wallSolarAbsorptionSW(self) -> "double":
        return _openstudioisomodel.UserModel_wallSolarAbsorptionSW(self)

    def wallThermalEmissivityS(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivityS(self)

    def wallThermalEmissivitySE(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivitySE(self)

    def wallThermalEmissivityE(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivityE(self)

    def wallThermalEmissivityNE(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivityNE(self)

    def wallThermalEmissivityN(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivityN(self)

    def wallThermalEmissivityNW(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivityNW(self)

    def wallThermalEmissivityW(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivityW(self)

    def wallThermalEmissivitySW(self) -> "double":
        return _openstudioisomodel.UserModel_wallThermalEmissivitySW(self)

    def windowUvalueS(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueS(self)

    def windowUvalueSE(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueSE(self)

    def windowUvalueE(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueE(self)

    def windowUvalueNE(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueNE(self)

    def windowUvalueN(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueN(self)

    def windowUvalueNW(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueNW(self)

    def windowUvalueW(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueW(self)

    def windowUvalueSW(self) -> "double":
        return _openstudioisomodel.UserModel_windowUvalueSW(self)

    def windowSHGCS(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCS(self)

    def windowSHGCSE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCSE(self)

    def windowSHGCE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCE(self)

    def windowSHGCNE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCNE(self)

    def windowSHGCN(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCN(self)

    def windowSHGCNW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCNW(self)

    def windowSHGCW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCW(self)

    def windowSHGCSW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSHGCSW(self)

    def windowSCFS(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFS(self)

    def windowSCFSE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFSE(self)

    def windowSCFE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFE(self)

    def windowSCFNE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFNE(self)

    def windowSCFN(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFN(self)

    def windowSCFNW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFNW(self)

    def windowSCFW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFW(self)

    def windowSCFSW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSCFSW(self)

    def windowSDFS(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFS(self)

    def windowSDFSE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFSE(self)

    def windowSDFE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFE(self)

    def windowSDFNE(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFNE(self)

    def windowSDFN(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFN(self)

    def windowSDFNW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFNW(self)

    def windowSDFW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFW(self)

    def windowSDFSW(self) -> "double":
        return _openstudioisomodel.UserModel_windowSDFSW(self)

    def setValid(self, val: 'bool') -> "void":
        return _openstudioisomodel.UserModel_setValid(self, val)

    def wallAreaS(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaS(self)

    def wallAreaSE(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaSE(self)

    def wallAreaE(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaE(self)

    def wallAreaNE(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaNE(self)

    def wallAreaN(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaN(self)

    def wallAreaNW(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaNW(self)

    def wallAreaW(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaW(self)

    def wallAreaSW(self) -> "double":
        return _openstudioisomodel.UserModel_wallAreaSW(self)

    def roofArea(self) -> "double":
        return _openstudioisomodel.UserModel_roofArea(self)

    def windowAreaS(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaS(self)

    def windowAreaSE(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaSE(self)

    def windowAreaE(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaE(self)

    def windowAreaNE(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaNE(self)

    def windowAreaN(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaN(self)

    def windowAreaNW(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaNW(self)

    def windowAreaW(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaW(self)

    def windowAreaSW(self) -> "double":
        return _openstudioisomodel.UserModel_windowAreaSW(self)

    def skylightArea(self) -> "double":
        return _openstudioisomodel.UserModel_skylightArea(self)

    def roofSolarAbsorption(self) -> "double":
        return _openstudioisomodel.UserModel_roofSolarAbsorption(self)

    def roofThermalEmissivity(self) -> "double":
        return _openstudioisomodel.UserModel_roofThermalEmissivity(self)

    def skylightUvalue(self) -> "double":
        return _openstudioisomodel.UserModel_skylightUvalue(self)

    def skylightSHGC(self) -> "double":
        return _openstudioisomodel.UserModel_skylightSHGC(self)

    def exteriorHeatCapacity(self) -> "double":
        return _openstudioisomodel.UserModel_exteriorHeatCapacity(self)

    def infiltration(self) -> "double":
        return _openstudioisomodel.UserModel_infiltration(self)

    def hvacWasteFactor(self) -> "double":
        return _openstudioisomodel.UserModel_hvacWasteFactor(self)

    def hvacHeatingLossFactor(self) -> "double":
        return _openstudioisomodel.UserModel_hvacHeatingLossFactor(self)

    def hvacCoolingLossFactor(self) -> "double":
        return _openstudioisomodel.UserModel_hvacCoolingLossFactor(self)

    def dhwDistributionEfficiency(self) -> "double":
        return _openstudioisomodel.UserModel_dhwDistributionEfficiency(self)

    def heatingPumpControl(self) -> "double":
        return _openstudioisomodel.UserModel_heatingPumpControl(self)

    def coolingPumpControl(self) -> "double":
        return _openstudioisomodel.UserModel_coolingPumpControl(self)

    def heatGainPerPerson(self) -> "double":
        return _openstudioisomodel.UserModel_heatGainPerPerson(self)

    def setWeatherFilePath(self, val: 'path') -> "void":
        return _openstudioisomodel.UserModel_setWeatherFilePath(self, val)

    def setCoolingSystemIPLVToCOPRatio(self, val: 'double') -> "void":
        return _openstudioisomodel.UserModel_setCoolingSystemIPLVToCOPRatio(self, val)

    def setExhaustAirRecirculation(self, val: 'double') -> "void":
        return _openstudioisomodel.UserModel_setExhaustAirRecirculation(self, val)

    def __init__(self):
        this = _openstudioisomodel.new_UserModel()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudioisomodel.delete_UserModel
    __del__ = lambda self: None
UserModel_swigregister = _openstudioisomodel.UserModel_swigregister
UserModel_swigregister(UserModel)

class ISOModelForwardTranslator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ISOModelForwardTranslator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ISOModelForwardTranslator, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _openstudioisomodel.new_ISOModelForwardTranslator()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudioisomodel.delete_ISOModelForwardTranslator
    __del__ = lambda self: None

    def translateModel(self, model: 'Model') -> "openstudio::isomodel::UserModel":
        return _openstudioisomodel.ISOModelForwardTranslator_translateModel(self, model)

    def warnings(self) -> "std::vector< openstudio::LogMessage,std::allocator< openstudio::LogMessage > >":
        return _openstudioisomodel.ISOModelForwardTranslator_warnings(self)

    def errors(self) -> "std::vector< openstudio::LogMessage,std::allocator< openstudio::LogMessage > >":
        return _openstudioisomodel.ISOModelForwardTranslator_errors(self)
ISOModelForwardTranslator_swigregister = _openstudioisomodel.ISOModelForwardTranslator_swigregister
ISOModelForwardTranslator_swigregister(ISOModelForwardTranslator)

# This file is compatible with both classic and new-style classes.


