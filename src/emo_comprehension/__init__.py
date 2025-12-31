"""Emotional Comprehension Pipeline.

A neuro-symbolic framework for deep emotional comprehension and aligned
response generation in AI systems.
"""

__version__ = "0.1.0"
__author__ = "Violet Site Systems"
__license__ = "CC0-1.0"

from emo_comprehension.core.analyzer import EmotionalAnalyzer
from emo_comprehension.core.comprehension import EmotionalComprehension
from emo_comprehension.core.response import ResponseGenerator

__all__ = [
    "EmotionalAnalyzer",
    "EmotionalComprehension",
    "ResponseGenerator",
]
