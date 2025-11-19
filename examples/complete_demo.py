#!/usr/bin/env python3
"""
Example Application: Complete Void-State Tools Demo

Usage: python examples/complete_demo.py
"""

import time
import sys

from void_state_tools import ToolRegistry, ToolConfig, get_deployment_status
from void_state_tools.mvp import (
    PatternPrevalenceQuantifier,
    LocalEntropyMicroscope,
    EventSignatureClassifier
)
from void_state_tools.monitoring import start_metrics_server

def main():
    print("="*60)
    print("VOID-STATE TOOLS - DEMO")
    print("="*60)
    
    # Start metrics server
    print("\nStarting metrics server on port 9090...")
    start_metrics_server(port=9090)
    
    # Setup tools
    registry = ToolRegistry()
    
    print("\nInitializing tools...")
    pattern_tool = PatternPrevalenceQuantifier(ToolConfig())
    pattern_tool.initialize()
    
    entropy_tool = LocalEntropyMicroscope(ToolConfig())
    entropy_tool.initialize()
    
    classifier = EventSignatureClassifier(ToolConfig())
    classifier.initialize()
    
    # Demo pattern analysis
    print("\n1. Pattern Analysis:")
    for pattern in ["login", "api_call", "login", "db_query"]:
        result = pattern_tool.analyze({
            "pattern": pattern,
            "context": "web",
            "timestamp": time.time()
        })
        print(f"  {pattern}: freq={result['frequency']}")
    
    # Demo entropy monitoring
    print("\n2. Entropy Monitoring:")
    for i in range(3):
        result = entropy_tool.observe_region("cpu_0", 100 + i)
        print(f"  cpu_0: entropy={result['entropy']:.2f}")
    
    # Demo event classification
    print("\n3. Event Classification:")
    event = {"type": "memory_allocation", "size": 1024}
    result = classifier.classify_event(event)
    print(f"  Classified: {result['classification']}")
    
    print("\n✓ Demo complete!")
    print("Metrics: http://localhost:9090/metrics")

if __name__ == "__main__":
    main()
