"""Shared fixtures and configuration for pytest."""

import pytest


@pytest.fixture
def sample_emotional_state():
    """Provide a sample emotional state for testing."""
    from emo_comprehension.core.analyzer import EmotionalState
    
    return EmotionalState(
        emotion="joy",
        intensity=0.8,
        valence=0.7,
        arousal=0.6,
    )


@pytest.fixture
def sample_comprehension_result():
    """Provide a sample comprehension result for testing."""
    from emo_comprehension.core.comprehension import ComprehensionResult
    
    return ComprehensionResult(
        emotional_states=[],
        primary_emotion="joy",
        confidence=0.8,
        insights={},
    )
