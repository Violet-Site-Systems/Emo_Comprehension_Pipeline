"""Utility functions for the emotional comprehension pipeline."""

import json
from typing import Any, Dict, List, cast


def load_config(config_path: str) -> Dict[str, Any]:
    """Load configuration from a JSON file. 

    Args:
        config_path: Path to the configuration file

    Returns:
        Configuration dictionary
    """
    with open(config_path, "r") as f:
        return cast(Dict[str, Any], json.load(f))

    "EmotionalComprehension",
    "ResponseGenerator",
]
