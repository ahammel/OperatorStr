This package provides the OperatorStr class, which are exactly the same things
as strings, except that one can apply arithmetic and logical operators to them.
This is done internally by converting the string to the integer version of its
unicode representation, performing the arithmetic and converting back.
OperatorStr arithmetic operations always return another OperatorStr.

::
    >>> from operator_str import OperatorStr
    >>> b = OperatorStr('banana')
    >>> b + 1
    'bananb'
    >>> b ^= OperatorStr('apples')
    >>> b
    '\x03\x11\x1e\r\x0b\x12'
    >>> b ^= OperatorStr('apples')
    >>> b
    'banana'

This may or may not be useful for cryptography. Here's a quick implementation
of the Vigenère cipher using OperatorStr::

    from operator_str import OperatorStr as OStr
    from itertools import cycle

    def vigenere(plaintext, key):
        key_zip = zip(plaintext, cycle(key))
        return "".join(OStr(p_char) ^ OStr(k_char) for p_char, k_char in key_zip)
