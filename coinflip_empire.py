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
