from functions.run_python_file import run_python_file


def main(): 
    printing_debug("calculator, main.py")
    print(run_python_file("calculator", "main.py"))

    printing_debug("calculator, main.py, [3 + 5]")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    printing_debug("calculator, tests.py")
    print(run_python_file("calculator", "tests.py"))

    printing_debug("calculator, ../main.py")
    print(run_python_file("calculator", "../main.py"))

    printing_debug("calculator, nonexistent.py")
    print(run_python_file("calculator", "nonexistent.py"))

    printing_debug("calculator, lorem.txt")
    print(run_python_file("calculator", "lorem.txt"))
    
def printing_debug(target: str): 
    print(f"Result for {target} directory:\n")


if __name__ == "__main__":
    main()