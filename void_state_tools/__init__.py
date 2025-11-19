"""
Void-State Proprietary Tools Framework

This package provides the core infrastructure for the Void-State system's
proprietary tools - the internal analytical and operational primitives that
form the system's "nervous system" and "immune system."

Architecture:
    - Base tool interfaces and abstract classes
    - Tool registry and lifecycle management
    - VM and Kernel integration points
    - Communication and coordination infrastructure
    - Resource management and monitoring

Usage:
    from void_state_tools import Tool, ToolRegistry
    from void_state_tools.memory import StructuralMemoryDiffAnalyzer
    
    # Create and register a tool
    tool = StructuralMemoryDiffAnalyzer(config)
    registry = ToolRegistry()
    handle = registry.attach_tool(tool)
"""

__version__ = "1.0.0"
__author__ = "Void-State Development Team"

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
)

__all__ = [
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
]
