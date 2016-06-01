state_names = ["alabama","california","oklahoma","florida"]
vowels = ["a","e","i","o","u"]
output = [ ]

for state in state_names:
    state_list = list(state.lower())

    for vowel in vowels:
        while True:
            try:
                state_list.remove(vowel)
            except:
                break
    output.append(" ".join(state_list).capitalize())

print(output)
