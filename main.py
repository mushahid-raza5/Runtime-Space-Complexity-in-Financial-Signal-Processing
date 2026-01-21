import csv
import random
from datetime import datetime, timedelta
import os

from data_loader import load_market_data
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from profiler import run_benchmark
from reporting import generate_plots, create_markdown_report

def make_dummy_file():
    print("No CSV found. Creating dummy data...")
    with open("market_data.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "symbol", "price"])
        
        price = 100.0
        now = datetime.now()
        
        for i in range(100000):
            t = now + timedelta(seconds=i)
            price += random.uniform(-1, 1)
            writer.writerow([t.isoformat(), "AAPL", round(price, 2)])
    print("Done creating file.")

def main():
    if not os.path.exists("market_data.csv"):
        make_dummy_file()
    print("Loading data...")
    full_data = load_market_data("market_data.csv")
    test_sizes = [1000, 10000, 100000]
    
    results = {
        'sizes': test_sizes,
        'naive_time': [], 'optimized_time': [],
        'naive_mem': [], 'optimized_mem': []
    }
    
    for count in test_sizes:
        print(f"\n--- Testing with {count} ticks ---")
        subset = full_data[:count]
        
        print("Running Naive Strategy...")
        t, m = run_benchmark(NaiveMovingAverageStrategy, subset)
        results['naive_time'].append(t)
        results['naive_mem'].append(m)
        print(f"Time: {t:.4f}s")
        
        print("Running Windowed Strategy...")
        t, m = run_benchmark(WindowedMovingAverageStrategy, subset, window_size=50)
        results['optimized_time'].append(t)
        results['optimized_mem'].append(m)
        print(f"Time: {t:.4f}s")

    print("\nGenerating report...")
    generate_plots(results)
    create_markdown_report(results)
    print("All done!")

if __name__ == "__main__":
    main()