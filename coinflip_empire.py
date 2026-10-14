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
