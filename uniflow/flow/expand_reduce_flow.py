"""Expand Reduce Flow"""
from uniflow.op.basic.expand_op import ExpandOp
from uniflow.op.basic.reduce_op import ReduceOp
from uniflow.flow.flow import Flow

from typing import Any, Dict, Sequence

from uniflow.constants import EXTRACT
from uniflow.flow.flow import Flow
from uniflow.node import Node
from uniflow.op.extract.load.image_op import ExtractImageOp, ProcessImageOp
from uniflow.op.extract.split.constants import PARAGRAPH_SPLITTER
from uniflow.op.extract.split.splitter_factory import SplitterOpsFactory
from uniflow.op.model.llm_preprocessor import LLMDataPreprocessor


class ExtractImageFlow(Flow):
    """Extract Image Flow Class."""

    TAG = EXPAND_REDUCE

    def __init__(
        self,
        model_config: Dict[str, Any],
        splitter: str = PARAGRAPH_SPLITTER,
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
        output = []
        for node in nodes:
            e1, e2 = self._expand_op(node)
            r1 = self._reduce_op(e1, e2)
            output.append(r1)

        return output

