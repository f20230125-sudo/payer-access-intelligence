import pytest
from pai.normalize import identifier, ndc11


@pytest.mark.parametrize('value', ['１２３', '١٢٣', '²'])
def test_plan_identifiers_require_ascii_digits(value):
    with pytest.raises(ValueError):
        identifier(value, 5)


@pytest.mark.parametrize('value', ['１２３４５６７８９０１', '١٢٣٤٥-٦٧٨٩-٠١'])
def test_ndc_identifiers_require_ascii_digits(value):
    with pytest.raises(ValueError):
        ndc11(value)
