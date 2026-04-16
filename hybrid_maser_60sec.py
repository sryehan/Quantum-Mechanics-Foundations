"""
================================================================================
   60-SECOND HYBRID ANIMATION: 3D PARTICLE MOTION + 2D DIAGRAMS
   PENTACENE MASER vs NV DIAMOND
   
   3D: Moving particles, electrons, photons, spins
   2D: Energy levels, Bloch spheres, charts
   LARGER TEXT & CLEAR COLOURS
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("60-SECOND HYBRID ANIMATION: 3D PARTICLES + 2D DIAGRAMS")
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
    
    # SCENE 1: PENTACENE MOLECULE WITH 3D ELECTRONS (0-75)
    if scene == 0:
        # Left: 3D particle motion
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('PENTACENE MOLECULE', color='#FFD700', fontsize=16, fontweight='bold')
        
        colors = ['#FF0000', '#FF6600', '#FFD700', '#00FF00', '#00BFFF']
        for ring in range(5):
            x_center = -2 + ring * 1
            y_center = 0
            z_center = 0.3 * np.sin(frame * 0.05 + ring)
            
            angles = np.linspace(0, 2*np.pi, 7)
            x = x_center + 0.5 * np.cos(angles)
            y = y_center + 0.5 * np.sin(angles)
            z = z_center + np.zeros_like(angles)
            ax1.plot(x, y, z, color=colors[ring], linewidth=3, alpha=0.9)
            
            electron_angle = frame * 0.1 + ring
            ex = x_center + 0.45 * np.cos(electron_angle)
            ey = y_center + 0.45 * np.sin(electron_angle)
            ez = z_center + 0.2
            ax1.scatter(ex, ey, ez, color='#00FFFF', s=100, alpha=0.9)
        
        ax1.text(-1, 2, 2.2, 'C22H14', color='#FFD700', fontsize=16, fontweight='bold')
        ax1.view_init(elev=25, azim=frame * 0.6)
        
        # Right: 2D information
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'PENTACENE PROPERTIES', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        ax2.text(5, 6.5, 'Molecular Formula: C22H14', color='#FFFFFF', fontsize=14, ha='center')
        ax2.text(5, 5.8, '5 Linearly Fused Benzene Rings', color='#FFFFFF', fontsize=14, ha='center')
        ax2.text(5, 5.1, 'Doped in p-terphenyl Crystal (0.1%)', color='#FFFFFF', fontsize=14, ha='center')
        ax2.text(5, 4.4, 'Pump Wavelength: 590 nm (Orange)', color='#00FF00', fontsize=14, ha='center')
        ax2.text(5, 3.7, 'Maser Frequency: 1.45 GHz', color='#FF0000', fontsize=14, ha='center')
        ax2.text(5, 3.0, 'Intersystem Crossing (ISC): S1 -> T1', color='#FFA500', fontsize=14, ha='center')
        
        rect = FancyBboxPatch((2, 0.5), 6, 1.2, boxstyle="round,pad=0.3", facecolor='#FF6600', alpha=0.3, edgecolor='#FF6600', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, 1.1, 'KEY: ISC creates population inversion at 1.45 GHz', color='#FFD700', fontsize=13, fontweight='bold', ha='center')
    
    # SCENE 2: 3D SPIN PARTICLES + 2D BLOCH (75-150)
    elif scene == 1:
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('SPIN PARTICLES IN MOTION', color='#FFD700', fontsize=16, fontweight='bold')
        
        for i in range(20):
            angle = frame * 0.15 + i
            x = -1.5 + 0.5 * np.cos(angle)
            y = 0 + 0.5 * np.sin(angle)
            z = 0.3 * np.sin(angle * 2)
            ax1.scatter(x, y, z, color='#FF0000', s=60, alpha=0.8)
        
        for i in range(20):
            angle = frame * 0.05 + i
            x = 1.5 + 0.4 * np.cos(angle)
            y = 0 + 0.4 * np.sin(angle)
            z = 0.2 * np.sin(angle)
            ax1.scatter(x, y, z, color='#00BFFF', s=70, alpha=0.9)
        
        ax1.text(-1.5, 0, -1.5, 'PENTACENE', color='#FF0000', fontsize=12, fontweight='bold', ha='center')
        ax1.text(-1.5, 0, -1.9, 'T2 ~ 100 ns', color='#FF0000', fontsize=10, ha='center')
        ax1.text(1.5, 0, -1.5, 'DIAMOND', color='#00BFFF', fontsize=12, fontweight='bold', ha='center')
        ax1.text(1.5, 0, -1.9, 'T2 ~ 1 ms', color='#00BFFF', fontsize=10, ha='center')
        ax1.view_init(elev=20, azim=frame * 0.5)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'SPIN COHERENCE COMPARISON', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        
        circle1 = Circle((3, 4.5), 1.2, fill=False, edgecolor='#FF0000', linewidth=3)
        ax2.add_patch(circle1)
        ellipse = plt.matplotlib.patches.Ellipse((3, 4.5), 2.4, 1.2, fill=False, edgecolor='#FF0000', linewidth=2, alpha=0.5)
        ax2.add_patch(ellipse)
        ax2.text(3, 3.0, 'PENTACENE', color='#FF0000', fontsize=12, fontweight='bold', ha='center')
        
        circle2 = Circle((7, 4.5), 1.2, fill=False, edgecolor='#00BFFF', linewidth=3)
        ax2.add_patch(circle2)
        ax2.text(7, 3.0, 'DIAMOND', color='#00BFFF', fontsize=12, fontweight='bold', ha='center')
        
        ax2.text(5, 1.5, 'Diamond has 10,000x longer coherence time', color='#FFFFFF', fontsize=13, ha='center')
    
    # SCENE 3: 3D PHOTON PUMPING + 2D ENERGY (150-225)
    elif scene == 2:
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-4, 4)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('OPTICAL PUMPING (590nm)', color='#FFD700', fontsize=16, fontweight='bold')
        
        pump_progress = (frame % 75) / 75
        for i in range(8):
            photon_x = -3 + (pump_progress + i * 0.1) * 5
            if photon_x < 2:
                ax1.scatter(photon_x, 0.5 * np.sin(photon_x * 2), 0.3 * np.cos(photon_x * 2), 
                           color='#00FF00', s=80, alpha=0.9)
        
        for i in range(10):
            ax1.scatter(2, 0.5 * np.sin(frame * 0.1 + i), 0.3 * np.cos(frame * 0.1 + i), 
                       color='#FFD700', s=60, alpha=0.7)
        
        ax1.text(0, 0, -1.8, '590nm LASER EXCITES ELECTRONS', color='#00FF00', fontsize=12, fontweight='bold', ha='center')
        ax1.view_init(elev=20, azim=frame * 0.6)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'ENERGY LEVEL DIAGRAM', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        
        ax2.hlines(y=6, xmin=2, xmax=8, colors='#FF00FF', linewidth=4)
        ax2.text(8.2, 6, 'S1 (Singlet)', color='#FF00FF', fontsize=13, fontweight='bold')
        ax2.hlines(y=4.5, xmin=2, xmax=8, colors='#FFA500', linewidth=4)
        ax2.text(8.2, 4.5, 'ISC', color='#FFA500', fontsize=13, fontweight='bold')
        ax2.hlines(y=3, xmin=2, xmax=8, colors='#FF0000', linewidth=4)
        ax2.text(8.2, 3, 'T1 (Triplet)', color='#FF0000', fontsize=13, fontweight='bold')
        ax2.hlines(y=1, xmin=2, xmax=8, colors='#0000FF', linewidth=4)
        ax2.text(8.2, 1, 'S0 (Ground)', color='#0000FF', fontsize=13, fontweight='bold')
        
        ax2.annotate('', xy=(3, 5.8), xytext=(3, 1.2), arrowprops=dict(arrowstyle='->', color='#00FF00', lw=3))
        ax2.text(1.5, 3.5, '590nm', color='#00FF00', fontsize=12, fontweight='bold', ha='center')
        ax2.annotate('', xy=(6, 4.3), xytext=(6, 5.8), arrowprops=dict(arrowstyle='->', color='#FFA500', lw=3))
        ax2.text(6.5, 5, 'ISC', color='#FFA500', fontsize=12, fontweight='bold')
        ax2.annotate('', xy=(4, 2.8), xytext=(4, 4.3), arrowprops=dict(arrowstyle='->', color='#FF0000', lw=3))
        ax2.text(2.5, 3.5, '1.45 GHz', color='#FF0000', fontsize=12, fontweight='bold', ha='center')
    
    # SCENE 4: 3D POPULATION BARS (225-300)
    elif scene == 3:
        pump_progress = min(1.0, sub_frame / 50)
        
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-2, 2)
        ax1.set_ylim(-1, 1)
        ax1.set_zlim(0, 3)
        ax1.set_title('POPULATION INVERSION', color='#FFD700', fontsize=16, fontweight='bold')
        
        ax1.bar3d(-0.8, -0.5, 0, 0.6, 0.6, 2.5 * (1 - pump_progress * 0.6), color='#0000FF', alpha=0.8)
        ax1.text(-0.5, 0, 2.8, 'Ng', color='#0000FF', fontsize=12, fontweight='bold')
        ax1.bar3d(0.2, -0.5, 0, 0.6, 0.6, 0.2 + pump_progress * 2.3, color='#FF0000', alpha=0.8)
        ax1.text(0.5, 0, 2.8, 'Ne', color='#FF0000', fontsize=12, fontweight='bold')
        ax1.view_init(elev=30, azim=frame * 0.5)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'POPULATION INVERSION ACHIEVED', color='#00FF00', fontsize=18, fontweight='bold', ha='center')
        
        rect = FancyBboxPatch((2, 4), 6, 2, boxstyle="round,pad=0.5", facecolor='#FF0000', alpha=0.3, edgecolor='#FF0000', linewidth=3)
        ax2.add_patch(rect)
        ax2.text(5, 5.5, f'Ne > Ng', color='#FF0000', fontsize=24, fontweight='bold', ha='center')
        ax2.text(5, 4.8, f'Inversion: {pump_progress:.0%}', color='#FFD700', fontsize=16, fontweight='bold', ha='center')
        ax2.text(5, 3.2, 'Condition: P_pump > 1/T1', color='#FFFFFF', fontsize=14, fontweight='bold', ha='center')
        ax2.text(5, 2.5, 'Stimulated Emission Dominates', color='#FFD700', fontsize=13, ha='center')
    
    # SCENE 5: 3D COMPARISON BARS (300-375)
    elif scene == 4:
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-1, 3)
        ax1.set_ylim(-0.5, 1.5)
        ax1.set_zlim(0, 12)
        ax1.set_title('PERFORMANCE COMPARISON', color='#FFD700', fontsize=16, fontweight='bold')
        
        metrics = ['T1', 'T2', 'Stability', 'CW']
        pentacene_vals = [2, 1, 5, 2]
        diamond_vals = [9, 9, 9, 9]
        
        for i, (p, d) in enumerate(zip(pentacene_vals, diamond_vals)):
            ax1.bar3d(i-0.2, -0.3, 0, 0.3, 0.3, p, color='#FF6600', alpha=0.8)
            ax1.bar3d(i+0.2, 0.3, 0, 0.3, 0.3, d, color='#00BFFF', alpha=0.8)
        
        ax1.set_xticks([0, 1, 2, 3])
        ax1.set_xticklabels(metrics, color='white', fontsize=11)
        ax1.view_init(elev=25, azim=frame * 0.4)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'COMPARISON RESULT', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        
        rect1 = FancyBboxPatch((1, 4.5), 3.5, 2.5, boxstyle="round,pad=0.3", facecolor='#00BFFF', alpha=0.2, edgecolor='#00BFFF', linewidth=3)
        ax2.add_patch(rect1)
        ax2.text(2.75, 6.5, 'DIAMOND', color='#00BFFF', fontsize=16, fontweight='bold', ha='center')
        ax2.text(2.75, 5.8, 'Long T1 (~6ms)', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(2.75, 5.3, 'Long T2 (~1ms)', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(2.75, 4.8, 'CW Operation', color='#FFFFFF', fontsize=12, ha='center')
        
        rect2 = FancyBboxPatch((5.5, 4.5), 3.5, 2.5, boxstyle="round,pad=0.3", facecolor='#FF6600', alpha=0.2, edgecolor='#FF6600', linewidth=3)
        ax2.add_patch(rect2)
        ax2.text(7.25, 6.5, 'PENTACENE', color='#FF6600', fontsize=16, fontweight='bold', ha='center')
        ax2.text(7.25, 5.8, 'Simple 590nm Pump', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(7.25, 5.3, 'Room Temperature', color='#FFFFFF', fontsize=12, ha='center')
        ax2.text(7.25, 4.8, 'Short T2 (~100ns)', color='#FFA500', fontsize=12, ha='center')
        
        ax2.text(5, 2.5, 'Diamond: Better for CW | Pentacene: Simpler System', color='#FFD700', fontsize=13, fontweight='bold', ha='center')
    
    # SCENE 6: 3D THERMAL PARTICLES (375-450)
    elif scene == 5:
        temp = 50 + (sub_frame) * 250 / 75
        
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title(f'THERMAL MOTION AT {temp:.0f}K', color='#FFD700', fontsize=16, fontweight='bold')
        
        speed = temp / 300
        for i in range(30):
            x = 2 * np.sin(frame * 0.1 * speed + i)
            y = 1.5 * np.cos(frame * 0.08 * speed + i)
            z = 1 * np.sin(frame * 0.12 * speed + i)
            ax1.scatter(x, y, z, color='#FF6600', s=30 + temp/10, alpha=0.7)
        
        ax1.text(0, 0, -2, f'Temperature: {temp:.0f}K', color='#FFFFFF', fontsize=12, fontweight='bold', ha='center')
        ax1.view_init(elev=20, azim=frame * 0.5)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'TEMPERATURE DEPENDENCE', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        
        T_plot = np.linspace(10, 300, 100)
        T1_penta = 1e-6 * np.exp(-(T_plot-10)/80) + 0.1e-6
        T1_diamond = 6e-3 * np.exp(-(T_plot-10)/200) + 1e-3
        
        ax2_inset = fig.add_axes([0.55, 0.15, 0.35, 0.3])
        ax2_inset.set_facecolor('#0A0A2A')
        ax2_inset.plot(T_plot, T1_penta*1e6, 'r-', linewidth=3, label='Pentacene T1 (us)')
        ax2_inset.plot(T_plot, T1_diamond*1e3, 'b-', linewidth=3, label='Diamond T1 (ms)')
        ax2_inset.axvline(x=temp, color='#00FF00', linestyle='--', linewidth=2)
        ax2_inset.set_xlabel('Temperature (K)', color='white', fontsize=10)
        ax2_inset.set_ylabel('Relaxation Time', color='white', fontsize=10)
        ax2_inset.legend(fontsize=8)
        ax2_inset.grid(alpha=0.2)
        
        penta_val = 1e-6 * np.exp(-(temp-10)/80) + 0.1e-6
        dia_val = 6e-3 * np.exp(-(temp-10)/200) + 1e-3
        ax2.text(5, 2.5, f'At {temp:.0f}K: Pentacene T1 ~ {penta_val:.2f} us', color='#FF0000', fontsize=11, ha='center')
        ax2.text(5, 2.0, f'At {temp:.0f}K: Diamond T1 ~ {dia_val:.2f} ms', color='#00BFFF', fontsize=11, ha='center')
    
    # SCENE 7: 3D MASER PHOTONS (450-525)
    elif scene == 6:
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-3, 3)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('MASER ACTION! 1.45 GHz', color='#FF0000', fontsize=16, fontweight='bold')
        
        for i in range(15):
            x = -2.5 + (sub_frame + i * 4) * 0.12
            if -2.5 < x < 2.5:
                ax1.scatter(x, 0.5 * np.sin(x * 3), 0.3 * np.cos(x * 3), color='#FF00FF', s=80, alpha=0.9)
        
        ax1.plot([-2.5, 2.5, 2.5, -2.5, -2.5], [-1.5, -1.5, 1.5, 1.5, -1.5], [-1, -1, -1, -1, -1], color='#00FFFF', linewidth=2)
        ax1.plot([-2.5, 2.5, 2.5, -2.5, -2.5], [-1.5, -1.5, 1.5, 1.5, -1.5], [1, 1, 1, 1, 1], color='#00FFFF', linewidth=2)
        
        ax1.text(0, 0, 1.5, 'STIMULATED EMISSION', color='#FF00FF', fontsize=12, fontweight='bold', ha='center')
        ax1.text(0, 0, 1.0, 'Coherent Photons!', color='#00FF00', fontsize=11, fontweight='bold', ha='center')
        ax1.view_init(elev=15, azim=frame * 0.8)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'MASER CONDITION', color='#FF0000', fontsize=18, fontweight='bold', ha='center')
        
        rect = FancyBboxPatch((1, 4), 8, 2.5, boxstyle="round,pad=0.5", facecolor='#FF0000', alpha=0.2, edgecolor='#FF0000', linewidth=3)
        ax2.add_patch(rect)
        
        ax2.text(5, 6, 'g(w) > k = w0/Q', color='#FFD700', fontsize=20, fontweight='bold', ha='center')
        ax2.text(5, 5.2, 'Gain > Cavity Loss', color='#00FF00', fontsize=16, fontweight='bold', ha='center')
        ax2.text(5, 4.5, 'MASER OSCILLATES!', color='#FF0000', fontsize=16, fontweight='bold', ha='center')
        ax2.text(5, 2.5, 'Output Frequency: 1.45 GHz', color='#FFFFFF', fontsize=14, fontweight='bold', ha='center')
        ax2.text(5, 1.8, 'Coherent Microwave Amplification', color='#FFD700', fontsize=13, ha='center')
    
    # SCENE 8: COMPLETE SYSTEM (525-600)
    else:
        ax1 = fig.add_subplot(121, projection='3d')
        ax1.set_facecolor('#0A0A2A')
        ax1.set_xlim(-4, 4)
        ax1.set_ylim(-2, 2)
        ax1.set_zlim(-2, 2)
        ax1.set_title('COMPLETE PENTACENE MASER', color='#FFD700', fontsize=16, fontweight='bold')
        
        ax1.plot([-3.5, -3.5, 2, 2, -3.5], [-1.5, -1.5, -1.5, -1.5, -1.5], [-0.8, -0.8, -0.8, -0.8, -0.8], color='#FF6600', linewidth=2)
        ax1.plot([-3.5, -3.5, 2, 2, -3.5], [-1.5, -1.5, -1.5, -1.5, -1.5], [0.8, 0.8, 0.8, 0.8, 0.8], color='#FF6600', linewidth=2)
        
        for i in range(12):
            px = -2.5 + (i % 4) * 1.2
            py = -1 + (i // 4) * 1.2
            pz = 0
            ax1.scatter(px, py, pz, color='#FF0000', s=80, alpha=0.8)
            ax1.text(px, py, pz+0.2, 'P', color='white', fontsize=8, ha='center')
        
        ax1.plot([-4, -2.5], [0, 0], [-0.5, 0.2], 'g-', linewidth=3)
        ax1.text(-3.5, 0.3, -0.2, '590nm', color='#00FF00', fontsize=10, fontweight='bold')
        ax1.plot([2.5, 4], [0, 0], [0, 0], 'y-', linewidth=3)
        ax1.text(3, 0.3, 0, '1.45 GHz', color='#FFFF00', fontsize=10, fontweight='bold')
        ax1.view_init(elev=20, azim=frame * 0.3)
        
        ax2 = fig.add_subplot(122)
        ax2.set_facecolor('#0A0A2A')
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.axis('off')
        
        ax2.text(5, 7.5, 'PENTACENE MASER SYSTEM', color='#FFD700', fontsize=18, fontweight='bold', ha='center')
        
        steps_text = [
            ('1', '590nm Optical Pumping', '#00FF00'),
            ('2', 'Intersystem Crossing (ISC)', '#FFA500'),
            ('3', 'Population Inversion (Ne > Ng)', '#FF0000'),
            ('4', 'Stimulated Emission at 1.45 GHz', '#FF00FF'),
            ('5', 'Coherent Maser Output!', '#FFFF00')
        ]
        
        for i, (num, text, color) in enumerate(steps_text):
            y_pos = 6.5 - i * 0.8
            ax2.text(3, y_pos, num, color=color, fontsize=16, fontweight='bold', ha='center')
            ax2.text(4.5, y_pos, text, color='#FFFFFF', fontsize=13, ha='left')
        
        rect = FancyBboxPatch((2, 0.8), 6, 1.2, boxstyle="round,pad=0.3", facecolor='#FFD700', alpha=0.2, edgecolor='#FFD700', linewidth=2)
        ax2.add_patch(rect)
        ax2.text(5, 1.5, 'PhD Research: University of Stuttgart', color='#FFD700', fontsize=12, fontweight='bold', ha='center')
        ax2.text(5, 1.0, 'Microwave Resonator Design', color='#FFFFFF', fontsize=10, ha='center')
    
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
print("CREATING 60-SECOND VIDEO...")
print("="*80)

output_file = 'hybrid_maser_60sec.mp4'

try:
    writer = imageio.get_writer(output_file, fps=10, format='mp4', mode='I')
    for frame_file in frame_files:
        image = imageio.imread(frame_file)
        writer.append_data(image)
    writer.close()
    
    print("")
    print(f"VIDEO CREATED: {output_file}")
    print(f"Duration: 60 seconds | 600 frames | 10 fps")
    
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
print("60-SECOND HYBRID ANIMATION COMPLETE!")
print("="*80)
print("""
SCENES COVERED:
1. Pentacene Structure + 3D Electrons
2. Spin Particles + Bloch Sphere Comparison  
3. Optical Pumping + Energy Level Diagram
4. Population Inversion + 3D Bars
5. Performance Comparison Bars
6. Thermal Motion + Temperature Graph
7. Maser Action + Cavity Photons
8. Complete Pentacene Maser System
""")
print(f"OUTPUT: {output_file}")
plt.close('all')