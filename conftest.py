import pytest
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

# @pytest.fixture()
# def clear_field():
#
