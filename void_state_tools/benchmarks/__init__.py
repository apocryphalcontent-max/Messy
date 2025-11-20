"""
Performance benchmarking utilities for Void-State Tools

Run with: python -m void_state_tools.benchmarks
"""

import time
import statistics
from typing import List
from dataclasses import dataclass

from void_state_tools.hooks import HookPoint, HookContext, HookTiming
from void_state_tools.base import ToolConfig
from void_state_tools.registry import ToolRegistry


@dataclass
class BenchmarkResult:
    """Results from a benchmark run"""
    name: str
    iterations: int
    min_ns: float
    max_ns: float
    mean_ns: float
    median_ns: float
    stddev_ns: float
    p95_ns: float
    p99_ns: float
    overhead_percent: float


class PerformanceBenchmark:
    """Performance benchmarking for tools and hooks"""
    
    def __init__(self, iterations: int = 10000):
        self.iterations = iterations
        self.results: List[BenchmarkResult] = []
    
    def benchmark_hook_overhead(self) -> BenchmarkResult:
        """Benchmark hook system overhead"""
        print(f"Benchmarking hook overhead ({self.iterations} iterations)...")
        
        hook = HookPoint("benchmark.hook", HookTiming.BEFORE, overhead_budget_ns=100)
        hook.register(lambda ctx: None)
        
        timings = []
        for i in range(self.iterations):
            context = HookContext(time.time(), i, 0, {})
            start = time.perf_counter_ns()
            hook.execute(context)
            end = time.perf_counter_ns()
            timings.append(end - start)
        
        result = self._calculate_stats("Hook Overhead", timings, budget_ns=100)
        self.results.append(result)
        return result
    
    def _calculate_stats(self, name: str, timings: List[float], budget_ns: float) -> BenchmarkResult:
        """Calculate statistics from timing data"""
        sorted_timings = sorted(timings)
        
        p95_idx = int(len(sorted_timings) * 0.95)
        p99_idx = int(len(sorted_timings) * 0.99)
        
        return BenchmarkResult(
            name=name,
            iterations=len(timings),
            min_ns=min(timings),
            max_ns=max(timings),
            mean_ns=statistics.mean(timings),
            median_ns=statistics.median(timings),
            stddev_ns=statistics.stdev(timings) if len(timings) > 1 else 0,
            p95_ns=sorted_timings[p95_idx],
            p99_ns=sorted_timings[p99_idx],
            overhead_percent=(statistics.mean(timings) / budget_ns) * 100 if budget_ns > 0 else 0
        )
    
    def print_results(self):
        """Print benchmark results"""
        print("\n" + "="*80)
        print("PERFORMANCE BENCHMARK RESULTS")
        print("="*80)
        
        for result in self.results:
            print(f"\n{result.name}:")
            print(f"  Mean: {result.mean_ns:,.0f} ns | P95: {result.p95_ns:,.0f} ns | P99: {result.p99_ns:,.0f} ns")
            status = "✓ PASS" if result.overhead_percent < 100 else "✗ FAIL"
            print(f"  Overhead: {result.overhead_percent:.1f}% {status}")
    
    def run_all(self):
        """Run all benchmarks"""
        self.benchmark_hook_overhead()
        self.print_results()


def main():
    benchmark = PerformanceBenchmark(iterations=10000)
    benchmark.run_all()


if __name__ == "__main__":
    main()
