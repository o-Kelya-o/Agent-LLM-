from functions.write_file import write_file

def main(): 
    printing_debug("lorem.txt")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    printing_debug("pkg/morelorem.txt")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    printing_debug("/tmp/temp.txt")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


def printing_debug(target: str): 
    print(f"Result for {target} file:\n")


if __name__ == "__main__":
    main()