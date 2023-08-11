from path import Path

def my_program():
    folder = Path("OutputFolder")
    folder.mkdir_p()
    path_arq = folder / "OutputFile.txt"

    with path_arq.open("w") as arq:
        arq.write("Hello World, this is program in Python!")
    with path_arq.open("r") as arq:
        content = arq.read()
        print("File's content:")
        print(content)

if __name__ == '__main__':
    try:
        my_program()
    except Exception as e:
        print(e)