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
            fp, pathname, description = imp.find_module('_openstudiomodeleditor', [dirname(__file__)])
        except ImportError:
            import _openstudiomodeleditor
            return _openstudiomodeleditor
        if fp is not None:
            try:
                _mod = imp.load_module('_openstudiomodeleditor', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _openstudiomodeleditor = swig_import_helper()
    del swig_import_helper
else:
    import _openstudiomodeleditor
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
    __swig_destroy__ = _openstudiomodeleditor.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _openstudiomodeleditor.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _openstudiomodeleditor.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _openstudiomodeleditor.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _openstudiomodeleditor.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _openstudiomodeleditor.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _openstudiomodeleditor.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _openstudiomodeleditor.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _openstudiomodeleditor.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _openstudiomodeleditor.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _openstudiomodeleditor.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _openstudiomodeleditor.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _openstudiomodeleditor.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _openstudiomodeleditor.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _openstudiomodeleditor.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _openstudiomodeleditor.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _openstudiomodeleditor.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _openstudiomodeleditor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


_openstudiomodeleditor.SHARED_PTR_DISOWN_swigconstant(_openstudiomodeleditor)
SHARED_PTR_DISOWN = _openstudiomodeleditor.SHARED_PTR_DISOWN
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
class IGWidget(openstudioutilitiescore.QWidget):
    __swig_setmethods__ = {}
    for _s in [openstudioutilitiescore.QWidget]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IGWidget, name, value)
    __swig_getmethods__ = {}
    for _s in [openstudioutilitiescore.QWidget]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IGWidget, name)
    __repr__ = _swig_repr

    def __init__(self, parent: 'QWidget'=None):
        this = _openstudiomodeleditor.new_IGWidget(parent)
        try:
            self.this.append(this)
        except:
            self.this = this

    def sizeHint(self) -> "QSize":
        return _openstudiomodeleditor.IGWidget_sizeHint(self)
    __swig_destroy__ = _openstudiomodeleditor.delete_IGWidget
    __del__ = lambda self: None
IGWidget_swigregister = _openstudiomodeleditor.IGWidget_swigregister
IGWidget_swigregister(IGWidget)

class IGComboBox(openstudioutilitiescore.QComboBox):
    __swig_setmethods__ = {}
    for _s in [openstudioutilitiescore.QComboBox]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, IGComboBox, name, value)
    __swig_getmethods__ = {}
    for _s in [openstudioutilitiescore.QComboBox]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, IGComboBox, name)
    __repr__ = _swig_repr

    def __init__(self, parent: 'QWidget'=None):
        this = _openstudiomodeleditor.new_IGComboBox(parent)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudiomodeleditor.delete_IGComboBox
    __del__ = lambda self: None
IGComboBox_swigregister = _openstudiomodeleditor.IGComboBox_swigregister
IGComboBox_swigregister(IGComboBox)

class InspectorGadget(openstudioutilitiescore.QWidget):
    __swig_setmethods__ = {}
    for _s in [openstudioutilitiescore.QWidget]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InspectorGadget, name, value)
    __swig_getmethods__ = {}
    for _s in [openstudioutilitiescore.QWidget]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InspectorGadget, name)
    __repr__ = _swig_repr
    FIXED = _openstudiomodeleditor.InspectorGadget_FIXED
    SCIENTIFIC = _openstudiomodeleditor.InspectorGadget_SCIENTIFIC
    UNFORMATED = _openstudiomodeleditor.InspectorGadget_UNFORMATED
    SI = _openstudiomodeleditor.InspectorGadget_SI
    IP = _openstudiomodeleditor.InspectorGadget_IP

    def __init__(self, parent: 'QWidget'=None, indent: 'int'=0, bridge: 'ComboHighlightBridge *'=None):
        this = _openstudiomodeleditor.new_InspectorGadget(parent, indent, bridge)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudiomodeleditor.delete_InspectorGadget
    __del__ = lambda self: None

    def layoutModelObj(self, workObj: 'WorkspaceObject', force: 'bool'=False, recursive: 'bool'=True, locked: 'bool'=False, hideChildren: 'bool'=False) -> "void":
        return _openstudiomodeleditor.InspectorGadget_layoutModelObj(self, workObj, force, recursive, locked, hideChildren)

    def setPrecision(self, prec: 'unsigned int', dispType: 'InspectorGadget::FLOAT_DISPLAY') -> "void":
        return _openstudiomodeleditor.InspectorGadget_setPrecision(self, prec, dispType)

    def setUnitSystem(self, unitSystem: 'InspectorGadget::UNIT_SYSTEM const') -> "void":
        return _openstudiomodeleditor.InspectorGadget_setUnitSystem(self, unitSystem)

    def removeWorkspaceObject(self, arg2: 'UUID') -> "void":
        return _openstudiomodeleditor.InspectorGadget_removeWorkspaceObject(self, arg2)

    def toggleUnits(self, displayIP: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_toggleUnits(self, displayIP)

    def rebuild(self, recursive: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_rebuild(self, recursive)

    def clear(self, recursive: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_clear(self, recursive)

    def IGdefaultRemoved(self, arg2: 'QString') -> "void":
        return _openstudiomodeleditor.InspectorGadget_IGdefaultRemoved(self, arg2)

    def IGvalueChanged(self, arg2: 'QString') -> "void":
        return _openstudiomodeleditor.InspectorGadget_IGvalueChanged(self, arg2)

    def IGcommentChanged(self, arg2: 'QString') -> "void":
        return _openstudiomodeleditor.InspectorGadget_IGcommentChanged(self, arg2)

    def IGautosize(self, toggled: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_IGautosize(self, toggled)

    def commentConfig(self, showComments: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_commentConfig(self, showComments)

    def setPrec(self) -> "void":
        return _openstudiomodeleditor.InspectorGadget_setPrec(self)

    def addExtensible(self) -> "void":
        return _openstudiomodeleditor.InspectorGadget_addExtensible(self)

    def removeExtensible(self) -> "void":
        return _openstudiomodeleditor.InspectorGadget_removeExtensible(self)

    def createAllFields(self) -> "void":
        return _openstudiomodeleditor.InspectorGadget_createAllFields(self)

    def showAllFields(self, state: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_showAllFields(self, state)

    def setRecursive(self, recursive: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorGadget_setRecursive(self, recursive)
InspectorGadget_swigregister = _openstudiomodeleditor.InspectorGadget_swigregister
InspectorGadget_swigregister(InspectorGadget)

class InspectorDialogClient(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InspectorDialogClient, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InspectorDialogClient, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _openstudiomodeleditor.new_InspectorDialogClient(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def valueName(self) -> "std::string":
        return _openstudiomodeleditor.InspectorDialogClient_valueName(self)

    def value(self) -> "int":
        return _openstudiomodeleditor.InspectorDialogClient_value(self)

    def valueDescription(self) -> "std::string":
        return _openstudiomodeleditor.InspectorDialogClient_valueDescription(self)

    def __eq__(self, other: 'InspectorDialogClient') -> "bool":
        return _openstudiomodeleditor.InspectorDialogClient___eq__(self, other)

    def __ne__(self, other: 'InspectorDialogClient') -> "bool":
        return _openstudiomodeleditor.InspectorDialogClient___ne__(self, other)

    def __gt__(self, other: 'InspectorDialogClient') -> "bool":
        return _openstudiomodeleditor.InspectorDialogClient___gt__(self, other)

    def __ge__(self, other: 'InspectorDialogClient') -> "bool":
        return _openstudiomodeleditor.InspectorDialogClient___ge__(self, other)

    def __lt__(self, other: 'InspectorDialogClient') -> "bool":
        return _openstudiomodeleditor.InspectorDialogClient___lt__(self, other)

    def __le__(self, other: 'InspectorDialogClient') -> "bool":
        return _openstudiomodeleditor.InspectorDialogClient___le__(self, other)
    __swig_getmethods__["enumName"] = lambda x: _openstudiomodeleditor.InspectorDialogClient_enumName
    if _newclass:
        enumName = staticmethod(_openstudiomodeleditor.InspectorDialogClient_enumName)
    __swig_getmethods__["getValues"] = lambda x: _openstudiomodeleditor.InspectorDialogClient_getValues
    if _newclass:
        getValues = staticmethod(_openstudiomodeleditor.InspectorDialogClient_getValues)
    __swig_destroy__ = _openstudiomodeleditor.delete_InspectorDialogClient
    __del__ = lambda self: None
InspectorDialogClient_swigregister = _openstudiomodeleditor.InspectorDialogClient_swigregister
InspectorDialogClient_swigregister(InspectorDialogClient)

def InspectorDialogClient_enumName() -> "std::string":
    return _openstudiomodeleditor.InspectorDialogClient_enumName()
InspectorDialogClient_enumName = _openstudiomodeleditor.InspectorDialogClient_enumName

def InspectorDialogClient_getValues() -> "std::set< int,std::less< int >,std::allocator< int > >":
    return _openstudiomodeleditor.InspectorDialogClient_getValues()
InspectorDialogClient_getValues = _openstudiomodeleditor.InspectorDialogClient_getValues

class InspectorDialog(openstudioutilitiescore.QMainWindow):
    __swig_setmethods__ = {}
    for _s in [openstudioutilitiescore.QMainWindow]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, InspectorDialog, name, value)
    __swig_getmethods__ = {}
    for _s in [openstudioutilitiescore.QMainWindow]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, InspectorDialog, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        if self.__class__ == InspectorDialog:
            _self = None
        else:
            _self = self
        this = _openstudiomodeleditor.new_InspectorDialog(_self, *args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudiomodeleditor.delete_InspectorDialog
    __del__ = lambda self: None

    def iddObjectType(self) -> "openstudio::IddObjectType":
        return _openstudiomodeleditor.InspectorDialog_iddObjectType(self)

    def setIddObjectType(self, arg2: 'IddObjectType', force: 'bool'=False) -> "bool":
        return _openstudiomodeleditor.InspectorDialog_setIddObjectType(self, arg2, force)

    def selectedObjectHandles(self) -> "std::vector< openstudio::Handle,std::allocator< openstudio::Handle > >":
        return _openstudiomodeleditor.InspectorDialog_selectedObjectHandles(self)

    def setSelectedObjectHandles(self, arg2: 'UUIDVector', force: 'bool'=False) -> "bool":
        return _openstudiomodeleditor.InspectorDialog_setSelectedObjectHandles(self, arg2, force)

    def model(self) -> "openstudio::model::Model":
        return _openstudiomodeleditor.InspectorDialog_model(self)

    def setModel(self, model: 'Model', force: 'bool'=False) -> "void":
        return _openstudiomodeleditor.InspectorDialog_setModel(self, model, force)

    def rebuildInspectorGadget(self, recursive: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorDialog_rebuildInspectorGadget(self, recursive)

    def saveState(self) -> "void":
        return _openstudiomodeleditor.InspectorDialog_saveState(self)

    def restoreState(self) -> "void":
        return _openstudiomodeleditor.InspectorDialog_restoreState(self)

    def displayIP(self, displayIP: 'bool const') -> "void":
        return _openstudiomodeleditor.InspectorDialog_displayIP(self, displayIP)

    def onIddObjectTypeChanged(self, arg0: 'IddObjectType') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onIddObjectTypeChanged(self, arg0)

    def onSelectedObjectHandlesChanged(self, arg0: 'UUIDVector') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onSelectedObjectHandlesChanged(self, arg0)

    def onModelChanged(self, arg0: 'Model') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onModelChanged(self, arg0)

    def onPushButtonNew(self, arg0: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onPushButtonNew(self, arg0)

    def onPushButtonCopy(self, arg0: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onPushButtonCopy(self, arg0)

    def onPushButtonDelete(self, arg0: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onPushButtonDelete(self, arg0)

    def onPushButtonPurge(self, arg0: 'bool') -> "void":
        return _openstudiomodeleditor.InspectorDialog_onPushButtonPurge(self, arg0)

    def showEvent(self, t_event: 'QShowEvent *') -> "void":
        return _openstudiomodeleditor.InspectorDialog_showEvent(self, t_event)

    def closeEvent(self, t_event: 'QCloseEvent *') -> "void":
        return _openstudiomodeleditor.InspectorDialog_closeEvent(self, t_event)
    def __disown__(self):
        self.this.disown()
        _openstudiomodeleditor.disown_InspectorDialog(self)
        return weakref_proxy(self)
InspectorDialog_swigregister = _openstudiomodeleditor.InspectorDialog_swigregister
InspectorDialog_swigregister(InspectorDialog)

class ModelObjectSelectorDialog(openstudioutilitiescore.QDialog):
    __swig_setmethods__ = {}
    for _s in [openstudioutilitiescore.QDialog]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ModelObjectSelectorDialog, name, value)
    __swig_getmethods__ = {}
    for _s in [openstudioutilitiescore.QDialog]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ModelObjectSelectorDialog, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _openstudiomodeleditor.new_ModelObjectSelectorDialog(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _openstudiomodeleditor.delete_ModelObjectSelectorDialog
    __del__ = lambda self: None

    def selectedModelObject(self) -> "boost::optional< openstudio::model::ModelObject >":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_selectedModelObject(self)

    def setWindowTitle(self, text: 'std::string const &') -> "void":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_setWindowTitle(self, text)

    def setUserText(self, text: 'std::string const &') -> "void":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_setUserText(self, text)

    def setOKButtonText(self, text: 'std::string const &') -> "void":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_setOKButtonText(self, text)

    def setCancelButtonText(self, text: 'std::string const &') -> "void":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_setCancelButtonText(self, text)

    def onPushButtonOK(self, arg2: 'bool') -> "void":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_onPushButtonOK(self, arg2)

    def onPushButtonCancel(self, arg2: 'bool') -> "void":
        return _openstudiomodeleditor.ModelObjectSelectorDialog_onPushButtonCancel(self, arg2)
ModelObjectSelectorDialog_swigregister = _openstudiomodeleditor.ModelObjectSelectorDialog_swigregister
ModelObjectSelectorDialog_swigregister(ModelObjectSelectorDialog)

class ModelObjectSelectorDialogWatcher(openstudioutilitiescore.QObject):
    __swig_setmethods__ = {}
    for _s in [openstudioutilitiescore.QObject]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ModelObjectSelectorDialogWatcher, name, value)
    __swig_getmethods__ = {}
    for _s in [openstudioutilitiescore.QObject]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ModelObjectSelectorDialogWatcher, name)
    __repr__ = _swig_repr

    def __init__(self, modelObjectSelectorDialog: 'std::shared_ptr< ModelObjectSelectorDialog >'):
        this = _openstudiomodeleditor.new_ModelObjectSelectorDialogWatcher(modelObjectSelectorDialog)
        try:
            self.this.append(this)
        except:
            self.this = this

    def selectedModelObject(self) -> "boost::optional< openstudio::model::ModelObject >":
        return _openstudiomodeleditor.ModelObjectSelectorDialogWatcher_selectedModelObject(self)

    def isSelectionFinal(self) -> "bool":
        return _openstudiomodeleditor.ModelObjectSelectorDialogWatcher_isSelectionFinal(self)
    __swig_destroy__ = _openstudiomodeleditor.delete_ModelObjectSelectorDialogWatcher
    __del__ = lambda self: None
ModelObjectSelectorDialogWatcher_swigregister = _openstudiomodeleditor.ModelObjectSelectorDialogWatcher_swigregister
ModelObjectSelectorDialogWatcher_swigregister(ModelObjectSelectorDialogWatcher)


def ensureThermalZone(space: 'openstudio::model::Space &') -> "void":
    return _openstudiomodeleditor.ensureThermalZone(space)
ensureThermalZone = _openstudiomodeleditor.ensureThermalZone

def ensureSpaceLoadDefinition(instance: 'openstudio::model::SpaceLoadInstance &') -> "void":
    return _openstudiomodeleditor.ensureSpaceLoadDefinition(instance)
ensureSpaceLoadDefinition = _openstudiomodeleditor.ensureSpaceLoadDefinition
# This file is compatible with both classic and new-style classes.


