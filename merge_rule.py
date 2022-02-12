from enum import Enum, auto


class MergeRule(Enum):
    SEQUENCE_MATHCER = auto()
    LEVENSHTEIN = auto()
    COSINE = auto()
