#   Author: Shaikh Aquib (softgen-aquib@gmail.com, aquib-shaikh@outlook.com)
#   Script to generate JsonPropertyName() fields for each and every field in the C# class


def parse(text: str):
    new_text = ""

    def put_line(line):
        nonlocal new_text
        new_text += line + "\n"

    text_lines = text.split("\n")
    total_spaces = 0 
    spaces = ""

    for line_ptr in range(len(text_lines)):
        line = text_lines[line_ptr]

        if "namespace" in line:
            put_line(line)
            continue

        # Add tag to indicate serializable class
        if "class" in line:
            class_spaces = generate_spaces(count_whitespaces(line)) # only for class field
            put_line(f"{class_spaces}[Serializable]")
            put_line(line)
            continue

        # Don't need to further process curly braces
        if (stripd_line := line.strip()) in ["{", "}", ""] or stripd_line.startswith("//"):
            put_line(line)
            continue

        words = line.strip().split(" ")

        # usually our variable name will be on third position in a line declaration
        var = words[2].strip(";") 
        snakified_var = convert_to_snake(var)

        if total_spaces == 0:
            total_spaces = count_whitespaces(line)
        
        if len(spaces) == 0:
            spaces = generate_spaces(total_spaces)

        put_line(f'{spaces}[JsonPropertyName("{snakified_var}")]')
        put_line(line)

    return new_text

def convert_to_snake(word: str):
    new_word = ""

    for i in range(len(word)):
        if i > 0 and (word[i].isupper() and word[i-1].islower()):
            new_word += "_"
        new_word += word[i].lower()
    return new_word

def count_whitespaces(line):
    count = 0
    for c in line:
        if c == " ": 
            count += 1
        else:
            return count

def generate_spaces(n):
    spaces = ""

    for i in range(n):
        spaces += " "

    return spaces




if __name__ == "__main__":
    text = open("test.cs", "r").read()
    print(parse(text))

