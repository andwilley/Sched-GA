from typing import List
from app.models.individual import Individual

def hamming(str1: str, str2: str) -> int:
    if len(str1) != len(str2):
        raise ValueError("Cannot calculate hamming distance of strings of different length.")
    count = 0
    for i, char in enumerate(str1):
        if char != str2[i]:
            count += 1
    return count

def pop_avg_hamming_dist(population: List[Individual]) -> float:
    # the performance of this function sucks (n^2), just run it once at the end.
    total_ham = count = 0
    for i, indiv in enumerate(population):
        if i > 0:
            for j in range(0, i):
                total_ham += hamming(indiv.crew_string(), population[j].crew_string())
                count += 1
    return total_ham / count
