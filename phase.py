import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sDivRatio = "Div Ratio : 19.25"
sRefClk = "Ref Clk : 625MHz"
sDtcPCount = "DTC_P_COUNT : 1"
sDCOClk = "DCO Clk : 12.03GHz"
titleText = f"{sDivRatio}, {sRefClk}, {sDtcPCount}, {sDCOClk}"

# Consume and convert data
phase_error_dat = pd.read_csv('phase_err_check.csv', delimiter=",")
phase_error_sim_time = phase_error_dat.iloc[:, 2].to_numpy() / 1e12
phase_error = phase_error_dat.iloc[:, 7].to_numpy()

# Filter out phase error which are bigger than 5000
todel = np.abs(phase_error) > 5000
phase_error = phase_error[~todel]
phase_error_sim_time = phase_error_sim_time[~todel]

# 1200 pixels wide and 500 pixels high
plt.figure(figsize=(12, 5), dpi=100)

# Show the maximum phase errors with their sim time
plt.subplot(2, 6, (1, 2, 3))
plt.plot(phase_error_sim_time, phase_error)
plt.title(f'PD Phase Error: {titleText}')
plt.grid(True)
plt.xlabel('sim time (ms)')
plt.ylabel('phase error (fs)')
vMax = np.max(phase_error)
indexOfMax = np.argmax(phase_error)
tMax = phase_error_sim_time[indexOfMax]
plt.text(tMax, vMax, f'Max {vMax} fs', fontsize=15, verticalalignment='top', horizontalalignment='right')
# plt.text(tMax, vMax, f'Max {vMax:.2f} fs', fontsize=15, verticalalignment='top', horizontalalignment='right')

# Show the PD Phase Error Discribution
plt.subplot(2, 6, (5, 6))
H = plt.hist(phase_error, bins='auto')
u = np.mean(phase_error)
s = np.std(phase_error)
vMax = np.max(H[0])
plt.text(0, vMax, f'Mean={u:.2f}fs, Std={s:.1f}fs', fontsize=15, verticalalignment='top', horizontalalignment='center')
plt.title(f'PD Phase Error Distribution: {titleText}')

# Display the plot
plt.tight_layout()
plt.show()
