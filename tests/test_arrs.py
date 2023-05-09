from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1], 0, "test") == 1
    assert arrs.get([1, 2, 3], -1, "test") == "test"
    assert arrs.get([1, 2, 3], -4) is None


def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], end=-1) == [1, 2]
    assert arrs.my_slice([1, 2, 3], start=-2, end=-1) == [2]
    assert arrs.my_slice([1, 2, 3], -5) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -3, -5) == []
    assert arrs.my_slice([1, 2, 3], -4, -5) == []
    assert arrs.my_slice([1, 2, 3], 2, 1) == []
    assert arrs.my_slice([1, 2, 3], end=5) == [1, 2, 3]
    assert arrs.my_slice([], 0, 1) == []
    assert arrs.my_slice([], -1) == []
    assert arrs.my_slice([1, 2, 3], 0, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], end=-1) == [1, 2]
    assert arrs.my_slice([1, 2, 3], -2, -1) == [2]
    assert arrs.my_slice([1, 2, 3], -4, None) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], -2, 2) == [2]
    assert arrs.my_slice([1, 2, 3], -3, 1) == [1]
    assert arrs.my_slice([1, 2, 3], end=0) == []
    assert arrs.my_slice([1, 2, 3], 1, 2) == [2]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], start=0) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], 1, 1) == []
    assert arrs.my_slice([1, 2, 3], -5, -4) == []
    assert arrs.my_slice([1, 2, 3], 5, 6) == []
