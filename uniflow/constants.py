
"""Flow constants."""

ROOT_NAME = "root"
OUTPUT_NAME = "output"

# Flow Types
EXTRACT = "extract"
TRANSFORM = "transform"
RATER = "rater"
EXPAND_REDUCE = "expand_reduce"

import sys
#sys.path.append('Cambio/uniflow')
from uniflow.flow.flow_factory import FlowFactory
from uniflow.constants import EXTRACT, RATER, TRANSFORM, EXPAND_REDUCE

FlowFactory.register(
    name="expand_reduce",
    flow_cls=EXPAND_REDUCE
)
# how to register...
print(FlowFactory.list(), "register?")