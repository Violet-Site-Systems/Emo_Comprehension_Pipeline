"""Tests for the emotional comprehension module."""

import pytest
from emo_comprehension.core.analyzer import EmotionalState
from emo_comprehension.core.comprehension import (
    EmotionalComprehension,
    ComprehensionResult,
)


def test_comprehension_initialization() -> None:
    """Test EmotionalComprehension initialization."""
    comp = EmotionalComprehension()
    assert comp.config == {}
    
    comp_custom = EmotionalComprehension(config={"key": "value"})
    assert comp_custom.config == {"key": "value"}


def test_comprehend_empty_states() -> None:
    """Test comprehension with empty emotional states."""
    comp = EmotionalComprehension()
    result = comp.comprehend([])
    
    assert isinstance(result, ComprehensionResult)
    assert result.emotional_states == []
    assert result.primary_emotion == "neutral"
    assert result.confidence == 0.0


def test_comprehend_single_state() -> None:
    """Test comprehension with single emotional state."""
    comp = EmotionalComprehension()
    state = EmotionalState(
        emotion="joy",
        intensity=0.8,
        valence=0.7,
        arousal=0.6,
    )
    result = comp.comprehend([state])
    
    assert isinstance(result, ComprehensionResult)
    assert len(result.emotional_states) == 1
    assert result.primary_emotion == "joy"
    assert result.confidence == 0.8


def test_comprehend_with_context() -> None:
    """Test comprehension with context."""
    comp = EmotionalComprehension()
    state = EmotionalState(
        emotion="sadness",
        intensity=0.6,
        valence=-0.5,
        arousal=0.4,
    )
    context = {"situation": "loss"}
    result = comp.comprehend([state], context=context)
    
    assert result.insights.get("context") == context
