import random

# String with included palindromes
s = 'k2e2z8p2xjr0rjx2p_ul93lgbzprqqzpdwnwdpzqqrpzexu_kr32yhd_pit8dwnm_ec72ac_01u310t404mfvyb_vajehda_8f4qvszmm_jy6yfy6yj_mmzsvq4f8_adhed2tiev9rv9sbo8e1r_bo864'
#s = prefix + s
# Initial comment

max_len = 1
max_str = s[0:1]
for i in range(0, len(s)):
    for expected_length in range(len(s) - i, max_len, -1):
        str_tmp = s[i: i + expected_length]
        if str_tmp == str_tmp[::-1]:
            max_len = len(str_tmp)
            max_str = str_tmp
            break
print(max_str)
# The longest palindrome is: 'ehda_8f4qvszmm_jy6yfy6yj_mmzsvq4f8_adhe'
