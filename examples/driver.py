def main():
    ve_v0 = 2.0
    tol_alpha = 0.04

    alphas = []
    phi_min_deg = []
    phi_max_deg = []

    a = 0.0
    while a <= 1.0:
        try:
            phi_min, phi_max = launch_angle_range(ve_v0, a, tol_alpha)
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

if __name__ == "__main__":
    main()
