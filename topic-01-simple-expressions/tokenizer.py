# tokenizer.py
# standard library used for working with regular expressions
import re
from pprint import pprint

# p = re.compile("ab*")

# if p.match("abbbbbbb") :
#     print("match")
# else:
#     print("not match")

#patterns is initial list of tuples where each tuple contains (raw, label)
patterns = [
    #(raw string, label of pattern)
    (r"\s+", "whitespace"),
    (r"\d+", "number"),
    (r"\+", "+"),
    (r"\-", "-"),
    (r"\/", "/"),
    (r"\*", "*"),
    (r"\(", "("),
    (r"\)", ")"),
    (r"\%", "%"),
    (r".", "error"),
]

patterns = [(re.compile(p), tag) for p,tag in patterns]

def tokenize(characters):
    "Tokenize a string using the patterns above"
    #list to store the extracteed tokens.
    tokens = []
    # tracks the current position in the input string
    position = 0
    # tracks line and column numbers for error reporting
    line = 1
    column = 1
    # holds the type of the match token
    current_tag = None

    # while loop continues till position is less than the total length of string (len(characters))
    while position < len(characters):
        # for loop iterates over all predefined patterns n their associated tags in patterns list. each pattern is compiled reg expr  
        for pattern, tag in patterns:
            # for current pattern, the match() method finds a match starting at position in the string. returns match object aka characters input str and position(index where the matching starts)
            # if no matches found returns none
            match = pattern.match(characters, position)
            # if match is found (aka match is not None) if block is executed 
            if match:
                # sets currrent_tag to tag associated with matched pattern telling us what type of token is matched (nimber, "+", "whitespace")
                current_tag = tag
                # no need to check for other patterns bc alrdy matches current one. ensures only first matching pattern is selected
                break
        # assert statement ensures that a match was indeed found, if not the program will raise an AssertionError and stop
        assert match is not None
        # match.group(0): extracts the matched substring from the match object. group(0): portion of str that matched the reg expr. value: holds actual substr that matched pattern
        value = match.group(0)

        if current_tag == "error":
            # value: expr/variable whose value u want to include in string. !r: conversion flag that tells Python to use the repr() function to get a formal string representation of the value. This is different from the usual str(), which is a more user-friendly representation.
            raise Exception(f"Unexpected character: {value!r}")

        if tag != "whitespace":
            #new token: type of token, line number where it was found, colume number where token starts
            token = {"tag": current_tag, "line": line, "column": column}
            # if the type is number 
            if current_tag == "number":
                #changes string to int 
                token["value"] = int(value)
                # newly created token is added to the tokens list, which is a list of all the tokens found in the input string.
            tokens.append(token)

        # advance position and update line/column
        # iterates over each character in the matched value aka portion of string that was matched
        for ch in value:
            #if newline
            if ch == "\n":
                #lline number is increased bc we've encountered a new line
                line += 1
                #column number is reset bc next ch will be at the start of new line
                column = 1
            #if not newline
            else:
                #column is incremented to go to next ch in the same line
                column += 1
        # position becomes end of current match which tells us where the next pattern should start from. match.end(): return index of 1st charachter aftere the matched substring, so the position is moved accordingly
        position = match.end()

    # after processing all characters, final token with tag none is addede to marj end of string; helps ensure that last token has the correct line/column info
    tokens.append({"tag": None, "line": line, "column": column})
    return tokens     

def test_digits():
    print("test tokenize digits")
    #tokenzie function returns a list of tokens which is stored in the variable t 
    t = tokenize("123")
    #bc 123 is number, this checks if the first token in the list t has the token number 
    assert t[0]["tag"] == "number"
    # checks that the value of the first token is the integer 123, which is the value of the number in the string "123".
    assert t[0]["value"] == 123
    #checks we've reached end
    assert t[1]["tag"] is None
    t = tokenize("1")
    assert t[0]["tag"] == "number"
    assert t[0]["value"] == 1
    assert t[1]["tag"] is None

def test_operators():
    print("test tokenize operators")
    t = tokenize("+ - * / ( ) %")
    # for tok in t: iterating going thru each item in list t, item expected to be a dictionary with keys like "tag", "line". varibale tok represents each dictionary in the list t one by one.
    # tok["tag"]: For each tok (which is a dictionary), this part accesses the value associated with the key "tag". For example, if tok is {"tag": "+", "line": 1, "column": 1}, then tok["tag"] would return "+".
    # this line creates a new list by going thru each dictionary in t and extracting the "tag" value resulting in a list of all the "tag" values from each token in t.
    tags = [tok["tag"] for tok in t]
    assert tags == ["+", "-", "*", "/", "(", ")", "%", None]

def test_expressions():
    print("test tokenize expressions")
    t = tokenize("1+222*3")
    assert t[0]["tag"] == "number" and t[0]["value"] == 1
    assert t[1]["tag"] == "+"
    assert t[2]["tag"] == "number" and t[2]["value"] == 222
    assert t[3]["tag"] == "*"
    assert t[4]["tag"] == "number" and t[4]["value"] == 3
    assert t[5]["tag"] is None

    t = tokenize("5%2")
    assert t[0]["tag"] == "number" and t[0]["value"] == 5
    assert t[1]["tag"] == "%"
    assert t[2]["tag"] == "number" and t[2]["value"] == 2
    assert t[3]["tag"] is None

def test_whitespace():
    print("test tokenize whitespace")
    t = tokenize("1 +\t2  \n*    3")
    assert t[0]["tag"] == "number" and t[0]["value"] == 1
    assert t[1]["tag"] == "+"
    assert t[2]["tag"] == "number" and t[2]["value"] == 2
    assert t[3]["tag"] == "*"
    assert t[4]["tag"] == "number" and t[4]["value"] == 3
    assert t[5]["tag"] is None

def test_error():
    print("test tokenize error")
    try:
        t = tokenize("1@@@ +\t2  \n*    3")
    except Exception as e:
        assert str(e) == "Unexpected character: '@'"
        return
    assert Exception("Error did not happen.")

if __name__ == "__main__":
    test_digits()
    test_operators()
    test_expressions()
    test_whitespace()
    test_error()
    print("done.")
