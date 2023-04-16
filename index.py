import itertools

def hamming_distance(str1, str2):
    """Calculate the Hamming distance between two strings of equal length."""
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length.")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))

def find_k_mismatches(pattern, text, k):
    """Find all k-mismatches of a pattern in a text."""
    kmer_size = len(pattern)
    mismatches = []
    for i in range(len(text) - kmer_size + 1):
        kmer = text[i:i+kmer_size]
        if hamming_distance(pattern, kmer) <= k:
            mismatches.append((kmer, i))
    return mismatches

def find_frequent_k_mismatches(text, k, d):
    """Find all k-mers that occur at least d times with up to k mismatches."""
    kmer_size = k
    all_kmers = set(''.join(kmer) for kmer in itertools.product('ACGT', repeat=kmer_size))
    frequent_kmers = set()
    counts = {kmer: 0 for kmer in all_kmers}
    for i in range(len(text) - kmer_size + 1):
        kmer = text[i:i+kmer_size]
        mismatches = find_k_mismatches(kmer, text, k)
        for mm_kmer, mm_index in mismatches:
            counts[mm_kmer] += 1
    max_count = max(counts.values())
    frequent_kmers = set(kmer for kmer, count in counts.items() if count >= d)
    return frequent_kmers
