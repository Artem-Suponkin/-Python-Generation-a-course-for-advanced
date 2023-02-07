#Write a program that uses the random module to generate n passwords with a length of m
# characters consisting of lowercase and uppercase English letters and numbers,
# except for those that are easily confused with each other:
#
#"l" (L small);
#"I" (I large);
#"1" (digit);
#"o" and "O" (capital and small letters);
#"0" (digit).
#
#Additional condition: each password must contain at least one digit and at least one letter in uppercase and lowercase.

def generate_password(m):
    import string, random
    s = [i for i in string.ascii_letters + string.digits if i not in ['l', 'I', 'o', 'O', '0', '1']]
    while True:
        password = ['a' for _ in range(m)]
        password[0] = random.choice([i for i in string.digits if i not in '01'])
        password[1] = random.choice([i for i in string.ascii_uppercase if i not in 'IO'])
        password[2] = random.choice([i for i in string.ascii_lowercase if i not in 'lo'])
        password[3:] = random.sample(s, m - 3)
        pas = ''.join(password)
        break
    return pas

def generate_passwords(n, m):
    spisok = []
    for _ in range(n):
        spisok.append(generate_password(m))
    return spisok

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')