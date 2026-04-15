"""
================================================================================
   COMPLETE CHAPTER 2 & 3: QUANTUM MECHANICS TO MASER THEORY
   ALL FIGURES + 30-SECOND ANIMATION + Q1 ANSWER
   
   COVERS: Wavefunction | Two-Level | Density Matrix | Boltzmann |
   Einstein A/B | Gain | Lorentzian | Bloch | Rabi | Population Inversion
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
from scipy.integrate import odeint
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("COMPLETE MASER THEORY: ALL FIGURES + 30-SECOND ANIMATION".center(80))
print("="*80)

# ===================================================================
# PART 1: ALL STATIC FIGURES (CHAPTER 2 & 3)
# ===================================================================

print("\n" + "="*80)
print("PART 1: STATIC FIGURES - CHAPTER 2 & 3".center(80))
print("="*80)

# FIGURE 1: Two-Level System + Wavefunction
fig1, axes = plt.subplots(2, 2, figsize=(14, 10))
fig1.patch.set_facecolor('#0A0A2A')
fig1.suptitle('CHAPTER 2: Quantum Mechanics Foundations', fontsize=16, color='cyan', fontweight='bold')

# 1a: Two-Level System
ax = axes[0,0]
ax.set_facecolor('#0A0A2A')
ax.hlines(y=1.5, xmin=0, xmax=3, colors='red', linewidth=4)
ax.hlines(y=-1.5, xmin=0, xmax=3, colors='blue', linewidth=4)
ax.text(3.2, 1.5, '|e⟩ (Excited)', color='red', fontsize=12, fontweight='bold')
ax.text(3.2, -1.5, '|g⟩ (Ground)', color='blue', fontsize=12, fontweight='bold')
ax.annotate('', xy=(2.5, 1.5), xytext=(2.5, -1.5), arrowprops=dict(arrowstyle='<->', color='yellow', lw=2))
ax.text(2.8, 0, 'ℏω₀', color='yellow', fontsize=10)
ax.set_title('Two-Level Quantum System', color='yellow', fontsize=12)
ax.set_xlim(-0.5, 4)
ax.set_ylim(-2.2, 2.2)
ax.axis('off')

# 1b: Wavefunction Probability Cloud
ax = axes[0,1]
ax.set_facecolor('#0A0A2A')
x = np.linspace(-4, 4, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
prob = np.exp(-R**2/2.5) * (1 + 0.4*np.cos(3*R))
ax.contourf(X, Y, prob, levels=20, cmap='hot')
ax.set_title('Wavefunction |ψ(r,t)|²', color='yellow', fontsize=12)
ax.set_xlabel('x', color='white')
ax.set_ylabel('y', color='white')
ax.text(0, -2.8, 'dP = |ψ|² dV', color='cyan', fontsize=10, ha='center')

# 1c: Density Matrix
ax = axes[1,0]
ax.set_facecolor('#0A0A2A')
for i in range(2):
    for j in range(2):
        rect = Rectangle((0.5 + j*1.2, 0.5 + (1-i)*1.2), 1.0, 1.0, fill=False, edgecolor='cyan', lw=2)
        ax.add_patch(rect)
ax.text(1.0, 1.7, 'ρₑₑ', color='red', fontsize=14, ha='center')
ax.text(2.2, 1.7, 'ρₑ₉', color='white', fontsize=14, ha='center')
ax.text(1.0, 0.5, 'ρ₉ₑ', color='white', fontsize=14, ha='center')
ax.text(2.2, 0.5, 'ρ₉₉', color='blue', fontsize=14, ha='center')
ax.text(-0.2, 1.2, 'ρ̂ =', color='white', fontsize=18)
ax.set_title('Density Matrix (Mixed States)', color='yellow', fontsize=12)
ax.text(0, -0.2, 'Tr(ρ̂) = 1,  dρ/dt = -i/ℏ[Ĥ,ρ]', color='orange', fontsize=9, ha='center')
ax.set_xlim(-1, 4)
ax.set_ylim(0, 2.5)
ax.axis('off')

# 1d: Boltzmann Distribution
ax = axes[1,1]
ax.set_facecolor('#0A0A2A')
T = np.linspace(50, 500, 200)
ratio = np.exp(-100/T)
ax.plot(T, ratio, 'g-', linewidth=2.5)
ax.axhline(y=1, color='r', linestyle='--', alpha=0.5)
ax.set_xlabel('Temperature T (K)', color='white')
ax.set_ylabel('Nₑ/N₉', color='white')
ax.set_title('Boltzmann Distribution', color='yellow', fontsize=12)
ax.grid(alpha=0.2)
ax.text(300, 0.3, 'At 300K: Nₑ/N₉ ≈ 0.9995', color='cyan', fontsize=9)

plt.tight_layout()
plt.show()

# FIGURE 2: Einstein A & B Coefficients
fig2, axes = plt.subplots(1, 3, figsize=(15, 5))
fig2.patch.set_facecolor('#0A0A2A')
fig2.suptitle('CHAPTER 3.1: Einstein\'s A and B Coefficients (1917)', fontsize=14, color='cyan', fontweight='bold')

for i, (title, color, arrow_type) in enumerate([
    ('ABSORPTION\nB_ge·u·N_g', 'lime', 'up'),
    ('SPONTANEOUS\nA_eg·N_e', 'orange', 'down'),
    ('STIMULATED\nB_eg·u·N_e', 'magenta', 'double')
]):
    ax = axes[i]
    ax.set_facecolor('#0A0A2A')
    ax.hlines(y=1, xmin=0, xmax=2, colors='blue', linewidth=3)
    ax.hlines(y=-1, xmin=0, xmax=2, colors='red', linewidth=3)
    ax.text(2.2, 1, '|g⟩', color='blue', fontsize=12)
    ax.text(2.2, -1, '|e⟩', color='red', fontsize=12)
    
    if arrow_type == 'up':
        ax.annotate('', xy=(1, 0.6), xytext=(1, -0.6), arrowprops=dict(arrowstyle='->', color=color, lw=2))
    elif arrow_type == 'down':
        ax.annotate('', xy=(1, -0.6), xytext=(1, 0.6), arrowprops=dict(arrowstyle='->', color=color, lw=2))
    else:
        ax.annotate('', xy=(1, -0.6), xytext=(1, 0.6), arrowprops=dict(arrowstyle='->', color=color, lw=2))
        ax.annotate('', xy=(1.7, -0.3), xytext=(0.3, 0.3), arrowprops=dict(arrowstyle='->', color=color, lw=1.5, alpha=0.6))
    
    ax.text(1, -1.5, title, color=color, fontsize=9, ha='center')
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-2, 1.5)
    ax.axis('off')

plt.tight_layout()
plt.show()

# FIGURE 3: Gain, Lorentzian, Bloch Equations
fig3, axes = plt.subplots(2, 2, figsize=(14, 10))
fig3.patch.set_facecolor('#0A0A2A')
fig3.suptitle('CHAPTER 3.2 & 3.3: Gain, Lineshape & Bloch Equations', fontsize=14, color='cyan', fontweight='bold')

# 3a: Lorentzian Lineshape
ax = axes[0,0]
ax.set_facecolor('#0A0A2A')
omega = np.linspace(-3, 3, 500)
gamma = 0.5
L = (gamma/2)/(np.pi * (omega**2 + (gamma/2)**2))
ax.plot(omega, L, 'c-', linewidth=2.5)
ax.fill_between(omega, 0, L, alpha=0.3, color='cyan')
ax.set_xlabel('(ω-ω₀)/γ', color='white')
ax.set_ylabel('L(ω)', color='white')
ax.set_title('Lorentzian Lineshape', color='yellow', fontsize=12)
ax.grid(alpha=0.2)

# 3b: Gain vs Population Difference
ax = axes[0,1]
ax.set_facecolor('#0A0A2A')
delta_N = np.linspace(-1, 1, 100)
gain = np.maximum(0, delta_N)
ax.plot(delta_N, gain, 'r-', linewidth=2.5)
ax.axvline(x=0, color='white', linestyle='--', alpha=0.5)
ax.fill_between(delta_N, 0, gain, where=(delta_N>0), alpha=0.3, color='green')
ax.fill_between(delta_N, 0, gain, where=(delta_N<0), alpha=0.3, color='red')
ax.text(-0.7, 0.3, 'NO GAIN', color='red', fontsize=10, ha='center')
ax.text(0.5, 0.3, 'GAIN', color='green', fontsize=10, ha='center')
ax.set_xlabel('N_e - N_g', color='white')
ax.set_ylabel('Gain g(ω)', color='white')
ax.set_title('Gain Condition: N_e > N_g', color='yellow', fontsize=12)
ax.grid(alpha=0.2)

# 3c: Bloch Vector Visualization
ax = axes[1,0]
ax.set_facecolor('#0A0A2A')
# Draw Bloch sphere
circle = Circle((0, 0), 1, fill=False, edgecolor='cyan', lw=2)
ax.add_patch(circle)
ax.arrow(0, 0, 0.6, 0.6, head_width=0.08, head_length=0.08, fc='red', ec='red')
ax.text(0.7, 0.7, 'M = (u,v,w)', color='red', fontsize=10)
ax.text(0, -1.2, 'u = Re(ρ_ge), v = Im(ρ_ge), w = ρ_ee-ρ_gg', color='white', fontsize=9, ha='center')
ax.set_title('Bloch Vector on Bloch Sphere', color='yellow', fontsize=12)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# 3d: Rabi Oscillation
ax = axes[1,1]
ax.set_facecolor('#0A0A2A')
t_rabi = np.linspace(0, 4*np.pi, 200)
w_rabi = -np.cos(2*t_rabi)
ax.plot(t_rabi, w_rabi, 'r-', linewidth=2.5)
ax.axhline(y=0, color='white', linestyle=':', alpha=0.5)
ax.set_xlabel('Time', color='white')
ax.set_ylabel('Population Inversion w', color='white')
ax.set_title('Rabi Oscillations (Ω_R = 2)', color='yellow', fontsize=12)
ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()

# ===================================================================
# PART 2: 30-SECOND COMPLETE ANIMATION
# ===================================================================

print("\n" + "="*80)
print("PART 2: 30-SECOND COMPLETE ANIMATION".center(80))
print("="*80)

fig_anim = plt.figure(figsize=(16, 9))
fig_anim.patch.set_facecolor('#0A0A2A')
ax_anim = fig_anim.add_subplot(111)
ax_anim.set_facecolor('#0A0A2A')
ax_anim.set_xlim(-6, 6)
ax_anim.set_ylim(-4, 4)
ax_anim.axis('off')

print("Rendering 300 frames for 30-second animation...")
frames_to_save = []

for frame in range(300):
    ax_anim.clear()
    ax_anim.set_facecolor('#0A0A2A')
    ax_anim.set_xlim(-6, 6)
    ax_anim.set_ylim(-4, 4)
    ax_anim.axis('off')
    
    # Energy levels (always present)
    ax_anim.hlines(y=1.5, xmin=-3, xmax=3, colors='red', linewidth=4)
    ax_anim.hlines(y=-1.5, xmin=-3, xmax=3, colors='blue', linewidth=4)
    ax_anim.text(-3.5, 1.5, '|e⟩', color='red', fontsize=16, fontweight='bold')
    ax_anim.text(-3.5, -1.5, '|g⟩', color='blue', fontsize=16, fontweight='bold')
    ax_anim.annotate('', xy=(3.5, 1.5), xytext=(3.5, -1.5), arrowprops=dict(arrowstyle='<->', color='yellow', lw=2))
    ax_anim.text(3.5, 0, 'ℏω₀', color='yellow', fontsize=11, ha='center')
    
    # Scene 1: Two-Level & Wavefunction (0-40)
    if frame < 40:
        ax_anim.text(0, 3.5, 'SCENE 1: Two-Level System & Wavefunction', color='cyan', fontsize=18, ha='center')
        x = np.linspace(-5, 5, 40)
        y = np.linspace(-3, 3, 40)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        prob = np.exp(-R**2/3) * (1 + 0.3*np.cos(3*R))
        ax_anim.contourf(X+1, Y-1, prob, levels=15, cmap='hot', alpha=0.5)
        ax_anim.text(1, -2.8, '|ψ(r,t)|² = Probability Cloud', color='yellow', fontsize=11, ha='center')
    
    # Scene 2: Density Matrix (40-80)
    elif frame < 80:
        ax_anim.text(0, 3.5, 'SCENE 2: Density Matrix ρ̂', color='cyan', fontsize=18, ha='center')
        for i in range(2):
            for j in range(2):
                rect = Rectangle((0 + j*1.2, -0.5 + (1-i)*1.2), 1.0, 1.0, fill=False, edgecolor='cyan', lw=2)
                ax_anim.add_patch(rect)
        ax_anim.text(0.5, 0.6, 'ρₑₑ', color='red', fontsize=14, ha='center')
        ax_anim.text(1.7, 0.6, 'ρₑ₉', color='white', fontsize=14, ha='center')
        ax_anim.text(0.5, -0.6, 'ρ₉ₑ', color='white', fontsize=14, ha='center')
        ax_anim.text(1.7, -0.6, 'ρ₉₉', color='blue', fontsize=14, ha='center')
        ax_anim.text(-1.2, 0.1, 'ρ̂ =', color='white', fontsize=20)
        ax_anim.text(0, -2.5, 'dρ/dt = -i/ℏ [Ĥ, ρ]', color='orange', fontsize=14, ha='center')
    
    # Scene 3: Boltzmann (80-120)
    elif frame < 120:
        ax_anim.text(0, 3.5, 'SCENE 3: Boltzmann Distribution', color='cyan', fontsize=18, ha='center')
        ax_anim.text(0, 2.5, 'Nₑ/N₉ = exp(-ℏω₀/k_BT)', color='green', fontsize=14, ha='center')
        ax_anim.text(0, 2.0, 'At 300K: Nₑ/N₉ ≈ 0.9995', color='yellow', fontsize=13, ha='center')
        bar_g = Rectangle((-3, -1.5), 1.5, 2.8, facecolor='blue', alpha=0.8)
        ax_anim.add_patch(bar_g)
        ax_anim.text(-2.25, -2.3, 'N₉ (MANY)', color='blue', fontsize=11, ha='center')
        bar_e = Rectangle((1.5, -1.5), 1.5, 0.08, facecolor='red', alpha=0.8)
        ax_anim.add_patch(bar_e)
        ax_anim.text(2.25, -2.3, 'Nₑ (FEW)', color='red', fontsize=11, ha='center')
        ax_anim.text(0, -3.2, '❌ NO POPULATION INVERSION → NO MASER', color='red', fontsize=14, ha='center', fontweight='bold')
    
    # Scene 4: Einstein A & B (120-160)
    elif frame < 160:
        ax_anim.text(0, 3.5, 'SCENE 4: Einstein A & B Coefficients', color='cyan', fontsize=18, ha='center')
        ax_anim.annotate('', xy=(-2.5, 0.5), xytext=(-2.5, -0.5), arrowprops=dict(arrowstyle='->', color='lime', lw=2))
        ax_anim.text(-2.5, -1.3, 'Absorption: B_ge·u·N_g', color='lime', fontsize=9, ha='center')
        ax_anim.annotate('', xy=(0, -0.5), xytext=(0, 0.5), arrowprops=dict(arrowstyle='->', color='orange', lw=2))
        ax_anim.text(0, -1.3, 'Spontaneous: A_eg·N_e', color='orange', fontsize=9, ha='center')
        ax_anim.annotate('', xy=(2.5, -0.5), xytext=(2.5, 0.5), arrowprops=dict(arrowstyle='->', color='magenta', lw=2))
        ax_anim.text(2.5, -1.3, 'Stimulated: B_eg·u·N_e', color='magenta', fontsize=9, ha='center')
        ax_anim.text(0, -2.5, 'Einstein: A_eg = (ℏω₀³/π²c³)·B_eg,  B_ge = B_eg', color='yellow', fontsize=10, ha='center')
        ax_anim.text(0, -3.2, 'Stimulated → IDENTICAL photons → COHERENT amplification!', color='magenta', fontsize=11, ha='center')
    
    # Scene 5: Gain & Lorentzian (160-200)
    elif frame < 200:
        ax_anim.text(0, 3.5, 'SCENE 5: Gain & Lorentzian Lineshape', color='cyan', fontsize=18, ha='center')
        x_l = np.linspace(-3, 3, 100)
        y_l = 1/(1 + x_l**2)
        ax_anim.plot(x_l, y_l*1.2, 'c-', linewidth=2.5)
        ax_anim.fill_between(x_l, 0, y_l*1.2, alpha=0.3, color='cyan')
        ax_anim.text(0, 1.5, 'L(ω) = Lorentzian', color='cyan', fontsize=12, ha='center')
        ax_anim.text(0, -1.5, 'g(ω) = (ℏω/c)·B_eg·(N_e-N_g)·L(ω)', color='yellow', fontsize=12, ha='center')
        ax_anim.text(0, -2.2, 'Maser Condition: g(ω) > κ = ω₀/Q', color='red', fontsize=13, ha='center', fontweight='bold')
        ax_anim.plot([1.5, 3.5], [0.5, 0.5], 'g-', linewidth=3)
        ax_anim.plot([1.5, 3.5], [0.3, 0.3], 'r--', linewidth=2)
        ax_anim.text(3.6, 0.48, 'Gain > Loss', color='lime', fontsize=10)
    
    # Scene 6: Bloch Equations & Rabi (200-240)
    elif frame < 240:
        ax_anim.text(0, 3.5, 'SCENE 6: Bloch Equations & Rabi Oscillations', color='cyan', fontsize=18, ha='center')
        t_r = np.linspace(0, 2*np.pi, 100)
        w_r = -np.cos(3*t_r)
        ax_anim.plot(t_r-2, w_r, 'r-', linewidth=2.5)
        ax_anim.axhline(y=0, color='white', linestyle=':', alpha=0.5)
        ax_anim.text(1, 1.0, 'Rabi Oscillations', color='red', fontsize=11)
        ax_anim.text(0, -2.0, 'Bloch Equations:', color='yellow', fontsize=12, ha='center')
        ax_anim.text(0, -2.5, 'du/dt = -Δω·v - u/T₂', color='white', fontsize=10, ha='center')
        ax_anim.text(0, -2.9, 'dv/dt = Δω·u - v/T₂ + Ω_R·w', color='white', fontsize=10, ha='center')
        ax_anim.text(0, -3.3, 'dw/dt = -Ω_R·v - (w-w₀)/T₁', color='white', fontsize=10, ha='center')
        ax_anim.text(0, -3.7, 'Ω_R = γ_e·B₁/2 (Rabi Frequency)', color='cyan', fontsize=10, ha='center')
    
    # Scene 7: Population Inversion (240-270)
    elif frame < 270:
        inv = min(1.0, (frame-240)/30)
        ax_anim.text(0, 3.5, 'SCENE 7: POPULATION INVERSION ACHIEVED!', color='lime', fontsize=18, ha='center')
        bar_g = Rectangle((-3, -1.5), 1.5, 2.5*(1-inv*0.7), facecolor='blue', alpha=0.8)
        ax_anim.add_patch(bar_g)
        ax_anim.text(-2.25, -2.3, 'N₉', color='blue', fontsize=12, ha='center')
        bar_e = Rectangle((1.5, -1.5), 1.5, 0.1 + inv*2.3, facecolor='red', alpha=0.8)
        ax_anim.add_patch(bar_e)
        ax_anim.text(2.25, -2.3, 'Nₑ', color='red', fontsize=12, ha='center')
        ax_anim.annotate('', xy=(0, 0.8), xytext=(-5, -2), arrowprops=dict(arrowstyle='->', color='green', lw=3))
        ax_anim.text(-4, -1.2, '532 nm Pump Laser', color='green', fontsize=10, fontweight='bold')
        ax_anim.text(0, -3.2, f'Inversion: {inv:.0%}', color='yellow', fontsize=12, ha='center')
        if inv > 0.8:
            ax_anim.text(0, -3.7, '✅ N_e > N_g → STIMULATED EMISSION DOMINATES!', color='lime', fontsize=12, ha='center')
    
    # Scene 8: Maser Action (270-300)
    else:
        ax_anim.text(0, 3.2, '✅ MASER ACTION! ✅', color='gold', fontsize=22, ha='center')
        ax_anim.text(-4, 2.0, 'Chapter 2:', color='cyan', fontsize=12, fontweight='bold')
        ax_anim.text(-4, 1.5, '• Wavefunction |ψ|²', color='white', fontsize=10)
        ax_anim.text(-4, 1.1, '• Two-Level |g⟩,|e⟩', color='white', fontsize=10)
        ax_anim.text(-4, 0.7, '• Density Matrix ρ̂', color='white', fontsize=10)
        ax_anim.text(-4, 0.3, '• Boltzmann N_e/N_g', color='white', fontsize=10)
        ax_anim.text(-4, -0.5, 'Chapter 3:', color='cyan', fontsize=12, fontweight='bold')
        ax_anim.text(-4, -1.0, '• Einstein A/B', color='white', fontsize=10)
        ax_anim.text(-4, -1.4, '• Gain g(ω) > κ', color='white', fontsize=10)
        ax_anim.text(-4, -1.8, '• Bloch Equations', color='white', fontsize=10)
        ax_anim.text(-4, -2.2, '• Rabi Frequency Ω_R', color='white', fontsize=10)
        
        ax_anim.text(2, 2.0, 'MASER CONDITION:', color='red', fontsize=13, fontweight='bold')
        ax_anim.text(2, 1.4, 'N_e > N_g', color='lime', fontsize=16, fontweight='bold')
        ax_anim.text(2, 0.8, 'P_pump > 1/T₁', color='lime', fontsize=16, fontweight='bold')
        ax_anim.text(2, 0.2, 'g(ω) > ω₀/Q', color='lime', fontsize=16, fontweight='bold')
        ax_anim.text(2, -0.8, '🎯 RESULT:', color='gold', fontsize=14, fontweight='bold')
        ax_anim.text(2, -1.4, 'COHERENT MASER', color='yellow', fontsize=13, fontweight='bold')
        ax_anim.text(0, -3.2, '🎉 THEORY TO WORKING MASER - COMPLETE! 🎉', color='cyan', fontsize=14, ha='center', fontweight='bold')
    
    fig_anim.canvas.draw()
    frames_to_save.append([fig_anim.canvas.copy_from_bbox(fig_anim.bbox)])

print("✅ 300 frames rendered!")

# ===================================================================
# SAVE VIDEO
# ===================================================================

print("\n" + "="*80)
print("SAVING 30-SECOND VIDEO...".center(80))
print("="*80)

try:
    import imageio
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as tmpdir:
        filenames = []
        for i, frame_data in enumerate(frames_to_save):
            fig_anim.canvas.restore_region(frame_data[0])
            filename = f"{tmpdir}/frame_{i:04d}.png"
            fig_anim.savefig(filename, facecolor='#0A0A2A')
            filenames.append(filename)
            if i % 60 == 0:
                print(f"   Frame {i}/300")
        
        print("   Creating MP4...")
        writer = imageio.get_writer('maser_complete_30sec.mp4', fps=10)
        for filename in filenames:
            writer.append_data(imageio.imread(filename))
        writer.close()
    
    print("\n✅ VIDEO SAVED: maser_complete_30sec.mp4")
    print("   Duration: 30 seconds | 300 frames | 10 fps")
    
    from IPython.display import Video, display
    display(Video('maser_complete_30sec.mp4', width=800, embed=True))
    
except Exception as e:
    print(f"⚠️ Video save error: {e}")

# ===================================================================
# Q1 ANSWER
# ===================================================================

print("\n" + "="*80)
print("Q1: POPULATION INVERSION IN |e⟩ ON A CHIP".center(80))
print("="*80)

print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                            ANSWER TO Q1                                       ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  POPULATION INVERSION (N_e > N_g) ON A CHIP:                                  ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────────┐ ║
║  │ PROBLEM: At 300K, N_e/N_g = exp(-ℏω₀/k_BT) ≈ 0.9995 → NO MASER         │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                               ║
║  ┌─────────────────────────────────────────────────────────────────────────┐ ║
║  │ SOLUTION: Optical Pumping + Condition P_pump > 1/T₁                     │ ║
║  └─────────────────────────────────────────────────────────────────────────┘ ║
║                                                                               ║
║  STEP 1: Use 532nm green laser to excite electrons |g⟩ → |e⟩                ║
║  STEP 2: Pump rate P_pump must exceed relaxation rate 1/T₁                  ║
║  STEP 3: dρ_ee/dt = -ρ_ee/T₁ + P_pump(1 - ρ_ee - ρ_gg)                      ║
║  STEP 4: At steady state: ρ_ee - ρ_gg = (P_pump·T₁ - 1)/(P_pump·T₁ + 1)     ║
║  STEP 5: Condition P_pump·T₁ > 1 gives ρ_ee > ρ_gg → N_e > N_g              ║
║                                                                               ║
║  PRACTICAL IMPLEMENTATION (Diamond NV-center):                               ║
║  • High-purity diamond (¹²C isotopically purified)                          ║
║  • Surface passivation (H/F termination) to reduce T₁ relaxation            ║
║  • High-Q superconducting resonator (niobium/sapphire)                      ║
║                                                                               ║
║  RESULT: P_pump > 1/T₁ → N_e > N_g → g(ω) > κ → MASER OSCILLATES!          ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")

print("\n" + "="*80)
print("COMPLETE! ALL FIGURES + 30-SECOND ANIMATION + Q1 ANSWER".center(80))
print("="*80)
print("\n📁 OUTPUT FILES:")
print("   • 3 static figures (Chapter 2 & 3)")
print("   • maser_complete_30sec.mp4 (30-second animation)")
print("\n✅ COVERS: Wavefunction | Two-Level | Density Matrix | Boltzmann |")
print("   Einstein A/B | Gain | Lorentzian | Bloch | Rabi | Population Inversion")