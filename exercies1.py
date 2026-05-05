def read_file(path):
    with open(path, "r") as f:
        text=f.read()

    lines=text.splitlines()
    words=text.split()

    return {
        "lines":len(lines),
        "words":len(words)
    }

if __name__ == "__main__":
    result=read_file("medicalreport.txt")
    print(result)