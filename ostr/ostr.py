from binascii import hexlify
import sys

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

    def __xor__(self, other):
        int_bytes = self._get_bytes() ^ other
        try:                                    # If the return value is an
            return bytes_to_ostr(int_bytes)     # int, convert it to an OStr.
        except AttributeError:                  # Else, just return it.
            return int_bytes

    def __rxor__(self, other):
        return self ^ other


def bytes_to_ostr(int_bytes):
    """Converts an integer representation of bytes to a unicode 
    OperatorStr.
    
    """
    size = 1
    while True:
        try:
            byte_array = int_bytes.to_bytes(size, byteorder='big')
        except OverflowError:
            size += 1
        else:
            break

    return OperatorStr(byte_array.decode('utf-8'))
