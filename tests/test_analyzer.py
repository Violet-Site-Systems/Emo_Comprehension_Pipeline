"""Tests for the emotional analyzer module."""

import pytest
from emo_comprehension.core.analyzer import EmotionalAnalyzer, EmotionalState


def test_emotional_state_creation() -> None:
    """Test creation of EmotionalState."""
    state = EmotionalState(
        emotion="joy",
        intensity=0.8,
        valence=0.7,
        arousal=0.6,
    )
    assert state.emotion == "joy"
    assert state.intensity == 0.8
    assert state.valence == 0.7
    assert state.arousal == 0.6


def test_emotional_state_validation() -> None:
    """Test EmotionalState validation."""
    with pytest.raises(Exception):
        EmotionalState(
            emotion="joy",
            intensity=1.5,  # Invalid: > 1.0
            valence=0.7,
            arousal=0.6,
        )


def test_analyzer_initialization() -> None:
    """Test EmotionalAnalyzer initialization."""
    analyzer = EmotionalAnalyzer()
    assert analyzer.model_name == "default"

    analyzer_custom = EmotionalAnalyzer(model_name="custom")
    assert analyzer_custom.model_name == "custom"


def test_analyze_text() -> None:
    """Test text analysis."""
    analyzer = EmotionalAnalyzer()
    states = analyzer.analyze_text("I am feeling happy today.")

    assert isinstance(states, list)
    assert len(states) > 0
    assert all(isinstance(s, EmotionalState) for s in states)


def test_analyze_context() -> None:
    """Test context-aware analysis."""
    analyzer = EmotionalAnalyzer()
    context = {"user_id": "123", "timestamp": "2025-12-31"}
    states = analyzer.analyze_context("I am feeling happy today.", context)

    assert isinstance(states, list)
    assert len(states) > 0
    assert states[0].context == context
