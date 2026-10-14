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
