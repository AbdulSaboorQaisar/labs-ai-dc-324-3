def main():
    lines = []
    print("Enter lines of text (press Enter on a blank line to terminate):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.lower())
    
    print("\nOutput:")
    for line in lines:
        print(line)

# Run the main function
if __name__ == "__main__":
    main()