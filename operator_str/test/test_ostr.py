import operator
from operator_str import OperatorStr, bytes_to_ostr
import pytest

class TestSmoke(object):
    """docstring for TestSmoke  """
    def test_xor(self):
        assert OperatorStr("A") ^ OperatorStr("g") == OperatorStr("&")

        for char in "balkjasdfaval;adsfa":
            os = OperatorStr(char)
            assert os ^ 0x10 == 0x10 ^ os
            assert os ^ 0x10 ^ 0x10 == os
            assert os ^ os == '\x00'

        for string in ["spam", "eggs", "banana", "foobar"]:
            os = OperatorStr(string)
            assert os ^ 0x10 ^ 0x10 == os
            assert os ^ os == '\x00'

    def test_add(self):
        assert OperatorStr("banana") + 1 == "bananb"
        assert 1 + OperatorStr("banana") == "bananb"

    def test_get_bytes(self):
        assert OperatorStr("A")._get_bytes() == 0x41
        assert OperatorStr("banana")._get_bytes() == 108170603228769

    def test_bytes_to_ostr(self):
        assert bytes_to_ostr(108170603228769) == OperatorStr("banana")
        assert bytes_to_ostr(0x41) == OperatorStr("A")

    def test_float(self):
        b = OperatorStr("banana")

        with pytest.raises(TypeError):
            b + 1.5
        with pytest.raises(TypeError):
            1.5 + b

    def test_negative_bytes(self):
        """bytes_to_ostr should fail when given negative bytes."""
        with pytest.raises(OverflowError):
            bytes_to_ostr(-1)

        with pytest.raises(OverflowError):
            OperatorStr('a') - OperatorStr('b')
