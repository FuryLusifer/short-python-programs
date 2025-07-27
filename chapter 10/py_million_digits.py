from mpmath import mp

mp.dps = 1_000_000
with open("chapter 10/pi_million_digits.txt", "w") as f:
    f.write(str(mp.pi))