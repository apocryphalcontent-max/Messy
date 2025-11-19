"""
Unit tests for Void-State Tools Framework

Comprehensive test suite covering all core components.
Run with: pytest void_state_tools/tests/ -v --cov=void_state_tools
"""

import pytest
import time
from typing import Dict, Any

from void_state_tools.base import (
    Tool, ToolState, ToolConfig, ToolHandle,
    AnalysisTool, InterceptorTool, MonitoringTool
)
from void_state_tools.registry import (
    ToolRegistry, ToolLifecycleManager,
    ToolRegistrationError, ToolNotFoundError, ToolLifecycleError
)
from void_state_tools.hooks import (
    HookPoint, HookContext, HookTiming, HookPriority,
    VMHooks, KernelHooks, HookRegistry,
    FrequencyFilter, TimeWindowFilter, ConditionalFilter
)


class MockTool(Tool):
    """Mock tool for testing"""
    
    def __init__(self, config: ToolConfig):
        super().__init__(config)
        self.initialized = False
        self.suspended = False
    
    def initialize(self) -> bool:
        self.initialized = True
        return True
    
    def shutdown(self) -> bool:
        self.initialized = False
        return True
    
    def suspend(self) -> bool:
        self.suspended = True
        return True
    
    def resume(self) -> bool:
        self.suspended = False
        return True
    
    def get_metadata(self) -> Dict[str, Any]:
        return {
            "name": "Mock Tool",
            "category": "test",
            "version": "1.0.0",
            "description": "A mock tool for testing",
            "capabilities": set(),
            "dependencies": set()
        }


class TestToolBase:
    """Tests for base Tool classes"""
    
    def test_tool_creation(self):
        config = ToolConfig(tool_name="test_tool", tool_category="test")
        tool = MockTool(config)
        assert tool.config == config
        assert tool.tool_id == config.tool_id
    
    def test_tool_initialization(self):
        tool = MockTool(ToolConfig())
        assert tool.initialize()
        assert tool.initialized
    
    def test_tool_config_defaults(self):
        config = ToolConfig()
        assert config.max_memory_mb == 100
        assert config.max_cpu_percent == 10
    
    def test_tool_lifecycle(self):
        tool = MockTool(ToolConfig())
        assert tool.initialize()
        assert tool.suspend()
        assert tool.suspended
        assert tool.resume()
        assert not tool.suspended
        assert tool.shutdown()


class TestToolRegistry:
    """Tests for ToolRegistry"""
    
    def test_tool_registration(self):
        registry = ToolRegistry()
        tool = MockTool(ToolConfig(tool_name="test"))
        handle = registry.register_tool(tool)
        assert handle.state == ToolState.DORMANT
    
    def test_duplicate_registration(self):
        registry = ToolRegistry()
        config = ToolConfig(tool_id="duplicate")
        registry.register_tool(MockTool(config))
        with pytest.raises(ToolRegistrationError):
            registry.register_tool(MockTool(config))
    
    def test_list_tools(self):
        registry = ToolRegistry()
        registry.register_tool(MockTool(ToolConfig(tool_category="cat1")))
        registry.register_tool(MockTool(ToolConfig(tool_category="cat2")))
        assert len(registry.list_tools()) == 2
        assert len(registry.list_tools(category="cat1")) == 1


class TestLifecycleManager:
    """Tests for ToolLifecycleManager"""
    
    def test_attach_detach(self):
        registry = ToolRegistry()
        tool = MockTool(ToolConfig())
        handle = registry.register_tool(tool)
        
        assert registry.lifecycle_manager.attach_tool(handle.tool_id)
        assert handle.state == ToolState.ACTIVE
        
        assert registry.lifecycle_manager.detach_tool(handle.tool_id)
        assert handle.state == ToolState.TERMINATED
    
    def test_suspend_resume(self):
        registry = ToolRegistry()
        tool = MockTool(ToolConfig())
        handle = registry.register_tool(tool)
        
        registry.lifecycle_manager.attach_tool(handle.tool_id)
        assert registry.lifecycle_manager.suspend_tool(handle.tool_id)
        assert handle.state == ToolState.SUSPENDED
        
        assert registry.lifecycle_manager.resume_tool(handle.tool_id)
        assert handle.state == ToolState.ACTIVE


class TestHookSystem:
    """Tests for hook system"""
    
    def test_hook_registration_and_execution(self):
        hook = HookPoint("test", HookTiming.BEFORE)
        results = []
        hook.register(lambda ctx: results.append(True))
        
        context = HookContext(time.time(), 0, 0, {})
        hook.execute(context)
        assert len(results) == 1
    
    def test_hook_priority(self):
        hook = HookPoint("test", HookTiming.BEFORE)
        order = []
        hook.register(lambda ctx: order.append("low"), priority=10)
        hook.register(lambda ctx: order.append("high"), priority=100)
        
        hook.execute(HookContext(time.time(), 0, 0, {}))
        assert order == ["high", "low"]
    
    def test_frequency_filter(self):
        filter = FrequencyFilter(sample_rate=0.5)
        context = HookContext(time.time(), 0, 0, {})
        results = [filter.should_trigger(context) for _ in range(100)]
        assert 30 <= sum(results) <= 70  # Approximately 50%


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
