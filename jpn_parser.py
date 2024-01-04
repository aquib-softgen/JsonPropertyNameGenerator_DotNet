import sys
import os


def parse(text: str):
    already_serializable = False
    new_text = ""

    def put_line(line):
        nonlocal new_text
        new_text += line + "\n"

    def should_ignore() -> bool:
        ignore_list = [
            "namespace",
            "[Xml",
            "[Tally",
            "[Column",
            "enum",
            "return",
            "=",
            "///",
            "get ",
            "set ",
            "get{",
            "set{",
            "(",
            ")",
        ]
        for _keyword in ignore_list:
            if _keyword in line:
                return True
        return False

    text_lines = text.split("\n")
    total_spaces = 0
    spaces = ""

    for line_ptr in range(len(text_lines)):
        line = text_lines[line_ptr]

        if "[Serializable]" in line:
            put_line(line)
            already_serializable = True
            continue

        if should_ignore() or ("{ get; set; }" not in line and "()" in line):
            put_line(line)
            continue

        # Add tag to indicate serializable class
        if "class" in line:
            class_spaces = generate_spaces(
                count_whitespaces(line)
            )  # only for class field

            if not already_serializable:
                put_line(f"{class_spaces}[Serializable]")

            put_line(line)
            continue

        # Don't need to further process curly braces
        if (stripd_line := line.strip()) in ["{", "}", ""] or stripd_line.startswith(
            "//"
        ):
            put_line(line)
            continue

        words = line.strip().split(" ")

        # skip if other lines like constructor
        if len(words) < 3:
            put_line(line)
            continue

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
        if i > 0 and (word[i].isupper() and word[i - 1].islower()):
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
    if len(sys.argv) > 2 and ("-f" in sys.argv or "--file" in sys.argv):
        file_path = os.path.join(os.getcwd(), sys.argv[2])
        fptr = open(file_path, "r")
        text = fptr.read()

        fptr.close()

        fptr = open(file_path, "w")
        fptr.write(parse(text))

    else:
        text = "".join(line for line in sys.stdin)
        print(parse(text))
