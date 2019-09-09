import os
import yaml
import pytest
from functools import partial
from pkg_resources import resource_filename as rs_fn
from pkg_resources import parse_version

EXP_DIR = rs_fn("xpdconf", "examples/")


def test_yaml_load():
    # test version
    if parse_version(yaml.__version__) > parse_version('3.13'):
        loader = partial(yaml.full_load)
    else:
        loader = partial(yaml.load)
    # assert no warning
    with pytest.warns(None) as record:
        fn = os.path.join(EXP_DIR, 'sim.yaml')
        with open(fn) as f:
            loader(f)
    assert not record
