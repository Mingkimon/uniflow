"""Expand Reduce Flow"""
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.flow.flow import Flow

from typing import Any, Dict, Sequence

from uniflow.constants import EXPAND_REDUCE
from uniflow.flow.flow import Flow
from uniflow.node import Node
from uniflow.op.extract.load.image_op import ExtractImageOp, ProcessImageOp
from uniflow.op.extract.split.constants import PARAGRAPH_SPLITTER
from uniflow.op.extract.split.splitter_factory import SplitterOpsFactory
from uniflow.op.model.llm_preprocessor import LLMDataPreprocessor


class ExpandReduceFlow(Flow):
    """Extract Image Flow Class."""

    TAG = EXPAND_REDUCE

    def __init__(
        self
    ) -> None:
        """Extract Image Flow Constructor.

        Args:
            model_config (Dict[str, Any]): Model config.
            splitter (str): Splitter to use. Defaults to "".
        """
        super().__init__()
        self._expand_op = ExpandOp(name="expand_op")
        self._reduce_op = ReduceOp(name='reduce_op')

    def run(self, nodes: Sequence[Node]) -> Sequence[Node]:
        """Run Model Flow.

        Args:
            nodes (Sequence[Node]): Nodes to run.

        Returns:
            Sequence[Node]: Nodes after running.
        """
        nodes = nodes[0]
        nodes = self._expand_op(nodes)
        nodes = self._reduce_op(nodes)

        return nodes

