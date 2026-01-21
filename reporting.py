import matplotlib.pyplot as plt

def generate_plots(results):
    sizes = results['sizes']
    
    plt.figure()
    plt.plot(sizes, results['naive_time'], 'r-o', label='Naive (Slow)')
    plt.plot(sizes, results['optimized_time'], 'g-o', label='Windowed (Fast)')
    plt.xlabel('Number of Ticks')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('runtime_scaling.png')
    print("Saved runtime_scaling.png")
    
    plt.figure()
    plt.plot(sizes, results['naive_mem'], 'r-o', label='Naive Memory')
    plt.plot(sizes, results['optimized_mem'], 'g-o', label='Windowed Memory')
    plt.xlabel('Number of Ticks')
    plt.ylabel('Memory (MiB)')
    plt.title('Memory Usage Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('memory_scaling.png')
    print("Saved memory_scaling.png")

def create_markdown_report(results):
    report = "# Complexity Report\n\n"
    report += "| Ticks | Naive Time | Optimized Time | Naive Mem | Optimized Mem |\n"
    report += "|---|---|---|---|---|\n"
    
    for i in range(len(results['sizes'])):
        s = results['sizes'][i]
        nt = results['naive_time'][i]
        ot = results['optimized_time'][i]
        nm = results['naive_mem'][i]
        om = results['optimized_mem'][i]
        
        report += f"| {s} | {nt:.4f}s | {ot:.4f}s | {nm:.2f}MB | {om:.2f}MB |\n"
        
    with open("complexity_report.md", "w") as f:
        f.write(report)
    print("Saved complexity_report.md")