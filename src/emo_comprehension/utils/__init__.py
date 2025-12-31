"""Utility functions for the emotional comprehension pipeline."""

from typing import Dict, Any, List
import json


def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Configuration dictionary
    """
    with open(config_path, "r") as f:
        return json.load(f)


def normalize_scores(scores: List[float]) -> List[float]:
    """Normalize a list of scores to sum to 1.0.
    
    Args:
        scores: List of scores to normalize
        
    Returns:
        Normalized scores
    """
    total = sum(scores)
    if total == 0:
        return [1.0 / len(scores)] * len(scores)
    return [s / total for s in scores]


def validate_emotional_state(state: Dict[str, Any]) -> bool:
    """Validate an emotional state dictionary.
    
    Args:
        state: Emotional state dictionary
        
    Returns:
        True if valid, False otherwise
    """
    required_keys = ["emotion", "intensity", "valence", "arousal"]
    return all(key in state for key in required_keys)
