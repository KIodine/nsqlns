from typing import (
    Union, Callable
)
from functools import (
    wraps
)

__all__ = [
    "NsqlNamespace",
]

DEFAULT_DELIM = ":"
REPR_TMP = "<namespace=\"{}\", delim=\"{}\">"

# --- Usage ---
# root = NsqlNamespace("root", delim=":")
# leaf = root/"leaf"
# str(leaf) -> "root:leaf"
# -------------
def typecheck(method: Callable):
        @wraps(method)
        def wrapper(inst: object, subj: object):
            if not isinstance(subj, (str, NsqlNamespace)):
                raise TypeError(f"Cannot concat with object type: {type(subj)}")
            return method(inst, subj)
        return wrapper

class NsqlNamespace():
    def __init__(
            self, node_s: str, delim: str=DEFAULT_DELIM
        ):
        self.node_s = node_s
        self.delim  = delim
        return
    
    def __str__(self) -> str:
        return self.node_s

    def __repr__(self) -> str:
        return REPR_TMP.format(self.node_s, self.delim)

    @typecheck
    def __gt__(self, subj: object) -> str:
        s = subj if isinstance(subj, str) else subj.node_s
        return self.delim.join((self.node_s, s))

    # Override the "/" operator.
    @typecheck
    def __truediv__(self, dividend: object):
        if isinstance(dividend, NsqlNamespace):
            s = dividend.node_s
            sub_delim = dividend.delim
        else:
            s = dividend
            sub_delim  = self.delim
        return NsqlNamespace(
                self.delim.join((self.node_s, s)),
                delim=sub_delim
            )

