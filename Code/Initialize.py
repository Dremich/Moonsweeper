def initialize(preprompt, instructions):
    # Open files
    p = open(preprompt)
    i = open(instructions)

    # Read contents and concatenate with newline
    result = p.read().strip() + "\n" + i.read().strip()

    # Close files
    p.close()
    i.close()

    # Return concatenated string
    return result


preprompt = "test.txt"
instructions = "empty.txt"

t = initialize(preprompt, instructions)
print(t)