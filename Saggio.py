import matplotlib.pyplot as plt
import numpy as np

# Generating sample data for the graphs
data_categories = ['Latency (ms)', 'Bandwidth (Mbps)', 'Coverage (%)', 'Cost ($ per GB)']
starlink = [25, 200, 95, 70]  # Hypothetical values
kuiper = [30, 150, 90, 75]
traditional_satellites = [600, 50, 80, 90]

# Graph 1: Comparison of Starlink, Kuiper, and Traditional Satellites
fig1, ax1 = plt.subplots(figsize=(10, 6))
bar_width = 0.25
x = np.arange(len(data_categories))

ax1.bar(x - bar_width, starlink, width=bar_width, label='Starlink', color='dodgerblue', edgecolor='black')
ax1.bar(x, kuiper, width=bar_width, label='Kuiper', color='limegreen', edgecolor='black')
ax1.bar(x + bar_width, traditional_satellites, width=bar_width, label='Traditional Satellites', color='tomato', edgecolor='black')

ax1.set_xticks(x)
ax1.set_xticklabels(data_categories, fontsize=12)
ax1.set_ylabel('Performance Metrics', fontsize=12)
ax1.set_title('Performance Comparison of Satellite Systems', fontsize=14, fontweight='bold')
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('performance_comparison.png')
plt.show()

# Graph 2: Projected Growth of Satellites in Orbit
years = [2024, 2025, 2026, 2027, 2028]
starlink_growth = [3000, 4000, 6000, 8000, 10000]
kuiper_growth = [500, 1500, 3500, 5500, 7000]

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(years, starlink_growth, marker='o', label='Starlink', color='dodgerblue', linewidth=2, markersize=8)
ax2.plot(years, kuiper_growth, marker='s', label='Kuiper', color='limegreen', linewidth=2, markersize=8)

ax2.set_title('Projected Growth of Satellites in Orbit (2024-2028)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Number of Satellites', fontsize=12)
ax2.legend(fontsize=10, loc='upper left')
ax2.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('growth_projection.png')
plt.show()

# Graph 3: Network Latency vs. Distance
latency = [20, 40, 60, 80, 100, 120]
distance = [200, 400, 600, 800, 1000, 1200]

fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.plot(distance, latency, label='Starlink/Kuiper LEO', color='dodgerblue', linewidth=2, marker='o', markersize=8)

# Adding hypothetical geostationary satellite latency
geo_latency = [600 for _ in distance]
ax3.plot(distance, geo_latency, label='Traditional GEO Satellites', linestyle='--', color='tomato', linewidth=2, marker='x', markersize=8)

ax3.set_title('Network Latency vs. Distance', fontsize=14, fontweight='bold')
ax3.set_xlabel('Distance (km)', fontsize=12)
ax3.set_ylabel('Latency (ms)', fontsize=12)
ax3.legend(fontsize=10, loc='upper left')
ax3.grid(linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('latency_distance.png')
plt.show()

# Summary
print("Graphs generated to explain the technological advancements, challenges, and future prospects of satellite-based networks like Starlink and Kuiper.")
print("The graphs illustrate: 1) Performance comparison, 2) Projected growth, and 3) Latency analysis.")
