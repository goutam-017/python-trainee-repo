def remove_duplicate_lines(input_file, output_file):

    seen = set()

    cleaned_lines = []

    with open(input_file, "r", encoding="utf-8") as f:

        lines = f.readlines()

    for line in lines:

        clean_line = line.strip()

        if clean_line not in seen and clean_line != "":

            seen.add(clean_line)

            cleaned_lines.append(clean_line)

    with open(output_file, "w", encoding="utf-8") as f:

        for line in cleaned_lines:

            f.write(line + "\n")


remove_duplicate_lines(
    "messy.txt",
    "cleaned.txt"
)