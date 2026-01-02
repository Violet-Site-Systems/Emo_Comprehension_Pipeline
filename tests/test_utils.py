"""Tests for utility functions."""

import json
import tempfile
from pathlib import Path

import pytest

from emo_comprehension.utils import (
    load_config,
    normalize_scores,
    validate_emotional_state,
)


def test_load_config() -> None:
    """Test configuration loading."""
    config_data = {"key": "value", "number": 42}

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(config_data, f)
        temp_path = f.name

    try:
        loaded = load_config(temp_path)
        assert loaded == config_data
    finally:
        Path(temp_path).unlink()


def test_normalize_scores() -> None:
    """Test score normalization."""
    scores = [1.0, 2.0, 3.0]
    normalized = normalize_scores(scores)

    assert len(normalized) == len(scores)
    assert abs(sum(normalized) - 1.0) < 1e-10
    assert all(0.0 <= s <= 1.0 for s in normalized)


def test_normalize_scores_zero_sum() -> None:
    """Test score normalization with zero sum."""
    scores = [0.0, 0.0, 0.0]
    normalized = normalize_scores(scores)

    assert len(normalized) == len(scores)
    assert abs(sum(normalized) - 1.0) < 1e-10
    assert all(abs(s - 1.0 / 3.0) < 1e-10 for s in normalized)


def test_validate_emotional_state_valid() -> None:
    """Test emotional state validation with valid state."""
    state = {
        "emotion": "joy",
        "intensity": 0.8,
        "valence": 0.7,
        "arousal": 0.6,
    }
    assert validate_emotional_state(state) is True


def test_validate_emotional_state_invalid() -> None:
    """Test emotional state validation with invalid state."""
    state = {
        "emotion": "joy",
        "intensity": 0.8,
        # Missing valence and arousal
    }
    assert validate_emotional_state(state) is False
