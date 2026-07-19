from functions.get_files_content import get_files_content 

def main():
    result = get_files_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    print(get_files_content("calculator", "main.py"))
    print(get_files_content("calculator", "pkg/calculator.py"))
    print(get_files_content("calculator", "/bin/cat"))
    print(get_files_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()
