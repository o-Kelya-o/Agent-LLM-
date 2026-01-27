from functions.get_file_content import get_file_content

def main():
    printing_debug("lorem.txt")
    print(get_file_content("calculator", "lorem.txt"))

    printing_debug("main.py")
    print(get_file_content("calculator", "main.py"))

    printing_debug("pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))

    printing_debug("/bin/cat")
    print(get_file_content("calculator", "/bin/cat"))

    printing_debug("pkg/does_not_exist.py")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

def printing_debug(target: str): 
    print(f"Result for {target} file:\n")


if __name__ == "__main__":
    main()