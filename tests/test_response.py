"""Tests for the response generation module."""

import pytest

from emo_comprehension.core.analyzer import EmotionalState
from emo_comprehension.core.comprehension import (
    ComprehensionResult,
    EmotionalComprehension,
)
from emo_comprehension.core.response import GeneratedResponse, ResponseGenerator


def test_generator_initialization() -> None:
    """Test ResponseGenerator initialization."""
    gen = ResponseGenerator()
    assert gen.model_name == "default"

    gen_custom = ResponseGenerator(model_name="custom")
    assert gen_custom.model_name == "custom"


def test_generate_response() -> None:
    """Test response generation."""
    gen = ResponseGenerator()
    comp_result = ComprehensionResult(
        emotional_states=[],
        primary_emotion="joy",
        confidence=0.8,
        insights={},
    )

    response = gen.generate(comp_result)

    assert isinstance(response, GeneratedResponse)
    assert isinstance(response.text, str)
    assert 0.0 <= response.emotional_alignment <= 1.0
    assert response.tone == "empathetic"


def test_generate_with_custom_tone() -> None:
    """Test response generation with custom tone."""
    gen = ResponseGenerator()
    comp_result = ComprehensionResult(
        emotional_states=[],
        primary_emotion="sadness",
        confidence=0.7,
        insights={},
    )

    response = gen.generate(comp_result, tone="supportive")
    assert response.tone == "supportive"


def test_generate_with_prompt() -> None:
    """Test response generation with custom prompt."""
    gen = ResponseGenerator()
    comp_result = ComprehensionResult(
        emotional_states=[],
        primary_emotion="anger",
        confidence=0.6,
        insights={},
    )

    custom_prompt = "I hear your frustration."
    response = gen.generate(comp_result, prompt=custom_prompt)
    assert response.text == custom_prompt


def test_generate_batch() -> None:
    """Test batch response generation."""
    gen = ResponseGenerator()
    comp_results = [
        ComprehensionResult(
            emotional_states=[],
            primary_emotion="joy",
            confidence=0.8,
            insights={},
        ),
        ComprehensionResult(
            emotional_states=[],
            primary_emotion="sadness",
            confidence=0.6,
            insights={},
        ),
    ]

    responses = gen.generate_batch(comp_results)
    assert len(responses) == 2
    assert all(isinstance(r, GeneratedResponse) for r in responses)
