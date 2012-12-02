from ostr import OperatorStr

class TestSmoke(object):
    """docstring for TestSmoke  """
    def test_smoke(self):
        assert OperatorStr("A") ^ OperatorStr("g") == OperatorStr("&")

        for char in "balkjasdfaval;adsfa":
            os = OperatorStr(char)
            assert os ^ 0x10 ^ 0x10 == os
            assert os ^ os == 0

        for string in ["spam", "eggs", "banana", "foobar"]:
            os = OperatorStr(string)
            assert os ^ 0x10 ^ 0x10 == os
            assert os ^ os == 0

