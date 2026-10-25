BITS = 8
MASK = 0xFF

def to_bin(n):
    return format(n & MASK, '08b')

def from_bin(b):
    v = int(b, 2)
    return v - 256 if v & 0x80 else v

def twos_sub(a, b):
    A, B = a & MASK, b & MASK
    negB = (~B + 1) & MASK  # 2's complement of subtrahend
    full = A + negB
    res = full & MASK       # discard carry-out
    carry_out = full >> BITS
    # overflow: operands (A, -B) have same sign but result sign differs
    overflow = ((A ^ res) & (negB ^ res) & 0x80) != 0
    return A, B, negB, res, carry_out, overflow

def run(label, a, b):
    A, B, negB, res, c, ovf = twos_sub(a, b)
    print(f"\n{label}: ({a}) - ({b})")
    print(f" A          = {a:>4} -> {to_bin(a)}")
    print(f" B          = {b:>4} -> {to_bin(b)}")
    print(f" -B (2's)   =      {to_bin(negB)}")
    print(f" A + (-B)   =      {to_bin(A)} + {to_bin(negB)} = {c}|{to_bin(res)} (carry discarded)")
    print(f" Result = {to_bin(res)} (binary) = {from_bin(to_bin(res))} (decimal)")
    print(f" Expected = (a - b) ->", "MATCH" if from_bin(to_bin(res)) == a - b else "MISMATCH")
    print(f" Overflow = {'YES' if ovf else 'NO'}")

run("a", 45, 19)
run("b", -35, -12)  