"""
================================================================================
   60-SECOND 3D ANIMATION: SIGNAL PROCESSING & NOISE ANALYSIS IN MASERS
   Noise Temperature | Power Spectral Density | Schawlow-Townes Linewidth
   Fourier Transform | FID Signal | Lorentzian Lineshape
   
   Beautiful 3D effects | Vibrant colors | All moving elements - FIXED
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("60-SECOND 3D ANIMATION: SIGNAL PROCESSING & NOISE ANALYSIS")
print("="*80)

print("Rendering 600 frames...")

import tempfile
import os
import imageio

temp_dir = tempfile.mkdtemp()
frame_files = []

for frame in range(600):
    fig = plt.figure(figsize=(16, 9))
    fig.patch.set_facecolor('#0A0A2A')
    
    scene = frame // 75
    sub_frame = frame % 75
    
    # ==================== SCENE 1: NOISE TEMPERATURE (0-75) ====================
    if scene == 0:
        # Left: 3D noise visualization
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('MASER NOISE TEMPERATURE', color='#FFD700', fontsize=14, fontweight='bold')
        
        # Noise particles
        for i in range(50):
            x = 2 * np.random.randn() * 0.5
            y = 1.5 * np.random.randn() * 0.5
            z = 1.5 * np.random.randn() * 0.5
            size = 20 + 30 * np.random.rand()
            alpha = 0.3 + 0.5 * np.random.rand()
            ax1.scatter(x, y, z, color='#FF3366', s=size, alpha=alpha)
        
        # Quantum limit sphere
        u = np.linspace(0, 2*np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x_sphere = 0.8 * np.outer(np.cos(u), np.sin(v))
        y_sphere = 0.8 * np.outer(np.sin(u), np.sin(v))
        z_sphere = 0.8 * np.outer(np.ones(np.size(u)), np.cos(v))
        ax1.plot_surface(x_sphere, y_sphere, z_sphere, color='#33FF66', alpha=0.2)
        
        ax1.text(0, 0, 1.5, 'Quantum Limit', color='#33FF66', fontsize=10, ha='center')
        ax1.view_init(elev=25, azim=frame * 0.5)
        
        # Right: Noise temperature equation
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'MASER NOISE TEMPERATURE', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        # Main equation
        rect = FancyBboxPatch((2, 5), 6, 1.5, boxstyle="round,pad=0.3", facecolor='#FF3366', alpha=0.2, edgecolor='#FF3366', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, 6.2, 'T_N = h w0 / [k_B ln(N_e/N_g)]', color='#FF3366', fontsize=14, fontweight='bold', ha='center')
        
        # Quantum limit
        rect2 = FancyBboxPatch((2, 3), 6, 1.2, boxstyle="round,pad=0.3", facecolor='#33FF66', alpha=0.2, edgecolor='#33FF66', linewidth=2)
        ax2.add_patch(rect2)
        ax2.text(5, 3.8, 'Quantum Limit: T_N -> h w0/k_B', color='#33FF66', fontsize=13, fontweight='bold', ha='center')
        
        # Explanation
        ax2.text(5, 2.0, 'Maser advantage: Extremely low noise', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(5, 1.4, 'Inversion ratio N_e/N_g determines noise floor', color='#FFA500', fontsize=11, ha='center')
    
    # ==================== SCENE 2: POWER SPECTRAL DENSITY (75-150) ====================
    elif scene == 1:
        # Left: 3D spectrum visualization
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('POWER SPECTRAL DENSITY', color='#FFD700', fontsize=14, fontweight='bold')
        
        # 3D spectrum plot
        freq = np.linspace(-2, 2, 30)
        psd = 1 / (1 + freq**2)
        for i, f in enumerate(freq):
            x = f
            y = -0.5
            z = psd[i]
            ax1.bar3d(x, y, 0, 0.1, 0.1, z, color='#FF66CC', alpha=0.7)
        
        # Moving peak indicator
        peak_pos = -1.5 + sub_frame / 75 * 3
        ax1.scatter(peak_pos, -0.5, 1, color='#FFD700', s=100, alpha=0.9)
        
        ax1.set_xlabel('Frequency', color='white', fontsize=9)
        ax1.set_ylabel('Power', color='white', fontsize=9)
        ax1.view_init(elev=25, azim=frame * 0.5)
        
        # Right: Schawlow-Townes linewidth
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'SCHAWLOW-TOWNES LINEWIDTH', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        # Main equation
        rect = FancyBboxPatch((1.5, 5), 7, 1.5, boxstyle="round,pad=0.3", facecolor='#FF66CC', alpha=0.2, edgecolor='#FF66CC', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, 6.2, 'Dn_ST = p h n0^2 (Dn_c)^2 / P_out', color='#FF66CC', fontsize=13, fontweight='bold', ha='center')
        
        # Explanation
        ax2.text(5, 4.0, 'Fundamental maser linewidth', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(5, 3.4, 'Due to quantum phase diffusion', color='#FFFFFF', fontsize=11, ha='center')
        ax2.text(5, 2.8, 'Sets limit to frequency stability', color='#FFA500', fontsize=11, ha='center')
        
        # Moving power indicator
        power = 0.5 + 0.5 * np.sin(frame * 0.05)
        ax2.text(5, 2.0, f'Output Power: {power:.2f} mW', color='#33FF66', fontsize=12, fontweight='bold', ha='center')
    
    # ==================== SCENE 3: FOURIER TRANSFORM (150-225) ====================
    elif scene == 2:
        # Left: 3D time domain signal
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('TIME DOMAIN: FID SIGNAL', color='#FFD700', fontsize=14, fontweight='bold')
        
        # FID signal
        t_vals = np.linspace(-2, 2, 50)
        decay = np.exp(-abs(t_vals) * 2)
        signal = decay * np.cos(10 * t_vals)
        
        progress = sub_frame / 75
        for i, ti in enumerate(t_vals):
            if ti < progress * 4 - 2:
                ax1.bar3d(ti, -0.5, 0, 0.08, 0.08, signal[i] + 1, color='#33FF66', alpha=0.8)
        
        ax1.set_xlabel('Time', color='white', fontsize=9)
        ax1.set_ylabel('Amplitude', color='white', fontsize=9)
        ax1.view_init(elev=25, azim=frame * 0.5)
        
        # Right: Fourier transform equation
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'FOURIER TRANSFORM', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        # Fourier equation
        rect = FancyBboxPatch((1.5, 5.2), 7, 1.2, boxstyle="round,pad=0.3", facecolor='#33FF66', alpha=0.2, edgecolor='#33FF66', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, 5.9, 'S(w) = INT S(t) e^{-iwt} dt', color='#33FF66', fontsize=14, fontweight='bold', ha='center')
        
        # FID equation
        rect2 = FancyBboxPatch((1.5, 3.5), 7, 1.2, boxstyle="round,pad=0.3", facecolor='#FFA500', alpha=0.2, edgecolor='#FFA500', linewidth=2)
        ax2.add_patch(rect2)
        ax2.text(5, 4.2, 'S(t) = S0 e^{-t/T2*} e^{iw0t}', color='#FFA500', fontsize=13, fontweight='bold', ha='center')
        
        ax2.text(5, 2.5, 'Free Induction Decay (FID)', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(5, 1.9, 'T2* includes inhomogeneous broadening', color='#FFD700', fontsize=11, ha='center')
    
    # ==================== SCENE 4: LORENTZIAN LINEWIDTH (225-300) ====================
    elif scene == 3:
        # Left: 3D Lorentzian
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('FREQUENCY DOMAIN: LORENTZIAN', color='#FFD700', fontsize=14, fontweight='bold')
        
        # Lorentzian curve
        x_vals = np.linspace(-2, 2, 30)
        y_vals = 1 / (1 + x_vals**2)
        
        for i, xi in enumerate(x_vals):
            ax1.bar3d(xi, -0.5, 0, 0.08, 0.08, y_vals[i] + 0.5, color='#FF3366', alpha=0.8)
        
        # Moving linewidth indicator
        linewidth_pos = 1 / (1 + (sub_frame/75 * 3 - 1.5)**2)
        ax1.scatter(sub_frame/75 * 3 - 1.5, -0.5, linewidth_pos + 0.5, color='#FFD700', s=100)
        
        ax1.set_xlabel('Frequency (w-w0)', color='white', fontsize=9)
        ax1.set_ylabel('Power', color='white', fontsize=9)
        ax1.view_init(elev=25, azim=frame * 0.5)
        
        # Right: Lorentzian equation
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'LORENTZIAN LINEWIDTH', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        # Lorentzian equation
        rect = FancyBboxPatch((1.5, 5), 7, 1.2, boxstyle="round,pad=0.3", facecolor='#FF3366', alpha=0.2, edgecolor='#FF3366', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, 5.7, '|S(w)|^2 = S0^2 (T2*)^2 / [1 + (w-w0)^2(T2*)^2]', color='#FF3366', fontsize=11, fontweight='bold', ha='center')
        
        # Linewidth relation
        rect2 = FancyBboxPatch((2, 3.2), 6, 1, boxstyle="round,pad=0.3", facecolor='#33FF66', alpha=0.2, edgecolor='#33FF66', linewidth=2)
        ax2.add_patch(rect2)
        ax2.text(5, 3.7, 'Dn = 1 / (p T2*)', color='#33FF66', fontsize=14, fontweight='bold', ha='center')
        
        ax2.text(5, 2.2, 'Linewidth determined by decoherence time', color='#FFFFFF', fontsize=11, ha='center')
        ax2.text(5, 1.6, 'Narrower linewidth = Better frequency stability', color='#FFA500', fontsize=11, ha='center')
    
    # ==================== SCENE 5: SIGNAL PROCESSING CHAIN (300-375) ====================
    elif scene == 4:
        # Left: 3D signal processing chain
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('SIGNAL PROCESSING CHAIN', color='#FFD700', fontsize=14, fontweight='bold')
        
        # Blocks
        blocks = [('Signal', -2, 0, 0.5), ('FT', -0.5, 0, 0.5), ('Filter', 1, 0, 0.5), ('Output', 2.5, 0, 0.5)]
        
        for name, x, y, z in blocks:
            ax1.bar3d(x-0.3, y-0.3, z-0.2, 0.6, 0.6, 0.4, color='#33FF66', alpha=0.5, edgecolor='#33FF66')
            ax1.text(x, y, z, name, color='white', fontsize=8, ha='center')
        
        # Arrows between blocks
        ax1.plot([-1.5, -0.8], [0, 0], [0.5, 0.5], 'y-', linewidth=2)
        ax1.plot([-0.2, 0.7], [0, 0], [0.5, 0.5], 'y-', linewidth=2)
        ax1.plot([1.3, 2.2], [0, 0], [0.5, 0.5], 'y-', linewidth=2)
        
        ax1.view_init(elev=25, azim=frame * 0.4)
        
        # Right: Processing explanation
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'SIGNAL PROCESSING STEPS', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        steps = [
            ('1', 'Time-domain signal acquisition', '#FF3366'),
            ('2', 'Fourier Transform to frequency domain', '#33FF66'),
            ('3', 'Noise filtering & windowing', '#FFA500'),
            ('4', 'Parameter extraction (Q, w0, T1, T2)', '#00FFFF')
        ]
        
        for i, (num, text, color) in enumerate(steps):
            y_pos = 6.2 - i * 1.1
            rect = FancyBboxPatch((2, y_pos-0.3), 6, 0.8, boxstyle="round,pad=0.2", facecolor=color, alpha=0.2, edgecolor=color, linewidth=2)
            ax2.add_patch(rect)
            ax2.text(3, y_pos, num, color=color, fontsize=14, fontweight='bold', ha='center')
            ax2.text(4.5, y_pos, text, color='#FFFFFF', fontsize=11, ha='left')
    
    # ==================== SCENE 6: NOISE SOURCES (375-450) ====================
    elif scene == 5:
        # Left: 3D noise sources
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('NOISE SOURCES IN MASER', color='#FFD700', fontsize=14, fontweight='bold')
        
        # Different noise sources
        noise_types = [('Thermal', -1.5, 1, 0), ('Quantum', 0, 1, 0), ('Amplifier', 1.5, 1, 0)]
        
        for name, x, y, z in noise_types:
            for i in range(20):
                nx = x + 0.3 * np.random.randn()
                ny = y + 0.3 * np.random.randn()
                nz = z + 0.3 * np.random.randn()
                ax1.scatter(nx, ny, nz, color='#FF3366', s=30, alpha=0.5)
            ax1.text(x, y+0.5, z, name, color='#FFA500', fontsize=10, fontweight='bold', ha='center')
        
        ax1.view_init(elev=25, azim=frame * 0.5)
        
        # Right: Noise comparison
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'NOISE COMPARISON', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        # Noise bar chart
        categories = ['Maser', 'HEMT', 'FET', 'TWT']
        noise_temp = [1, 50, 100, 200]
        
        colors_bar = ['#33FF66', '#FFA500', '#FF3366', '#FF66CC']
        for i, (cat, temp, col) in enumerate(zip(categories, noise_temp, colors_bar)):
            rect = FancyBboxPatch((1.5 + i*1.8, 4), 1.2, temp/200 * 3, boxstyle="round,pad=0.1", facecolor=col, alpha=0.6, edgecolor=col, linewidth=2)
            ax2.add_patch(rect)
            ax2.text(2.1 + i*1.8, 4.2, cat, color='white', fontsize=9, ha='center')
            ax2.text(2.1 + i*1.8, 4.0, f'{temp}K', color='white', fontsize=8, ha='center')
        
        ax2.text(5, 2.5, 'Maser has lowest noise temperature', color='#33FF66', fontsize=12, fontweight='bold', ha='center')
        ax2.text(5, 2.0, 'Approaches quantum limit at cryogenic temperatures', color='#FFFFFF', fontsize=10, ha='center')
    
    # ==================== SCENE 7: PRACTICAL MEASUREMENT (450-525) ====================
    elif scene == 6:
        # Left: 3D measurement setup
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('NOISE MEASUREMENT SETUP', color='#FFD700', fontsize=14, fontweight='bold')
        
        # Components
        ax1.bar3d(-2, -0.5, -0.5, 1.2, 1, 1, color='#33FF66', alpha=0.4, edgecolor='#33FF66')
        ax1.text(-1.4, 0, 0, 'Maser', color='#33FF66', fontsize=8, ha='center')
        
        ax1.bar3d(0, -0.5, -0.5, 1.2, 1, 1, color='#FFA500', alpha=0.4, edgecolor='#FFA500')
        ax1.text(0.6, 0, 0, 'Mixer', color='#FFA500', fontsize=8, ha='center')
        
        ax1.bar3d(2, -0.5, -0.5, 1.2, 1, 1, color='#FF3366', alpha=0.4, edgecolor='#FF3366')
        ax1.text(2.6, 0, 0, 'SA', color='#FF3366', fontsize=8, ha='center')
        
        # Connections
        ax1.plot([-0.8, 0], [0, 0], [0, 0], 'y-', linewidth=2)
        ax1.plot([1.2, 2], [0, 0], [0, 0], 'y-', linewidth=2)
        
        ax1.view_init(elev=25, azim=frame * 0.4)
        
        # Right: Measurement parameters
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'MEASURED PARAMETERS', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        
        params = [
            ('Noise Temperature', 'T_N', '#33FF66'),
            ('Linewidth', 'Dn', '#FF3366'),
            ('Q Factor', 'Q = w0/Dw', '#FFA500'),
            ('Coherence Time', 'T2', '#00FFFF')
        ]
        
        for i, (name, symbol, color) in enumerate(params):
            y_pos = 6.2 - i * 1.1
            rect = FancyBboxPatch((2, y_pos-0.3), 6, 0.8, boxstyle="round,pad=0.2", facecolor=color, alpha=0.2, edgecolor=color, linewidth=2)
            ax2.add_patch(rect)
            ax2.text(3.5, y_pos, name, color='#FFFFFF', fontsize=12, ha='center')
            ax2.text(7, y_pos, symbol, color=color, fontsize=12, fontweight='bold', ha='center')
    
    # ==================== SCENE 8: FINAL SUMMARY (525-600) ====================
    else:
        # Left: 3D summary
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#1a1a3a')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('NOISE & SIGNAL SUMMARY', color='#FFD700', fontsize=14, fontweight='bold')
        
        # Rotating key concepts
        angle = frame * 0.02
        ax1.text(np.cos(angle), np.sin(angle), 0.8, 'T_N', color='#33FF66', fontsize=16, fontweight='bold')
        ax1.text(np.cos(angle+2), np.sin(angle+2), 0.3, 'Dn', color='#FF3366', fontsize=16, fontweight='bold')
        ax1.text(np.cos(angle+4), np.sin(angle+4), -0.2, 'FT', color='#FFA500', fontsize=16, fontweight='bold')
        ax1.text(np.cos(angle+3), np.sin(angle+3), 0.5, 'PSD', color='#00FFFF', fontsize=14, fontweight='bold')
        
        ax1.view_init(elev=30, azim=frame * 0.5)
        
        # Right: Final conclusion
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#1a1a3a')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'SIGNAL PROCESSING SUMMARY', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        
        rect = FancyBboxPatch((1.5, 4), 7, 2.5, boxstyle="round,pad=0.5", facecolor='#00FFFF', alpha=0.15, edgecolor='#00FFFF', linewidth=3)
        ax2.add_patch(rect)
        
        ax2.text(5, 6.0, 'Maser: Ultra-low noise amplifier', color='#33FF66', fontsize=13, fontweight='bold', ha='center')
        ax2.text(5, 5.2, 'FT: Time <-> Frequency domain', color='#FFA500', fontsize=13, fontweight='bold', ha='center')
        ax2.text(5, 4.4, 'PSD: Determines frequency stability', color='#FF3366', fontsize=13, fontweight='bold', ha='center')
        
        ax2.text(5, 2.8, 'Key for PhD Research', color='#FFFFFF', fontsize=14, fontweight='bold', ha='center')
        ax2.text(5, 2.2, 'University of Stuttgart Collaboration', color='#FFD700', fontsize=11, ha='center')
    
    # Save frame
    frame_file = os.path.join(temp_dir, f'frame_{frame:04d}.png')
    plt.savefig(frame_file, facecolor='#0A0A2A', dpi=90)
    frame_files.append(frame_file)
    plt.close(fig)
    
    if frame % 100 == 0:
        print(f"   Frame {frame}/600")

print("")
print("All 600 frames rendered successfully!")

# Create video
print("")
print("="*80)
print("CREATING 60-SECOND 3D VIDEO...")
print("="*80)

output_file = 'signal_processing_noise_maser.mp4'

try:
    writer = imageio.get_writer(output_file, fps=10, format='mp4', mode='I')
    for frame_file in frame_files:
        image = imageio.imread(frame_file)
        writer.append_data(image)
    writer.close()
    
    print("")
    print("VIDEO CREATED: " + output_file)
    print("Duration: 60 seconds | 600 frames | 10 fps")
    
    # Clean up
    for frame_file in frame_files:
        os.remove(frame_file)
    os.rmdir(temp_dir)
    
except Exception as e:
    print(f"Error: {e}")

# Display
try:
    from IPython.display import Video, display
    display(Video(output_file, width=800, embed=True))
    print("")
    print("Video displayed above!")
except:
    print("")
    print(f"Video saved: {output_file}")

print("")
print("="*80)
print("60-SECOND SIGNAL PROCESSING & NOISE ANALYSIS ANIMATION COMPLETE!")
print("="*80)
print("")
print("SCENES COVERED:")
print("1. Noise Temperature - Quantum Limit")
print("2. Power Spectral Density - Schawlow-Townes Linewidth")
print("3. Fourier Transform - FID Signal")
print("4. Lorentzian Lineshape - Frequency Domain")
print("5. Signal Processing Chain")
print("6. Noise Sources Comparison")
print("7. Practical Measurement Setup")
print("8. Final Summary")
print("")
print(f"OUTPUT: {output_file}")

plt.close('all')