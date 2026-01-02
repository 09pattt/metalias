def test_Transform_bytes():
    from src.utils.format import Transform
    v1, u1 = Transform("1500").bytes()
    v2, u2 = Transform("85000000").bytes()
    v3, u3 = Transform("189000").bytes()
    v4, u4 = Transform("12000000000000000000000000000").bytes()
    assert v1 == 1.5
    assert u1 == "KB"
    assert v2 == 85
    assert u2 == "MB"
    assert v3 == 189
    assert u3 == "KB"
    assert u4 == "PB"