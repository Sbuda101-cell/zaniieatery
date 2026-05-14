import hashlib
import random
import time
from statistics import mean

# ============================================
# CONFIG
# ============================================
HOUSE_EDGE = 0.03       # 3% house edge
RTP = 1 - HOUSE_EDGE    # 97% RTP
ROUNDS = 100


# ============================================
# PROVABLY FAIR HASH GENERATOR
# ============================================
def generate_hash(server_seed, client_seed, nonce):
    data = f"{server_seed}:{client_seed}:{nonce}"
    return hashlib.sha256(data.encode()).hexdigest()


# ============================================
# CONVERT HASH -> RANDOM FLOAT
# ============================================
def hash_to_float(hash_string):
    # Take first 13 hex chars
    h = hash_string[:13]

    # Convert hex -> int
    number = int(h, 16)

    # Normalize to 0-1 range
    return number / float(0x1FFFFFFFFFFFFF)


# ============================================
# CRASH MULTIPLIER MATH
# ============================================
def generate_crash_point(server_seed, client_seed, nonce):
    h = generate_hash(server_seed, client_seed, nonce)

    r = hash_to_float(h)

    # Prevent division by zero
    if r >= 0.999999:
        r = 0.999998

    # Aviator-style multiplier formula
    multiplier = RTP / (1 - r)

    # Minimum crash point
    if multiplier < 1:
        multiplier = 1.00

    return round(multiplier, 2), h


# ============================================
# SIMULATION
# ============================================
def simulate_game(rounds=100):
    print("=" * 60)
    print("AVIATOR-STYLE CRASH GAME SIMULATION")
    print("=" * 60)

    server_seed = hashlib.sha256(str(time.time()).encode()).hexdigest()
    client_seed = "PLAYER-001"

    multipliers = []

    for nonce in range(rounds):
        crash, h = generate_crash_point(server_seed, client_seed, nonce)

        multipliers.append(crash)

        print(f"Round {nonce+1}")
        print(f"Hash: {h}")
        print(f"Crash Point: {crash}x")
        print("-" * 60)

    return multipliers


# ============================================
# PROBABILITY ANALYSIS
# ============================================
def analyze_results(multipliers):
    print("\n")
    print("=" * 60)
    print("STATISTICS")
    print("=" * 60)

    avg = mean(multipliers)

    over_2x = len([m for m in multipliers if m >= 2])
    over_5x = len([m for m in multipliers if m >= 5])
    over_10x = len([m for m in multipliers if m >= 10])
    over_50x = len([m for m in multipliers if m >= 50])

    total = len(multipliers)

    print(f"Total Rounds: {total}")
    print(f"Average Multiplier: {avg:.2f}x")
    print()

    print(f">= 2x : {over_2x} rounds ({(over_2x/total)*100:.2f}%)")
    print(f">= 5x : {over_5x} rounds ({(over_5x/total)*100:.2f}%)")
    print(f">= 10x: {over_10x} rounds ({(over_10x/total)*100:.2f}%)")
    print(f">= 50x: {over_50x} rounds ({(over_50x/total)*100:.2f}%)")


# ============================================
# SIMPLE PREDICTION MODEL
# ============================================
def classify_signal(multiplier):
    if multiplier < 2:
        return "LOW"
    elif multiplier < 10:
        return "MEDIUM"
    else:
        return "HIGH"


def predictor_demo(multipliers):
    print("\n")
    print("=" * 60)
    print("SIGNAL CLASSIFICATION")
    print("=" * 60)

    for i, m in enumerate(multipliers[:20]):
        signal = classify_signal(m)
        print(f"Round {i+1}: {m}x -> {signal}")


# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    results = simulate_game(ROUNDS)

    analyze_results(results)

    predictor_demo(results)
