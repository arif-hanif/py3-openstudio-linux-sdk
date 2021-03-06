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
            fp, pathname, description = imp.find_module('_openstudioenergyplus', [dirname(__file__)])
        except ImportError:
            import _openstudioenergyplus
            return _openstudioenergyplus
        if fp is not None:
            try:
                _mod = imp.load_module('_openstudioenergyplus', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _openstudioenergyplus = swig_import_helper()
    del swig_import_helper
else:
    import _openstudioenergyplus
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
    __swig_destroy__ = _openstudioenergyplus.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _openstudioenergyplus.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _openstudioenergyplus.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _openstudioenergyplus.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _openstudioenergyplus.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _openstudioenergyplus.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _openstudioenergyplus.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _openstudioenergyplus.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _openstudioenergyplus.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _openstudioenergyplus.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _openstudioenergyplus.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _openstudioenergyplus.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _openstudioenergyplus.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _openstudioenergyplus.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _openstudioenergyplus.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _openstudioenergyplus.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _openstudioenergyplus.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _openstudioenergyplus.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_openstudioenergyplus.SHARED_PTR_DISOWN_swigconstant(_openstudioenergyplus)
SHARED_PTR_DISOWN = _openstudioenergyplus.SHARED_PTR_DISOWN
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
class ErrorLevel(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ErrorLevel, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ErrorLevel, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _openstudioenergyplus.new_ErrorLevel(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def valueName(self) -> "std::string":
        return _openstudioenergyplus.ErrorLevel_valueName(self)

    def value(self) -> "int":
        return _openstudioenergyplus.ErrorLevel_value(self)

    def valueDescription(self) -> "std::string":
        return _openstudioenergyplus.ErrorLevel_valueDescription(self)

    def __eq__(self, other: 'ErrorLevel') -> "bool":
        return _openstudioenergyplus.ErrorLevel___eq__(self, other)

    def __ne__(self, other: 'ErrorLevel') -> "bool":
        return _openstudioenergyplus.ErrorLevel___ne__(self, other)

    def __gt__(self, other: 'ErrorLevel') -> "bool":
        return _openstudioenergyplus.ErrorLevel___gt__(self, other)

    def __ge__(self, other: 'ErrorLevel') -> "bool":
        return _openstudioenergyplus.ErrorLevel___ge__(self, other)

    def __lt__(self, other: 'ErrorLevel') -> "bool":
        return _openstudioenergyplus.ErrorLevel___lt__(self, other)

    def __le__(self, other: 'ErrorLevel') -> "bool":
        return _openstudioenergyplus.ErrorLevel___le__(self, other)
    __swig_getmethods__["enumName"] = lambda x: _openstudioenergyplus.ErrorLevel_enumName
    if _newclass:
        enumName = staticmethod(_openstudioenergyplus.ErrorLevel_enumName)
    __swig_getmethods__["getValues"] = lambda x: _openstudioenergyplus.ErrorLevel_getValues
    if _newclass:
        getValues = staticmethod(_openstudioenergyplus.ErrorLevel_getValues)
    __swig_destroy__ = _openstudioenergyplus.delete_ErrorLevel
    __del__ = lambda self: None
ErrorLevel_swigregister = _openstudioenergyplus.ErrorLevel_swigregister
ErrorLevel_swigregister(ErrorLevel)

def ErrorLevel_enumName() -> "std::string":
    return _openstudioenergyplus.ErrorLevel_enumName()
ErrorLevel_enumName = _openstudioenergyplus.ErrorLevel_enumName

def ErrorLevel_getValues() -> "std::set< int,std::less< int >,std::allocator< int > >":
    return _openstudioenergyplus.ErrorLevel_getValues()
ErrorLevel_getValues = _openstudioenergyplus.ErrorLevel_getValues

class ErrorFile(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ErrorFile, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ErrorFile, name)
    __repr__ = _swig_repr

    def __init__(self, errPath: 'path'):
        this = _openstudioenergyplus.new_ErrorFile(errPath)
        try:
            self.this.append(this)
        except:
            self.this = this

    def warnings(self) -> "std::vector< std::string,std::allocator< std::string > >":
        return _openstudioenergyplus.ErrorFile_warnings(self)

    def severeErrors(self) -> "std::vector< std::string,std::allocator< std::string > >":
        return _openstudioenergyplus.ErrorFile_severeErrors(self)

    def fatalErrors(self) -> "std::vector< std::string,std::allocator< std::string > >":
        return _openstudioenergyplus.ErrorFile_fatalErrors(self)

    def completed(self) -> "bool":
        return _openstudioenergyplus.ErrorFile_completed(self)

    def completedSuccessfully(self) -> "bool":
        return _openstudioenergyplus.ErrorFile_completedSuccessfully(self)
    __swig_destroy__ = _openstudioenergyplus.delete_ErrorFile
    __del__ = lambda self: None
ErrorFile_swigregister = _openstudioenergyplus.ErrorFile_swigregister
ErrorFile_swigregister(ErrorFile)


_openstudioenergyplus.ENERGYPLUS_VERSION_swigconstant(_openstudioenergyplus)
ENERGYPLUS_VERSION = _openstudioenergyplus.ENERGYPLUS_VERSION
class ForwardTranslator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ForwardTranslator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ForwardTranslator, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _openstudioenergyplus.new_ForwardTranslator()
        try:
            self.this.append(this)
        except:
            self.this = this

    def translateModel(self, model: 'Model', progressBar: 'ProgressBar'=None) -> "openstudio::Workspace":
        return _openstudioenergyplus.ForwardTranslator_translateModel(self, model, progressBar)

    def translateModelObject(self, modelObject: 'ModelObject') -> "openstudio::Workspace":
        return _openstudioenergyplus.ForwardTranslator_translateModelObject(self, modelObject)

    def warnings(self) -> "std::vector< openstudio::LogMessage,std::allocator< openstudio::LogMessage > >":
        return _openstudioenergyplus.ForwardTranslator_warnings(self)

    def errors(self) -> "std::vector< openstudio::LogMessage,std::allocator< openstudio::LogMessage > >":
        return _openstudioenergyplus.ForwardTranslator_errors(self)

    def setKeepRunControlSpecialDays(self, keepRunControlSpecialDays: 'bool') -> "void":
        return _openstudioenergyplus.ForwardTranslator_setKeepRunControlSpecialDays(self, keepRunControlSpecialDays)

    def setIPTabularOutput(self, isIP: 'bool') -> "void":
        return _openstudioenergyplus.ForwardTranslator_setIPTabularOutput(self, isIP)

    def setExcludeLCCObjects(self, excludeLCCObjects: 'bool') -> "void":
        return _openstudioenergyplus.ForwardTranslator_setExcludeLCCObjects(self, excludeLCCObjects)
    __swig_destroy__ = _openstudioenergyplus.delete_ForwardTranslator
    __del__ = lambda self: None
ForwardTranslator_swigregister = _openstudioenergyplus.ForwardTranslator_swigregister
ForwardTranslator_swigregister(ForwardTranslator)

class ReverseTranslator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ReverseTranslator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ReverseTranslator, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _openstudioenergyplus.new_ReverseTranslator()
        try:
            self.this.append(this)
        except:
            self.this = this

    def loadModel(self, path: 'path', progressBar: 'ProgressBar'=None) -> "boost::optional< openstudio::model::Model >":
        return _openstudioenergyplus.ReverseTranslator_loadModel(self, path, progressBar)

    def translateWorkspace(self, workspace: 'Workspace', progressBar: 'ProgressBar'=None, clearLogSink: 'bool'=True) -> "openstudio::model::Model":
        return _openstudioenergyplus.ReverseTranslator_translateWorkspace(self, workspace, progressBar, clearLogSink)

    def warnings(self) -> "std::vector< openstudio::LogMessage,std::allocator< openstudio::LogMessage > >":
        return _openstudioenergyplus.ReverseTranslator_warnings(self)

    def errors(self) -> "std::vector< openstudio::LogMessage,std::allocator< openstudio::LogMessage > >":
        return _openstudioenergyplus.ReverseTranslator_errors(self)

    def untranslatedIdfObjects(self) -> "std::vector< openstudio::IdfObject,std::allocator< openstudio::IdfObject > >":
        return _openstudioenergyplus.ReverseTranslator_untranslatedIdfObjects(self)
    __swig_destroy__ = _openstudioenergyplus.delete_ReverseTranslator
    __del__ = lambda self: None
ReverseTranslator_swigregister = _openstudioenergyplus.ReverseTranslator_swigregister
ReverseTranslator_swigregister(ReverseTranslator)


def loadAndTranslateIdf(path: 'path') -> "boost::optional< openstudio::model::Model >":
    return _openstudioenergyplus.loadAndTranslateIdf(path)
loadAndTranslateIdf = _openstudioenergyplus.loadAndTranslateIdf
# This file is compatible with both classic and new-style classes.


