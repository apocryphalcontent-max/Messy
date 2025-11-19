"""
Tests for MVP tool implementations
"""

import pytest
from void_state_tools.mvp import (
    StructuralMemoryDiffAnalyzer,
    StatisticalAnomalyDetector,
    ExecutionLineageTracer,
    get_mvp_status
)
from void_state_tools.base import ToolConfig


class TestMVPTools:
    """Tests for Phase 1 MVP tools"""
    
    def test_mvp_status(self):
        """Test MVP status reporting"""
        status = get_mvp_status()
        assert status["phase"] == "1 (MVP)"
        assert "complete" in status
        assert "total" in status
        assert status["complete"] >= 3  # At least 3 complete
    
    def test_memory_diff_analyzer(self):
        """Test Structural Memory Diff Analyzer"""
        config = ToolConfig(tool_name="memory_analyzer")
        tool = StructuralMemoryDiffAnalyzer(config)
        
        assert tool.initialize()
        metadata = tool.get_metadata()
        assert metadata["name"] == "Memory Diff Analyzer"
        assert metadata["category"] == "memory_diff_analyzers"
        assert tool.shutdown()
    
    def test_anomaly_detector(self):
        """Test Statistical Anomaly Detector"""
        config = ToolConfig(tool_name="anomaly_detector")
        tool = StatisticalAnomalyDetector(config)
        
        assert tool.initialize()
        metadata = tool.get_metadata()
        assert metadata["name"] == "Anomaly Detector"
        assert tool.shutdown()
    
    def test_execution_tracer(self):
        """Test Execution Lineage Tracer"""
        config = ToolConfig(tool_name="exec_tracer")
        tool = ExecutionLineageTracer(config)
        
        assert tool.initialize()
        metadata = tool.get_metadata()
        assert metadata["name"] == "Execution Tracer"
        assert tool.shutdown()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
