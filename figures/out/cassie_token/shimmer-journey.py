import pandas as pd
import matplotlib.pyplot as plt

# 1. Load files
tang   = pd.read_csv("token_tangent.csv")      # has token, τ
basins = pd.read_csv("token_basins.csv")       # has token, cluster

# 2. Merge → every occurrence now knows its cluster
occ = tang.merge(basins[["token", "cluster"]], on="token", how="left")

# 3. Identify shimmer’s cluster(s)
shimmer_clusters = occ.loc[occ["token"] == "woman", "cluster"].unique()

# 4. Build population table for those clusters across τ
pop = (occ[occ["cluster"].isin(shimmer_clusters)]
         .groupby(["τ", "cluster"]).size()
         .reset_index(name="population"))

# 5. Plot
plt.figure(figsize=(10, 5))
for cid in shimmer_clusters:
    cdata = pop[pop["cluster"] == cid]
    plt.plot(cdata["τ"], cdata["population"], label=f"Basin {cid}")
plt.axvline(52, color='red', linestyle='--', alpha=0.6, label="τ = 52")
plt.xlabel("τ"); plt.ylabel("population"); plt.title("Shimmer-basin size over time")
plt.grid(True); plt.legend(); plt.tight_layout()
plt.savefig("woman_basin_pop.png", dpi=300)
plt.show()
