#!/usr/bin/env python3
"""
Pipeline Validation Test Suite

This module provides validation tests for the Emotional Comprehension Pipeline.
It tests the integration and functionality of all pipeline components.

Usage:
    python pipeline-validation.py

Requirements:
    - Python 3.8+
    - pytest (for running tests)
    - Additional dependencies as pipeline develops
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any


class PipelineValidator:
    """Validates the Emotional Comprehension Pipeline components and integration."""
    
    def __init__(self):
        """Initialize the pipeline validator."""
        self.project_root = Path(__file__).parent.parent
        self.examples_dir = self.project_root / "examples"
        self.src_dir = self.project_root / "src"
        self.docs_dir = self.project_root / "docs"
        
    def validate_structure(self) -> Dict[str, bool]:
        """
        Validate that the repository structure matches requirements.
        
        Returns:
            Dictionary mapping structure elements to validation status
        """
        results = {}
        
        # Check documentation files
        doc_files = [
            "pipeline-spec.md",
            "physix-overview.md",
            "dac-roadmap.md",
            "scaling-basi.md",
            "identity-continuity.md",
            "ethical-oversight.md"
        ]
        
        for doc_file in doc_files:
            file_path = self.docs_dir / doc_file
            results[f"docs/{doc_file}"] = file_path.exists()
            
        # Check source directories
        src_dirs = ["y0x1", "ionation", "metta", "tqnn", "hyperon"]
        
        for src_dir in src_dirs:
            dir_path = self.src_dir / src_dir
            results[f"src/{src_dir}/"] = dir_path.exists()
            results[f"src/{src_dir}/README.md"] = (dir_path / "README.md").exists()
            
        # Check example files
        example_files = [
            "input-output-samples.json",
            "emotional-cases-dataset.json"
        ]
        
        for example_file in example_files:
            file_path = self.examples_dir / example_file
            results[f"examples/{example_file}"] = file_path.exists()
            
        return results
    
    def validate_json_files(self) -> Dict[str, Any]:
        """
        Validate JSON files for correct syntax and structure.
        
        Returns:
            Dictionary with validation results for each JSON file
        """
        results = {}
        
        json_files = [
            self.examples_dir / "input-output-samples.json",
            self.examples_dir / "emotional-cases-dataset.json"
        ]
        
        for json_file in json_files:
            try:
                if json_file.exists():
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    results[json_file.name] = {
                        "valid": True,
                        "data": data,
                        "error": None
                    }
                else:
                    results[json_file.name] = {
                        "valid": False,
                        "data": None,
                        "error": "File not found"
                    }
            except json.JSONDecodeError as e:
                results[json_file.name] = {
                    "valid": False,
                    "data": None,
                    "error": f"JSON decode error: {e}"
                }
            except Exception as e:
                results[json_file.name] = {
                    "valid": False,
                    "data": None,
                    "error": f"Error: {e}"
                }
                
        return results
    
    def validate_samples_structure(self) -> Dict[str, bool]:
        """
        Validate the structure of input-output samples.
        
        Returns:
            Dictionary with validation results for sample structure
        """
        results = {}
        
        samples_file = self.examples_dir / "input-output-samples.json"
        
        if not samples_file.exists():
            results["file_exists"] = False
            return results
            
        results["file_exists"] = True
            
        try:
            with open(samples_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            results["has_metadata"] = "metadata" in data
            results["has_samples"] = "samples" in data
            
            if "samples" in data and isinstance(data["samples"], list):
                results["samples_count"] = len(data["samples"]) > 0
                
                # Validate first sample structure
                if len(data["samples"]) > 0:
                    sample = data["samples"][0]
                    results["sample_has_id"] = "id" in sample
                    results["sample_has_input"] = "input" in sample
                    results["sample_has_expected_output"] = "expected_output" in sample
                else:
                    results["sample_has_id"] = False
                    results["sample_has_input"] = False
                    results["sample_has_expected_output"] = False
            else:
                results["samples_count"] = False
                    
        except Exception as e:
            results["error"] = str(e)
            
        return results
    
    def validate_dataset_structure(self) -> Dict[str, bool]:
        """
        Validate the structure of emotional cases dataset.
        
        Returns:
            Dictionary with validation results for dataset structure
        """
        results = {}
        
        dataset_file = self.examples_dir / "emotional-cases-dataset.json"
        
        if not dataset_file.exists():
            results["file_exists"] = False
            return results
            
        results["file_exists"] = True
            
        try:
            with open(dataset_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            results["has_metadata"] = "metadata" in data
            results["has_categories"] = "categories" in data
            
            if "categories" in data and isinstance(data["categories"], list):
                results["categories_count"] = len(data["categories"]) > 0
                
                # Count total cases
                total_cases = 0
                for category in data["categories"]:
                    if "cases" in category:
                        total_cases += len(category["cases"])
                        
                results["total_cases"] = total_cases > 0
            else:
                results["categories_count"] = False
                results["total_cases"] = False
                
        except Exception as e:
            results["error"] = str(e)
            
        return results
    
    def run_all_validations(self) -> Dict[str, Any]:
        """
        Run all validation tests.
        
        Returns:
            Dictionary with all validation results
        """
        return {
            "structure": self.validate_structure(),
            "json_files": self.validate_json_files(),
            "samples_structure": self.validate_samples_structure(),
            "dataset_structure": self.validate_dataset_structure()
        }
    
    def print_results(self, results: Dict[str, Any]) -> None:
        """
        Print validation results in a readable format.
        
        Args:
            results: Validation results dictionary
        """
        print("\n" + "=" * 70)
        print("EMOTIONAL COMPREHENSION PIPELINE VALIDATION RESULTS")
        print("=" * 70 + "\n")
        
        # Structure validation
        print("Repository Structure:")
        print("-" * 70)
        structure_results = results.get("structure", {})
        all_passed = all(structure_results.values())
        
        for item, passed in structure_results.items():
            status = "✓" if passed else "✗"
            print(f"  {status} {item}")
            
        print(f"\nStructure Validation: {'PASSED' if all_passed else 'FAILED'}")
        
        # JSON validation
        print("\n" + "-" * 70)
        print("JSON File Validation:")
        print("-" * 70)
        json_results = results.get("json_files", {})
        
        for filename, result in json_results.items():
            status = "✓" if result["valid"] else "✗"
            print(f"  {status} {filename}")
            if not result["valid"]:
                print(f"    Error: {result['error']}")
                
        # Samples structure
        print("\n" + "-" * 70)
        print("Input-Output Samples Structure:")
        print("-" * 70)
        samples_results = results.get("samples_structure", {})
        
        for key, value in samples_results.items():
            if key != "error":
                status = "✓" if value else "✗"
                print(f"  {status} {key}: {value}")
            else:
                print(f"  Error: {value}")
                
        # Dataset structure
        print("\n" + "-" * 70)
        print("Emotional Cases Dataset Structure:")
        print("-" * 70)
        dataset_results = results.get("dataset_structure", {})
        
        for key, value in dataset_results.items():
            if key != "error":
                status = "✓" if value else "✗"
                print(f"  {status} {key}: {value}")
            else:
                print(f"  Error: {value}")
                
        print("\n" + "=" * 70)
        
    def get_validation_status(self, results: Dict[str, Any]) -> bool:
        """
        Determine overall validation status.
        
        Args:
            results: Validation results dictionary
            
        Returns:
            True if all validations passed, False otherwise
        """
        structure_passed = all(results.get("structure", {}).values())
        json_passed = all(
            r["valid"] for r in results.get("json_files", {}).values()
        )
        
        # Check all sample structure validations (exclude non-boolean keys like 'error')
        samples_results = results.get("samples_structure", {})
        samples_passed = all(
            v for k, v in samples_results.items() 
            if k != "error" and isinstance(v, bool)
        ) if samples_results else False
        
        # Check all dataset structure validations (exclude non-boolean keys like 'error')
        dataset_results = results.get("dataset_structure", {})
        dataset_passed = all(
            v for k, v in dataset_results.items() 
            if k != "error" and isinstance(v, bool)
        ) if dataset_results else False
        
        return all([structure_passed, json_passed, samples_passed, dataset_passed])


def main():
    """Main entry point for the validation script."""
    print("\nStarting Emotional Comprehension Pipeline Validation...\n")
    
    validator = PipelineValidator()
    results = validator.run_all_validations()
    validator.print_results(results)
    
    # Exit with appropriate status code
    if validator.get_validation_status(results):
        print("\n✓ All validations passed!\n")
        sys.exit(0)
    else:
        print("\n✗ Some validations failed. Please review the results above.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
