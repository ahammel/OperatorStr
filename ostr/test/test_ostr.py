from ostr import OperatorStr, bytes_to_ostr

class TestSmoke(object):
    """docstring for TestSmoke  """
    def test_smoke(self):
        assert OperatorStr("A") ^ OperatorStr("g") == OperatorStr("&")

        for char in "balkjasdfaval;adsfa":
            os = OperatorStr(char)
            assert os ^ 0x10 == 0x10 ^ os
            assert os ^ 0x10 ^ 0x10 == os
            assert os ^ os == 0

        for string in ["spam", "eggs", "banana", "foobar"]:
            os = OperatorStr(string)
            assert os ^ 0x10 ^ 0x10 == os
            assert os ^ os == 0

    def test_get_bytes(self):
        assert OperatorStr("A")._get_bytes() == 0x41
        assert OperatorStr("banana")._get_bytes() == 108170603228769

    def test_bytes_to_ostr(self):
        assert bytes_to_ostr(108170603228769) == OperatorStr("banana")
        assert bytes_to_ostr(0x41) == OperatorStr("A")

