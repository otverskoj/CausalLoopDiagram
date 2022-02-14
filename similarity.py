from difflib import SequenceMatcher
from merge_rule import MergeRule
from jellyfish import levenshtein_distance


def _is_similar_by_sequence_matcher(first_node: str, second_node: str) -> bool:
    return SequenceMatcher(a=first_node, b=second_node).ratio() >= 0.75


def _is_similar_by_levenshtein(first_node: str, second_node: str) -> bool:
    return levenshtein_distance(first_node, second_node) <= 5


def _is_similar_by_cosine(first_node: str, second_node: str) -> bool:
    return False


handlers: dict = {
    MergeRule.SEQUENCE_MATHCER: _is_similar_by_sequence_matcher,
    MergeRule.LEVENSHTEIN: _is_similar_by_levenshtein,
    MergeRule.COSINE: _is_similar_by_cosine
}


def is_similar(first_node: str, second_node: str, rule: MergeRule) -> bool:
    if rule in handlers:
        handler = handlers[rule]
        return handler(first_node, second_node)
    else:
        print('There is no such rule')
        return False
