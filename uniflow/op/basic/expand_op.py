"""Expand operation."""
import copy
from typing import Any, Mapping, Sequence

from uniflow.node import Node
from uniflow.op.op import Op

class ExpandOp(Op):
    """Expand operation class."""

    def _transform(self, value_dict: Mapping[str, Any]) -> Mapping[str, Any]:
        """Transform value dict.

        Args:
            value_dict (Mapping[str, Any]): Input value dict.

        Returns:
            Mapping[str, Any]: Output value dict.
        """
        return copy.deepcopy(value_dict)

    def __call__(self, root: Node) -> Sequence[Node]:
        """Call expand operation.

        Args:
            nodes (Sequence[Node]): Input nodes.

        Returns:
            Sequence[Node]: Output nodes.
        """
        if not root.value_dict:
            return None
        dic_1 = {}
        dic_2 = {}
        root_keys = list(root.value_dict.keys())
        mid = len(root_keys)//2
        for i in range(len(root_keys)):
            pair_key = root_keys[i]
            pair_value = root.value_dict[pair_key]
            if i < mid:
                dic_1[pair_key] = pair_value
            else:
                dic_1[pair_key] = pair_value

        expand_1 = Node(name=self.unique_name(), value_dict=dic_1, prev_nodes=[root])
        expand_2 = Node(name=self.unique_name(), value_dict=dic_2, prev_nodes=[root])
        return expand_1, expand_2