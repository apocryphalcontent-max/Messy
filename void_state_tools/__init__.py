"""
Void-State Proprietary Tools Framework

This package provides the core infrastructure for the Void-State system's
proprietary tools - the internal analytical and operational primitives that
form the system's "nervous system" and "immune system."

Architecture - Layered & Phased:
    Layer 0: Integration Substrate (Hook System, Tool Registry)
    Layer 1: Sensing & Instrumentation (Memory Diff, Execution Tracing)
    Layer 2: Analysis & Intelligence (Anomaly Detection, Pattern Recognition)
    Layer 3: Cognitive & Predictive (Timeline Branching, Prophecy)
    Layer 4: Meta & Evolution (Tool Synthesis, Self-Modification)

Phased Deployment:
    Phase 1 (MVP): 8 essential tools - Months 1-6
    Phase 2 (Growth): +15 tools - Months 7-18
    Phase 3 (Advanced): +24 tools - Months 19-36

Usage:
    # MVP/Phase 1 Tools (Production Ready)
    from void_state_tools import Tool, ToolRegistry
    from void_state_tools.mvp import (
        StructuralMemoryDiffAnalyzer,
        StatisticalAnomalyDetector,
        ExecutionLineageTracer
    )
    
    # Create and register a tool
    tool = StructuralMemoryDiffAnalyzer(config)
    registry = ToolRegistry()
    handle = registry.register_tool(tool)
    registry.lifecycle_manager.attach_tool(handle.tool_id)
    
    # Check deployment status
    from void_state_tools import get_deployment_status
    status = get_deployment_status()
    print(f"Phase 1: {status['phase1']['progress']}")
"""

__version__ = "1.0.0-mvp"
__author__ = "Void-State Development Team"
__phase__ = "1 (MVP)"

from .base import (
    Tool,
    ToolState,
    ToolConfig,
    ToolHandle,
    ToolMetrics,
)

from .registry import (
    ToolRegistry,
    ToolLifecycleManager,
)

from .hooks import (
    HookPoint,
    VMHooks,
    KernelHooks,
    HookRegistry,
)

# Phase-specific imports
from . import mvp
from . import phase2
from . import phase3

__all__ = [
    # Core infrastructure (Layer 0)
    "Tool",
    "ToolState",
    "ToolConfig",
    "ToolHandle",
    "ToolMetrics",
    "ToolRegistry",
    "ToolLifecycleManager",
    "HookPoint",
    "VMHooks",
    "KernelHooks",
    "HookRegistry",
    
    # Phase modules
    "mvp",
    "phase2",
    "phase3",
    
    # Utility functions
    "get_deployment_status",
]

def get_deployment_status():
    """
    Get status of all deployment phases.
    
    Returns:
        dict: Status of Phase 1, 2, and 3 with progress metrics
    """
    return {
        "version": __version__,
        "current_phase": __phase__,
        "phase1": mvp.get_mvp_status(),
        "phase2": phase2.get_phase2_status(),
        "phase3": phase3.get_phase3_status(),
        "total_tools": {
            "complete": 3,
            "planned": 44,
            "total": 47
        }
    }
