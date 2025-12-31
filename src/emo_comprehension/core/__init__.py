"""Core module for emotional comprehension pipeline."""

from emo_comprehension.core.analyzer import EmotionalAnalyzer
from emo_comprehension.core.comprehension import EmotionalComprehension
from emo_comprehension.core.response import ResponseGenerator

__all__ = [
    "EmotionalAnalyzer",
    "EmotionalComprehension",
    "ResponseGenerator",
]
