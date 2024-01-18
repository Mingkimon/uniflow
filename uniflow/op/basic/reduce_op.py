"""Reduce operation."""
import copy
from typing import Any, Mapping, Sequence

from uniflow.node import Node
from uniflow.op.op import Op


class ReduceOp(Op):
    """Reduce operation class."""

    def _transform(self, value_dict: Mapping[str, Any]) -> Mapping[str, Any]:
        """Transform value dict.

        Args:
            value_dict (Mapping[str, Any]): Input value dict.

        Returns:
            Mapping[str, Any]: Output value dict.
        """
        return copy.deepcopy(value_dict)

    def __call__(self, nodes: Sequence[Node]) -> Node:
        """Call linear operation.

        Args:
            nodes (Sequence[Node]): Input nodes.

        Returns:
            Sequence[Node]: Output nodes.
        """
        reduce_1_dic = {}
        for i in range(len(nodes)):
            print(nodes[i].name)
            print(nodes[i].value_dict)
        print("finished round")
        # should take 2 dict as input....why
        expand_1, expand_2 = nodes
        e1_value_dict = self._transform(expand_1.value_dict)
        e2_value_dict = self._transform(expand_2.value_dict)
        key_lst_1 = list(e1_value_dict.keys())
        key_lst_2 = list(e2_value_dict.keys())

        assert len(key_lst_1) == len(key_lst_2), f"Lengths not match, {len(key_lst_1)} and {len(key_lst_2)}"

        for i in range(len(key_lst_1)):
            joint_key = key_lst_1[i] + " " + key_lst_2[i]
            joint_value = expand_1.value_dict[key_lst_1[i]] + " " + expand_2.value_dict[key_lst_2[i]]
            reduce_1_dic[joint_key] = joint_value
            
        reduce_1 = Node(name=self.unique_name(), value_dict=reduce_1_dic, prev_nodes=[expand_1, expand_2])
        print("finish return")

        return reduce_1
