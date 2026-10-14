import random
import matplotlib.pyplot as plt

FLIPS = 10_000
random.seed()

print("=" * 45)
print("           COINFLIP EMPIRE")
print("=" * 45)

flips = [random.choice(["H", "T"]) for _ in range(FLIPS)]

heads = flips.count("H")
tails = flips.count("T")

head_percent = heads / FLIPS * 100
tail_percent = tails / FLIPS * 100

longest_streak = 0
current_streak = 0
streak_side = None
current_side = None
plt.show()

for flip in flips:
    if flip == current_side:
        current_streak += 1
    else:
        current_side = flip
        current_streak = 1


    if current_streak > longest_streak:
        longest_streak = current_streak
        streak_side = flip


heads_so_far = 0
cumulative_percent = []


for i, flip in enumerate(flips, start=1):
    if flip == "H":
        heads_so_far += 1

    cumulative_percent.append(heads_so_far / i * 100)

print(f"\nTotal flips:       {FLIPS:,}")
print(f"Heads:             {heads:,} ({head_percent:.2f}%)")
print(f"Tails:             {tails:,} ({tail_percent:.2f}%)")
print(f"Expected heads:    50.00%")
print(f"Difference:        {abs(head_percent - 50):.2f} percentage points")
print(f"Longest streak:    {longest_streak} {streak_side}'s")



print("\nFirst 30 flips:")
print(" ".join(flips[:30]))

print("\nGenerating graphs...")

plt.figure(figsize=(7, 5))
plt.bar(["Heads", "Tails"], [heads, tails])
plt.title("Coinflip Empire: Heads vs Tails")
plt.ylabel("Number of flips")
plt.savefig("coinflip_results.png", dpi=150)
plt.show()


plt.figure(figsize=(10, 5))
plt.plot(range(1, FLIPS + 1), cumulative_percent)
plt.axhline(y=50, linestyle="--", label="Expected: 50%")
plt.title("Does Randomness Approach 50/50?")
plt.xlabel("Number of flips")
plt.ylabel("Heads percentage (%)")
plt.legend()
plt.tight_layout()
plt.savefig("coinflip_probability.png", dpi=150)
