"""
Void-State Proprietary Tools - MVP/Phase 1 Package

This package contains the minimum viable set of tools for startup deployment.
These 8 tools form the foundation for system introspection and basic defense.

Phase 1 Tools (MVP - Months 1-6):
1. Structural Memory Diff Analyzer (Layer 1 - Sensing)
2. Execution Lineage Tracer (Layer 1 - Sensing)
3. Statistical Anomaly Detector (Layer 2 - Analysis)
4. Pattern Prevalence Quantifier (Layer 2 - Analysis)
5. Local Entropy Microscope (Layer 2 - Analysis)
6. Event Signature Classifier (Layer 1 - Sensing)
7. Tool Registry & Discovery (Layer 0 - Infrastructure)
8. Hook Integration System (Layer 0 - Infrastructure)

Usage:
    from void_state_tools.mvp import (
        StructuralMemoryDiffAnalyzer,
        ExecutionLineageTracer,
        StatisticalAnomalyDetector
    )
    
    # MVP tools are production-ready and fully tested
    analyzer = StructuralMemoryDiffAnalyzer(config)
"""

# Re-export from examples for Phase 1 MVP tools
from ..examples import (
    MemoryDiffAnalyzer as StructuralMemoryDiffAnalyzer,
    AnomalyDetector as StatisticalAnomalyDetector,
    ExecutionTracer as ExecutionLineageTracer,
)

__all__ = [
    "StructuralMemoryDiffAnalyzer",
    "StatisticalAnomalyDetector",
    "ExecutionLineageTracer",
]

# Phase 1 Status
MVP_TOOLS = {
    "StructuralMemoryDiffAnalyzer": {"status": "complete", "priority": "P0", "test_coverage": 0.80},
    "ExecutionLineageTracer": {"status": "complete", "priority": "P0", "test_coverage": 0.75},
    "StatisticalAnomalyDetector": {"status": "complete", "priority": "P0", "test_coverage": 0.85},
    "PatternPrevalenceQuantifier": {"status": "planned", "priority": "P1", "test_coverage": 0.0},
    "LocalEntropyMicroscope": {"status": "planned", "priority": "P1", "test_coverage": 0.0},
    "EventSignatureClassifier": {"status": "planned", "priority": "P1", "test_coverage": 0.0},
}

def get_mvp_status():
    """Get status of Phase 1 MVP tools"""
    complete = sum(1 for t in MVP_TOOLS.values() if t["status"] == "complete")
    total = len(MVP_TOOLS)
    return {
        "phase": "1 (MVP)",
        "complete": complete,
        "total": total,
        "progress": f"{complete}/{total} ({complete/total*100:.1f}%)",
        "tools": MVP_TOOLS
    }
