import time
from memory_profiler import memory_usage

def get_execution_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

def get_memory_peak(func, *args):
    mem_usage = memory_usage((func, args), interval=0.1, timeout=None)
    return max(mem_usage) - min(mem_usage)

def run_benchmark(strategy_class, data, **kwargs):
    strategy = strategy_class(**kwargs)
    
    def run_strategy():
        for tick in data:
            strategy.generate_signals(tick)
            
    time_taken = get_execution_time(run_strategy)
    
    strategy_for_mem = strategy_class(**kwargs)
    def run_strategy_mem():
        for tick in data:
            strategy_for_mem.generate_signals(tick)
            
    mem_used = get_memory_peak(run_strategy_mem)
    
    return time_taken, mem_used