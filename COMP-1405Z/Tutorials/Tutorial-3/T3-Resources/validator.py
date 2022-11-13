import mystack

def isvalid(string):
    forward_brackets = ["(", "[", "{"]
    backward_brackets = [")", "]", "}"]

    forward_stack = []

    for char in string:
        if char in forward_brackets:
            mystack.push(forward_stack, char)

        if char in backward_brackets:
            if forward_brackets[backward_brackets.index(char)] != mystack.pop(forward_stack):
                return False

    # Makes sure that there are an even numbers of opening and closing brackets - [(([])) should evaluate to "False"
    return mystack.isempty(forward_stack)
