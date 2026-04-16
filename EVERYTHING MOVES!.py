"""
================================================================================
   COMPLETE 30-SECOND ANIMATION: CAVITY QED + NV CENTERS + MASER ACTION
   Chapters 4 & 5: Jaynes-Cummings | Tavis-Cummings | Strong Coupling
   NV Center | Optical Pumping | Population Inversion | Maser Oscillation
   
   AUTO-MOVING ANIMATION - EVERYTHING WILL MOVE!
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("CREATING 30-SECOND ANIMATION - EVERYTHING WILL MOVE!".center(80))
print("="*80)

# Create figure
fig = plt.figure(figsize=(16, 9))
fig.patch.set_facecolor('#0A0A2A')
ax = fig.add_subplot(111)
ax.set_facecolor('#0A0A2A')
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 4)
ax.axis('off')

print("Rendering 300 frames with moving elements...")

import tempfile
import os
import imageio

temp_dir = tempfile.mkdtemp()
frame_files = []

for frame in range(300):
    ax.clear()
    ax.set_facecolor('#0A0A2A')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.axis('off')
    
    # Calculate animation progress
    t = frame / 300
    
    # ===== SCENE 1: Cavity with MOVING Standing Wave (0-40) =====
    if frame < 40:
        ax.text(0, 3.5, 'SCENE 1: Microwave Cavity Resonator', color='cyan', fontsize=18, ha='center', fontweight='bold')
        
        # Draw cavity
        ax.add_patch(Rectangle((-4, -1), 5, 3, fill=False, edgecolor='cyan', lw=3))
        ax.text(-1.5, 1.2, 'Cavity', color='cyan', fontsize=12, ha='center')
        
        # MOVING standing wave
        for x in np.linspace(-3.5, 1.5, 40):
            y = 0.5 + 0.8 * np.sin(x * 4 + frame * 0.3)
            ax.plot(x, y, 'co', markersize=4, alpha=0.8)
            ax.plot(x, -y + 1, 'co', markersize=3, alpha=0.5)
        
        # MOVING photons inside cavity
        photon_x = -3 + (frame % 50) * 0.1
        if photon_x < 1.5:
            ax.add_patch(Circle((photon_x, 0.5), 0.08, color='yellow', alpha=0.8))
        
        ax.text(0, -2.5, 'Quality Factor: Q = ω₀/κ', color='yellow', fontsize=14, ha='center')
        ax.text(0, -3.2, 'Photon Lifetime: τ = Q/ω₀', color='white', fontsize=12, ha='center')
    
    # ===== SCENE 2: Jaynes-Cummings with RABI OSCILLATION (40-80) =====
    elif frame < 80:
        ax.text(0, 3.5, 'SCENE 2: Jaynes-Cummings Model', color='cyan', fontsize=18, ha='center', fontweight='bold')
        
        # MOVING Rabi oscillation
        rabi = np.sin(frame * 0.2)
        
        # Atom with MOVING population
        atom_color = 'red' if rabi > 0 else 'blue'
        ax.add_patch(Circle((-2, 0), 0.5, color=atom_color, alpha=0.8))
        if rabi > 0:
            ax.text(-2, 0, '|e⟩', color='white', fontsize=8, ha='center')
        else:
            ax.text(-2, 0, '|g⟩', color='white', fontsize=8, ha='center')
        
        # Cavity
        ax.add_patch(Rectangle((1, -0.8), 2, 1.6, fill=False, edgecolor='cyan', lw=2))
        ax.text(2, 0, 'Cavity', color='cyan', fontsize=8, ha='center')
        
        # MOVING coupling arrow with pulsing
        pulse = 1 + 0.3 * np.sin(frame * 0.5)
        ax.annotate('', xy=(0.5, 0), xytext=(-1, 0), arrowprops=dict(arrowstyle='<->', color='magenta', lw=2*pulse))
        ax.text(-0.5, 0.5, f'g = {1.0 + np.sin(frame*0.3):.1f}', color='magenta', fontsize=10, ha='center')
        
        # Hamiltonian
        ax.text(0, -2.0, 'Ĥ_JC = ℏω_câ†â + (ℏω₀/2)σ̂_z + ℏg(â†σ̂_- + âσ̂_+)', 
                color='yellow', fontsize=11, ha='center')
        ax.text(0, -2.7, f'Vacuum Rabi Splitting: 2g = {2 * (1 + np.sin(frame*0.3)):.1f}', color='white', fontsize=12, ha='center')
    
    # ===== SCENE 3: Tavis-Cummings with FLYING SPINS (80-120) =====
    elif frame < 120:
        ax.text(0, 3.5, 'SCENE 3: Tavis-Cummings Model - N Spins', color='cyan', fontsize=18, ha='center', fontweight='bold')
        
        # MOVING spins
        for i in range(50):
            x = -4 + (i % 10) * 0.8
            y = -0.5 + (i // 10) * 0.7 + 0.1 * np.sin(frame * 0.1 + i)
            ax.add_patch(Circle((x, y), 0.12, color='red', alpha=0.7))
            ax.text(x, y, '↑', color='white', fontsize=6, ha='center')
        
        # Cavity with PULSING
        pulse = 1 + 0.2 * np.sin(frame * 0.3)
        ax.add_patch(Rectangle((2, -1.2), 2.5, 2.4, fill=False, edgecolor='cyan', lw=2*pulse))
        ax.text(3.25, 0, 'Cavity', color='cyan', fontsize=10, ha='center')
        
        # MOVING coupling
        ax.annotate('', xy=(2, 0), xytext=(1, 0), arrowprops=dict(arrowstyle='<->', color='magenta', lw=2))
        
        ax.text(0, -2.2, 'Ĥ_TC = ℏω_câ†â + Σ(ℏω_i/2)σ̂_z⁽ⁱ⁾ + ℏg_eff(â†Ĵ_- + âĴ_+)', 
                color='yellow', fontsize=10, ha='center')
        ax.text(0, -2.8, f'g_eff = g × √N = {np.sqrt(50):.1f} × g', color='lime', fontsize=16, ha='center', fontweight='bold')
    
    # ===== SCENE 4: Strong Coupling with MOVING BALLS (120-160) =====
    elif frame < 160:
        ax.text(0, 3.5, 'SCENE 4: Strong Coupling Regime', color='cyan', fontsize=18, ha='center', fontweight='bold')
        
        # MOVING regime indicators
        strong_x = -3 + 0.1 * np.sin(frame * 0.1)
        badc_x = 0 + 0.1 * np.cos(frame * 0.12)
        bade_x = 3 + 0.1 * np.sin(frame * 0.15)
        
        ax.add_patch(Rectangle((strong_x-1, 1), 2, 1.5, facecolor='green', alpha=0.3, edgecolor='lime', lw=2))
        ax.text(strong_x, 1.8, 'Strong Coupling', color='lime', fontsize=9, ha='center')
        
        ax.add_patch(Rectangle((badc_x-1, 1), 2, 1.5, facecolor='orange', alpha=0.3, edgecolor='orange', lw=2))
        ax.text(badc_x, 1.8, 'Bad Cavity', color='orange', fontsize=9, ha='center')
        
        ax.add_patch(Rectangle((bade_x-1, 1), 2, 1.5, facecolor='red', alpha=0.3, edgecolor='red', lw=2))
        ax.text(bade_x, 1.8, 'Bad Emitter', color='red', fontsize=9, ha='center')
        
        # MOVING cooperativity value
        C_val = 0.5 + 0.5 * np.sin(frame * 0.05)
        ax.text(0, -1.0, f'Cooperativity: C = g²/κγ = {C_val:.2f}', color='yellow', fontsize=14, ha='center')
        ax.text(0, -1.8, f'Maser Condition: C × N = {C_val * 50:.1f} > 1?', color='lime' if C_val*50 > 1 else 'red', 
                fontsize=16, ha='center', fontweight='bold')
    
    # ===== SCENE 5: NV Center with SPINNING ELECTRONS (160-200) =====
    elif frame < 200:
        ax.text(0, 3.5, 'SCENE 5: NV⁻ Center in Diamond', color='cyan', fontsize=18, ha='center', fontweight='bold')
        
        # MOVING diamond lattice
        for i in range(40):
            x = -4 + (i % 8) * 0.9
            y = -1.5 + (i // 8) * 0.7 + 0.05 * np.sin(frame * 0.2 + i)
            ax.add_patch(Circle((x, y), 0.08, color='gray', alpha=0.5))
        
        # PULSING NV center
        pulse = 1 + 0.2 * np.sin(frame * 0.3)
        ax.add_patch(Circle((-1, 0), 0.4 * pulse, color='red', alpha=0.8))
        ax.text(-1, 0, 'NV⁻', color='white', fontsize=10, ha='center', fontweight='bold')
        
        # MOVING energy levels
        ax.hlines(y=2.2 + 0.05*np.sin(frame*0.2), xmin=2, xmax=4.5, colors='red', lw=2)
        ax.text(4.6, 2.2, '³E', color='red', fontsize=9)
        ax.hlines(y=1.2 + 0.05*np.cos(frame*0.25), xmin=2, xmax=4.5, colors='orange', lw=2)
        ax.text(4.6, 1.2, 'Singlets', color='orange', fontsize=9)
        ax.hlines(y=0 + 0.05*np.sin(frame*0.3), xmin=2, xmax=4.5, colors='blue', lw=2)
        ax.text(4.6, 0, '³A₂', color='blue', fontsize=9)
        
        ax.text(0, -2.5, 'NV⁻ Hamiltonian: Ĥ = hD_gsŜ_z² + g_eμ_BB·Ŝ', color='yellow', fontsize=11, ha='center')
        ax.text(0, -3.2, f'D_gs = 2.87 GHz → MASER FREQUENCY!', color='lime', fontsize=12, ha='center')
    
    # ===== SCENE 6: Optical Pumping with MOVING PHOTONS (200-240) =====
    elif frame < 240:
        ax.text(0, 3.5, 'SCENE 6: Optical Pumping - Population Inversion', color='cyan', fontsize=18, ha='center', fontweight='bold')
        
        # MOVING pump photons
        pump_progress = (frame - 200) / 40
        photon_pos = -5 + pump_progress * 5
        ax.annotate('', xy=(0, 0.5), xytext=(-5, -1), arrowprops=dict(arrowstyle='->', color='green', lw=3))
        ax.add_patch(Circle((photon_pos, -1 + (photon_pos+5)*0.3), 0.12, color='lime', alpha=0.9))
        ax.text(-4.2, -0.8, '532 nm', color='green', fontsize=11, fontweight='bold')
        
        # MOVING population bars
        ax.text(-3, 2.2, 'Before:', color='white', fontsize=10)
        ax.add_patch(Rectangle((-3.5, 1), 0.8, 1.2, facecolor='blue', alpha=0.8))
        ax.text(-3.1, 0.6, 'N_g', color='blue', fontsize=8)
        ax.add_patch(Rectangle((-2.2, 1), 0.8, 0.1, facecolor='red', alpha=0.8))
        
        inv_progress = min(1.0, pump_progress)
        ax.text(2, 2.2, 'After:', color='white', fontsize=10)
        ax.add_patch(Rectangle((1.5, 1), 0.8, 1.2*(1-inv_progress*0.6), facecolor='blue', alpha=0.8))
        ax.add_patch(Rectangle((2.8, 1), 0.8, 0.1 + inv_progress*1.3, facecolor='red', alpha=0.8))
        
        ax.text(0, -1.5, 'ISC: m_s = ±1 → Singlets → m_s = 0', color='orange', fontsize=11, ha='center')
        ax.text(0, -2.2, 'POPULATION INVERSION at 2.87 GHz!', color='lime', fontsize=12, ha='center', fontweight='bold')
    
    # ===== SCENE 7: Maser Action with MOVING WAVES (240-270) =====
    elif frame < 270:
        ax.text(0, 3.5, 'SCENE 7: MASER ACTION!', color='lime', fontsize=22, ha='center', fontweight='bold')
        
        # MOVING stimulated emission photons
        for i in range(10):
            x = -3 + (frame - 240 + i * 3) * 0.15
            if -3 < x < 4:
                size = 0.08 + 0.05 * np.sin(frame * 0.5 + i)
                ax.add_patch(Circle((x, 0 + i*0.1), size, color='magenta', alpha=0.8))
        
        ax.annotate('', xy=(3, 0), xytext=(-4, 0), arrowprops=dict(arrowstyle='->', color='magenta', lw=2))
        
        # MOVING gain curve
        x_g = np.linspace(-2, 2, 50)
        y_g = 1/(1 + x_g**2) * 1.2
        ax.plot(x_g + 0.1*np.sin(frame*0.1), y_g - 1.5, 'c-', lw=2.5)
        ax.axhline(y=-0.3 + 0.05*np.sin(frame*0.2), color='red', linestyle='--', lw=2)
        
        gain_val = 1.2 - 0.3 + 0.1*np.sin(frame*0.1)
        ax.text(2.5, -0.2, f'Gain > Loss: {gain_val:.1f} > 0.3', color='lime', fontsize=10)
        
        ax.text(0, -2.5, 'Maser Condition: g(ω) > κ = ω₀/Q', color='yellow', fontsize=13, ha='center')
        ax.text(0, -3.2, 'MASER OSCILLATES! → Coherent Output!', color='lime', fontsize=12, ha='center', fontweight='bold')
    
    # ===== SCENE 8: Complete System with ALL MOVING (270-300) =====
    else:
        ax.text(0, 3.5, '✅ COMPLETE DIAMOND MASER SYSTEM ✅', color='gold', fontsize=18, ha='center', fontweight='bold')
        
        # MOVING diamond
        ax.add_patch(Rectangle((-5, -0.5), 3, 2, facecolor='cyan', alpha=0.2 + 0.1*np.sin(frame*0.2), edgecolor='cyan', lw=2))
        ax.text(-3.5, 0.5, 'Diamond', color='cyan', fontsize=10, ha='center')
        
        # PULSING cavity
        pulse = 1 + 0.1 * np.sin(frame * 0.3)
        ax.add_patch(Rectangle((-1, -0.8), 2.5, 2.6, facecolor='magenta', alpha=0.1, edgecolor='magenta', lw=2*pulse))
        ax.text(0.25, 0.5, 'Microwave Cavity', color='magenta', fontsize=9, ha='center')
        
        # MOVING pump
        ax.annotate('', xy=(-2, 0.5), xytext=(-5.5, -1), arrowprops=dict(arrowstyle='->', color='green', lw=2))
        pump_photon = -5 + (frame % 30) * 0.12
        ax.add_patch(Circle((pump_photon, -1 + (pump_photon+5)*0.3), 0.08, color='lime', alpha=0.8))
        
        # MOVING output
        output_photon = 1.8 + (frame % 20) * 0.12
        if output_photon < 4:
            ax.add_patch(Circle((output_photon, 0.5), 0.08, color='yellow', alpha=0.8))
        ax.annotate('', xy=(1.8, 0.5), xytext=(4, 0.5), arrowprops=dict(arrowstyle='->', color='yellow', lw=2))
        ax.text(4.2, 0.3, '2.87 GHz', color='yellow', fontsize=8)
        
        # Summary with MOVING text
        ax.text(-4, -2.2 + 0.03*np.sin(frame*0.1), 'Jaynes-Cummings:', color='cyan', fontsize=9)
        ax.text(-4, -2.6, 'Ĥ_JC = ℏω_câ†â + ℏω₀σ̂_z/2 + ℏg(â†σ̂_- + âσ̂_+)', color='white', fontsize=7)
        ax.text(1.5, -2.2 + 0.03*np.cos(frame*0.12), 'g_eff = g√N', color='lime', fontsize=10, fontweight='bold')
        ax.text(-2, -3.3 + 0.02*np.sin(frame*0.15), 'MASER: N_e > N_g | C·N > 1', color='gold', fontsize=10, ha='center', fontweight='bold')
    
    # Save frame
    frame_file = os.path.join(temp_dir, f'frame_{frame:04d}.png')
    fig.savefig(frame_file, facecolor='#0A0A2A', dpi=100)
    frame_files.append(frame_file)
    
    if frame % 50 == 0:
        print(f"   Frame {frame}/300")

print("\n✅ All 300 frames rendered with MOVING elements!")

# ===================================================================
# CREATE VIDEO
# ===================================================================

print("\n" + "="*80)
print("CREATING VIDEO FILE...".center(80))
print("="*80)

output_file = 'auto_moving_maser_animation.mp4'

try:
    writer = imageio.get_writer(output_file, fps=10, format='mp4', mode='I')
    for frame_file in frame_files:
        image = imageio.imread(frame_file)
        writer.append_data(image)
    writer.close()
    
    print(f"\n✅ VIDEO CREATED: {output_file}")
    print(f"   Duration: 30 seconds | 300 frames | 10 fps")
    
    # Clean up
    for frame_file in frame_files:
        os.remove(frame_file)
    os.rmdir(temp_dir)
    
except Exception as e:
    print(f"Error: {e}")

# ===================================================================
# DISPLAY
# ===================================================================

try:
    from IPython.display import Video, display
    display(Video(output_file, width=800, embed=True))
    print("\n🎬 VIDEO DISPLAYED ABOVE - EVERYTHING MOVES!")
except:
    print(f"\n📁 Video saved: {output_file}")

print("\n" + "="*80)
print("✅ 30-SECOND AUTO-MOVING ANIMATION COMPLETE!".center(80))
print("="*80)

plt.close(fig)