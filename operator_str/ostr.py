import operator
from binascii import hexlify


OPERS = {operator.add: "+",
        operator.sub: "-",
        operator.mul: "*",
        operator.floordiv: "/",
        operator.mod: "%",
        operator.pow: "**",
        operator.and_: "&",
        operator.or_: "|",
        operator.xor: "^"}


class OperatorStr(str):
    """A string upon which one can perform bitwise operations. Useful for
    cryptography. Or maybe not.
    
    """
    def _get_bytes(self):
        """Converts the string representation to an integer form of the 
        underlying bytes.
        
        """
        hex_bytes = hexlify(self.encode('utf-8'))
        return int(hex_bytes, 16)

    def __add__(self, other):
        return _apply_operator(self, other, operator.add)

    def __radd__(self, other):
        return _rapply_operator(self, other, operator.add)

    def __sub__(self, other):
        return _apply_operator(self, other, operator.sub)

    def __rsub__(self, other):
        return _rapply_operator(self, other, operator.sub)

    def __mul__(self, other):
        return _apply_operator(self, other, operator.mul)

    def __rmul__(self, other):
        return _rapply_operator(self, other, operator.mul)

    def __floordiv__(self, other):
        return _apply_operator(self, other, operator.floordiv)

    def __rfloordiv__(self, other):
        return _rapply_operator(self, other, operator.floordiv)

    def __mod__(self, other):
        return _apply_operator(self, other, operator.mod)

    def __rmod__(self, other):
        return _rapply_operator(self, other, operator.mod)

    def __divmod__(self, other):
        return _apply_operator(self, other, operator.divmod)

    def __rdivmod__(self, other):
        return _rapply_operator(self, other, operator.divmod)

    def __pow__(self, other):
        return _apply_operator(self, other, operator.pow)

    def __rpow__(self, other):
        return _rapply_operator(self, other, operator.pow)

    def __lshift__(self, other):
        return _apply_operator(self, other, operator.lshift)

    def __rlshift__(self, other):
        return _rapply_operator(self, other, operator.lshift)

    def __rshift__(self, other):
        return _apply_operator(self, other, operator.rshift)

    def __rrshift__(self, other):
        return _rapply_operator(self, other, operator.rshift)

    def __and__(self, other):
        return _apply_operator(self, other, operator.and_)

    def __rand__(self, other):
        return _rapply_operator(self, other, operator.and_)

    def __or__(self, other):
        return _apply_operator(self, other, operator.or_)

    def __ror__(self, other):
        return _rapply_operator(self, other, operator.or_)

    def __xor__(self, other):
        return _apply_operator(self, other, operator.xor)

    def __rxor__(self, other):
        return _rapply_operator(self, other, operator.xor)

    def __iadd__(self, other):
        return _apply_operator(self, other, operator.add)

    def __isub__(self, other):
        return _apply_operator(self, other, operator.sub)

    def __imul__(self, other):
        return _apply_operator(self, other, operator.mul)

    def __ifloordiv__(self, other):
        return _apply_operator(self, other, operator.floordiv)

    def __imod__(self, other):
        return _apply_operator(self, other, operator.mod)

    def __ipow__(self, other):
        return _apply_operator(self, other, operator.pow)

    def __ilshift__(self, other):
        return _apply_operator(self, other, operator.lshift)

    def __irshift__(self, other):
        return _apply_operator(self, other, operator.rshift)

    def __iand__(self, other):
        return _apply_operator(self, other, operator.and_)

    def __ior__(self, other):
        return _apply_operator(self, other, operator.or_)

    def __ixor__(self, other):
        return _apply_operator(self, other, operator.xor)


def bytes_to_ostr(int_bytes):
    """Converts an integer representation of bytes to a unicode 
    OperatorStr.
    
    """
    # TODO: Fix this hideous function.
    if int_bytes < 0:
        raise OverflowError("Characters of byte-index < 0 are undefined!")

    size = 1
    while True:
        try:
            byte_array = int_bytes.to_bytes(size, byteorder='big')
        except OverflowError:
            size += 1
        else:
            break

    unicode_bytes = [chr(int(byte)) for byte in byte_array]
    return OperatorStr("".join(unicode_bytes))


def _get_ostr(value):
    """If the value is an int, convert it to an OperatorStr and returns it.
    Otherwise, just returns it.
    
    """
    # TODO: The existence of this function is probably a sign of poor design.
    if isinstance(value, int):
        return bytes_to_ostr(value)
    else:
        return value


def _apply_operator(operator_string, n, operator):
    """Converts the operator_string to bytes, performs the operator on the
    operator_string and the argument and returns the result converted to
    an OperatorStr.

    """
    if isinstance(n, float):
        raise TypeError("unsupported operand type(s) for {}: "
                        "'OperatorStr' and 'float'".format(OPERS[operator]))
    int_bytes = operator(operator_string._get_bytes(), n)
    return _get_ostr(int_bytes)


def _rapply_operator(operator_string, n, operator):
    """Like _apply_operator, only with the arguments reversed.

    """
    if isinstance(n, float):
        raise TypeError("unsupported operand type(s) for {}: "
                        "'float' and 'OperatorStr'".format(OPERS[operator]))
    int_bytes = operator(n, operator_string._get_bytes())
    return _get_ostr(int_bytes)
