def rol(bits, n):
    print(f"ROL: original = {bits}")
    for i in range(1, n + 1):
        msb = bits[0]
        bits = bits[1:] + msb
        print(f"  step {i}: MSB {msb} moved to LSB -> {bits}")
    print(f"  final = {bits}")
    return bits


def rcl(bits, n, carry='0'):
    print(f"RCL: original = {bits}, initial carry = {carry}")
    for i in range(1, n + 1):
        new_carry = bits[0]
        bits = bits[1:] + carry
        print(f"  step {i}: CF {carry}->{new_carry}, register -> {bits}")
        carry = new_carry
    print(f"  final = {bits}, final carry = {carry}")
    return bits, carry


x = "10110110"
r1 = rol(x, 2)
print()
r2, cf = rcl(x, 2, '0')

# verification vs manual results
assert r1 == "11011010"
assert (r2, cf) == ("11011001", '0')
print("\nAll results match manual calculations.")