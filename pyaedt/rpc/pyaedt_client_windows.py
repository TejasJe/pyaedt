import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", ".."))
from pyaedt import is_ironpython

if is_ironpython:
    from pyaedt.third_party.ironpython.rpyc_27.utils.server import ThreadedServer
else:
    from rpyc.utils.server import ThreadedServer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from pyaedt.rpc.rpyc_services import PyaedtServiceWindows

if __name__ == "__main__":
    port = int(sys.argv[1])
    hostname = sys.argv[2]
    print("Starting Service on Port {} Hostname {}".format(port, hostname))
    safe_attrs = {
        "__abs__",
        "__add__",
        "__and__",
        "__bool__",
        "__code__",
        "__cmp__",
        "__contains__",
        "__delitem__",
        "__delslice__",
        "__div__",
        "__divmod__",
        "__doc__",
        "__eq__",
        "__float__",
        "__floordiv__",
        "__func__",
        "__ge__",
        "__getitem__",
        "__getslice__",
        "__gt__",
        "__hash__",
        "__hex__",
        "__iadd__",
        "__iand__",
        "__idiv__",
        "__ifloordiv__",
        "__ilshift__",
        "__imod__",
        "__imul__",
        "__index__",
        "__int__",
        "__invert__",
        "__ior__",
        "__ipow__",
        "__irshift__",
        "__isub__",
        "__iter__",
        "__itruediv__",
        "__ixor__",
        "__le__",
        "__len__",
        "__long__",
        "__lshift__",
        "__lt__",
        "__mod__",
        "__mul__",
        "__name__",
        "__ne__",
        "__neg__",
        "__new__",
        "__nonzero__",
        "__oct__",
        "__or__",
        "__pos__",
        "__pow__",
        "__radd__",
        "__rand__",
        "__rdiv__",
        "__rdivmod__",
        "__repr__",
        "__rfloordiv__",
        "__rlshift__",
        "__rmod__",
        "__rmul__",
        "__ror__",
        "__rpow__",
        "__rrshift__",
        "__rshift__",
        "__rsub__",
        "__rtruediv__",
        "__rxor__",
        "__setitem__",
        "__setslice__",
        "__str__",
        "__sub__",
        "__truediv__",
        "__xor__",
        "next",
        "__length_hint__",
        "__enter__",
        "__exit__",
        "__next__",
        "__format__",
    }
    t = ThreadedServer(
        PyaedtServiceWindows,
        hostname=hostname,
        port=port,
        protocol_config={
            "sync_request_timeout": None,
            "allow_public_attrs": True,
            "allow_setattr": True,
            "allow_all_attrs": True,
            "safe_attrs": safe_attrs,
            "allow_pickle": True,
            "allow_getattr": True,
            "import_custom_exceptions": True,
            "instantiate_custom_exceptions": True,
            "instantiate_oldstyle_exceptions": True,
            "allow_delattr": True,
        },
    )
    t.start()
