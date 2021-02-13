with open("Input/Letters/starting_letter.txt") as input_text:
    lines = input_text.readlines()

with open("Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

for name in names:
    name = name.strip()
    first_line = lines[0]
    lines[0] = lines[0].replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as output:
        for line in lines:
            output.write(line)
    lines[0] = first_line
