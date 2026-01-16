def mod_inv(x):
    exp = MOD - 2
    ans = 1
    base = x % MOD

    while exp > 0:
        if exp % 2 == 1:          # check exponent bit
            ans = (ans * base) % MOD
        base = (base * base) % MOD
        exp //= 2

    return ans

#--------------------------------------------------------------------#
#--------- Bit Manipulation version-----------
def mod_inv(x):
    exp = MOD - 2
    ans = 1
    base = x % MOD

    while exp > 0:
        if exp & 1:                 # check lowest bit
            ans = (ans * base) % MOD
        base = (base * base) % MOD
        exp >>= 1                  # right shift (divide by 2)

    return ans
