from functions.get_files_info import get_files_info


def main(): 
    printing_debug("current")
    print(get_files_info("calculator", "."))

    printing_debug("pkg")
    print(get_files_info("calculator", "pkg"))

    printing_debug("/bin")
    print(get_files_info("calculator", "/bin"))

    printing_debug("../")
    print(get_files_info("calculator", "../"))
    
def printing_debug(target: str): 
    print(f"Result for {target} directory:\n")

if __name__ == "__main__":
    main()