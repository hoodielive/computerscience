
X_B = {
    ("B", "s1"): ("X", "R", "s2"),
    ("B", "s2"): ("B", "L", "s3"),
    ("X", "s3"): ("B", "R", "s4"),
    ("B", "s4"): ("B", "L", "s1"),
}

def simulate(instructions):
    tape = ["B", "B"]
    head = 0 
    state = "s1" 

    for _ in range(8):
#        print("".join(tape))
        print(state.rjust(4) + "".join(tape))
        print(" " * head + "^")
        key = (tape[head], state) 
        tape_sym, head_dir, new_state = instructions[key]
        tape[head] = tape_sym
        head += 1 if head_dir == "R" else -1
        state = new_state

simulate(X_B)
