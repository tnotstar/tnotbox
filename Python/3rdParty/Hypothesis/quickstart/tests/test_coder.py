# -*- coding: utf-8 -*-

from hypothesis import example, given, strategies as st

from quickstart.coder import encode, decode


@given(s=st.text())
@example(s="")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s


# EOF
