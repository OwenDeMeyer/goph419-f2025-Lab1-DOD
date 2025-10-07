from src.goph419lab01 import functions
import matplotlib.pyplot as plt
import os 
PI = 3.14159265358979323846
def plot_alpha_vs_launch_angle():
            ve_v0 = 2.0
            tol_alpha = 0.04
        
            alphas = []
            phi_min_deg = []
            phi_max_deg = []
        
            a = 0.0
            while a <= 1.0:
                try:
                    phi_min, phi_max = functions.launch_angle_range(ve_v0, a, tol_alpha)
                except ValueError:
                    a += 0.01
                    continue
        
                alphas.append(a)
                phi_min_deg.append(phi_min * 180 / PI)
                phi_max_deg.append(phi_max * 180 / PI)
                
                a += 0.01
        
            plt.figure(figsize=(7,5))
            plt.plot(alphas, phi_min_deg, label="Minimum launch angle", color="blue")
            plt.plot(alphas, phi_max_deg, label="Maximum launch angle", color="green")
            plt.xlabel("α (Maximum altitude ratio)")
            plt.ylabel("Launch angle")
            plt.title(f"Launch angle range vs α")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            os.makedirs("figures", exist_ok=True)
            plt.savefig("figures/launch_angle_vs_alpha.png", dpi=300)
            plt.show()
       
def plot_velocity_vs_launch_angle():
        a = 0.25
        tol_alpha = 0.04
        ve_v0 = 0.5
        ve_v0s = []
        phi_min_deg = []
        phi_max_deg = []
    
        
        while ve_v0 <= 6.0:
            try:
                phi_min, phi_max = functions.launch_angle_range(ve_v0, a, tol_alpha)
            except ValueError:
                ve_v0 += 0.01
                continue
    
            ve_v0s.append(ve_v0)
            phi_min_deg.append(phi_min * 180 / PI)
            phi_max_deg.append(phi_max * 180 / PI)
            
            ve_v0 += 0.01
    
        plt.figure(figsize=(7,5))
        plt.plot(ve_v0s, phi_min_deg, label="Minimum launch angle", color="blue")
        plt.plot(ve_v0s, phi_max_deg, label="Maximum launch angle", color="green")
        plt.xlabel("Velocity Ratio (Ve/V0)")
        plt.ylabel("Launch angle")
        plt.title(f"Launch angle range vs Velocity Ratio ")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        os.makedirs("figures", exist_ok=True)
        plt.savefig("figures/launch_angle_vs_velocity.png", dpi=300)
        plt.show()


def main():
    plot_alpha_vs_launch_angle()
    plot_velocity_vs_launch_angle()

if __name__ == "__main__":
    main()


