from enum import Enum, auto


class MergeRule(Enum):
    LEVENSHTEIN = auto()
    COSINE = auto()
    
