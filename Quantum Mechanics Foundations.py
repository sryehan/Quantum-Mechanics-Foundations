import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle, Circle
from IPython.display import Video, display
import warnings
warnings.filterwarnings('ignore')

# ============================================
# পুরো অ্যানিমেশন একসাথে
# ============================================

fig = plt.figure(figsize=(16, 9), dpi=100)
fig.patch.set_facecolor('#0A0A2A')
ax = None
frames = []

print("🎬 অ্যানিমেশন তৈরি হচ্ছে...")

for frame_num in range(240):
    if ax is None:
        ax = fig.add_subplot(111)
    ax.clear()
    ax.set_facecolor('#0A0A2A')
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.axis('off')
    
    t = frame_num
    alpha = min(1.0, t / 30) if t < 30 else 1.0
    
    # === Level গুলো সবসময় থাকবে ===
    ax.hlines(y=1.5, xmin=-3, xmax=3, colors='red', linewidth=3)
    ax.hlines(y=-1.5, xmin=-3, xmax=3, colors='blue', linewidth=3)
    ax.text(-3.5, 1.5, '|e⟩', color='red', fontsize=20, fontweight='bold')
    ax.text(-3.5, -1.5, '|g⟩', color='blue', fontsize=20, fontweight='bold')
    ax.text(3.5, 0, 'ℏω₀', color='yellow', fontsize=14, ha='center')
    ax.annotate('', xy=(3.5, 1.5), xytext=(3.5, -1.5),
               arrowprops=dict(arrowstyle='<->', color='yellow', lw=2))
    
    # === Scene অনুযায়ী কন্টেন্ট ===
    if frame_num < 30:
        ax.text(0, 3.5, 'Two-Level Quantum System', color='yellow', fontsize=18, ha='center')
        
    elif frame_num < 60:
        x = np.linspace(-4, 4, 40)
        y = np.linspace(-3, 3, 40)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        prob = np.exp(-R**2 / 2) * (1 + 0.3 * np.cos(4 * R))
        ax.contourf(X, Y, prob, levels=20, cmap='hot', alpha=0.5)
        ax.text(0, -3.2, '|ψ(r,t)|²', color='cyan', fontsize=16, ha='center')
        ax.text(0, 3.5, 'Wavefunction', color='yellow', fontsize=18, ha='center')
        
    elif frame_num < 90:
        cells = [['ρₑₑ', 'ρₑ₉'], ['ρ₉ₑ', 'ρ₉₉']]
        for i in range(2):
            for j in range(2):
                x = 3 + j * 0.8
                y = 0 + (1 - i) * 0.8
                rect = Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=False, edgecolor='cyan', lw=2)
                ax.add_patch(rect)
                color = 'red' if cells[i][j]=='ρₑₑ' else 'blue' if cells[i][j]=='ρ₉₉' else 'white'
                ax.text(x, y, cells[i][j], color=color, fontsize=14, ha='center', va='center')
        ax.text(2.2, 0.8, 'ρ̂ =', color='white', fontsize=20)
        ax.text(0, 3.5, 'Density Matrix', color='yellow', fontsize=18, ha='center')
        ax.text(0, -3.2, 'dρ̂/dt = -i/ℏ [Ĥ, ρ̂]', color='orange', fontsize=14, ha='center')
        
    elif frame_num < 120:
        ax.text(0, 2.5, 'Thermal Equilibrium', color='red', fontsize=18, ha='center')
        ax.text(0, 1.8, 'Nₑ/N₉ = exp(-ℏω₀/kT) ≈ 0.9995', color='green', fontsize=14, ha='center')
        bar_gg = Rectangle((-3, -2), 1.5, 3, facecolor='blue', alpha=0.7)
        ax.add_patch(bar_gg)
        ax.text(-2.25, -2.5, 'N₉', color='blue', fontsize=14, ha='center')
        bar_ee = Rectangle((1.5, -2), 1.5, 0.05, facecolor='red', alpha=0.7)
        ax.add_patch(bar_ee)
        ax.text(2.25, -2.5, 'Nₑ', color='red', fontsize=14, ha='center')
        ax.text(0, -3.2, '❌ No maser', color='red', fontsize=16, ha='center')
        
    elif frame_num < 150:
        inv_factor = min(1.0, (frame_num-120)/30)
        ax.text(0, 2.8, '✓ Population Inversion!', color='green', fontsize=20, ha='center')
        bar_gg = Rectangle((-3, -2), 1.5, 3*(1-inv_factor*0.6), facecolor='blue', alpha=0.7)
        ax.add_patch(bar_gg)
        ax.text(-2.25, -2.5, 'N₉', color='blue', fontsize=14, ha='center')
        bar_ee = Rectangle((1.5, -2), 1.5, 0.05+inv_factor*2.5, facecolor='red', alpha=0.7)
        ax.add_patch(bar_ee)
        ax.text(2.25, -2.5, 'Nₑ', color='red', fontsize=14, ha='center')
        ax.text(0, -3.2, '✅ Nₑ > N₉ → MASER READY!', color='yellow', fontsize=14, ha='center')
        
    elif frame_num < 180:
        chip = Rectangle((-5, -3.5), 10, 2.5, facecolor='gray', alpha=0.3, edgecolor='white')
        ax.add_patch(chip)
        ax.text(0, -2.2, 'Chip Substrate', color='gray', fontsize=12, ha='center')
        for x in np.linspace(-3.5, 3.5, 7):
            ax.add_patch(Circle((x, -2.5), 0.08, color='purple'))
        ax.annotate('', xy=(0, -2.5), xytext=(2, 1.5),
                   arrowprops=dict(arrowstyle='->', color='purple', lw=2))
        ax.text(2.5, -0.5, 'T₁ relaxation', color='purple', fontsize=12, rotation=30)
        ax.text(0, 3.5, 'Chip Challenge: Surface Defects', color='yellow', fontsize=16, ha='center')
        
    elif frame_num < 210:
        ax.annotate('', xy=(0, 1.5), xytext=(-5, -3),
                   arrowprops=dict(arrowstyle='->', color='green', lw=3))
        ax.text(-3.5, -1, 'Pump Laser\n532 nm', color='green', fontsize=12, ha='center')
        ax.text(0, -3.2, 'dρₑₑ/dt = -ρₑₑ/T₁ + P_pump(1-ρₑₑ-ρ₉₉)', color='yellow', fontsize=11, ha='center')
        ax.text(0, -3.7, 'Condition: P_pump > 1/T₁', color='red', fontsize=14, ha='center', fontweight='bold')
        ax.text(0, 3.5, 'Solution: Fast Optical Pumping', color='green', fontsize=18, ha='center')
        
    else:
        ax.text(-3, 2.5, '✓ Population Inversion', color='green', fontsize=16, fontweight='bold')
        ax.text(-3, 1.5, '✓ Pump rate > 1/T₁', color='cyan', fontsize=16, fontweight='bold')
        ax.text(-3, 0.5, '✓ ρₑₑ > ρ₉₉', color='red', fontsize=16, fontweight='bold')
        ax.text(-3, -0.5, '✓ Maser Oscillates!', color='yellow', fontsize=16, fontweight='bold')
        
        cells = [['0.6', 'ρₑ₉'], ['ρ₉ₑ', '0.4']]
        for i in range(2):
            for j in range(2):
                x = 2.5 + j * 0.8
                y = 0.5 + (1 - i) * 0.8
                rect = Rectangle((x-0.4, y-0.4), 0.8, 0.8, fill=False, edgecolor='cyan', lw=2)
                ax.add_patch(rect)
                color = 'red' if cells[i][j]=='0.6' else 'blue' if cells[i][j]=='0.4' else 'white'
                ax.text(x, y, cells[i][j], color=color, fontsize=14, ha='center', va='center')
        ax.text(1.7, 1.3, 'ρ̂ =', color='white', fontsize=16)
        ax.text(0, -3.2, '🎯 POPULATION INVERSION ACHIEVED! 🎯', color='yellow', fontsize=16, ha='center', fontweight='bold')
    
    fig.canvas.draw()
    frames.append([fig.canvas.copy_from_bbox(fig.bbox)])

print("✅ অ্যানিমেশন তৈরি সম্পূর্ণ!")