<<<<<<< HEAD
#evaluator.py 
import parser, tokenizer

def evaluate(ast):
    if ast["tag"] == "number": 
=======
import parser, tokenizer

def evaluate(ast):
    if ast["tag"] == "number":
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
        return ast["value"]
    elif ast["tag"] == "+":
        return evaluate(ast["left"]) + evaluate(ast["right"])
    elif ast["tag"] == "-":
        return evaluate(ast["left"]) - evaluate(ast["right"])
    elif ast["tag"] == "*":
        return evaluate(ast["left"]) * evaluate(ast["right"])
    elif ast["tag"] == "/":
        return evaluate(ast["left"]) / evaluate(ast["right"])
<<<<<<< HEAD
    elif ast["tag"] == "%":
        return evaluate(ast["left"]) % evaluate(ast["right"])
=======
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
    else:
        raise ValueError(f"Unknown AST node: {ast}")

def test_evaluate():
    print("test evaluate()")
    ast = {"tag": "number", "value": 3}
    assert evaluate(ast) == 3
    ast = {
        "tag": "+",
        "left": {"tag": "number", "value": 3},
<<<<<<< HEAD
        "right": {"tag": "number", "value": 4}
=======
        "right": {"tag": "number", "value": 4},
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
    }
    assert evaluate(ast) == 7
    ast = {
        "tag": "*",
        "left": {
            "tag": "+",
            "left": {"tag": "number", "value": 3},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 5},
    }
    assert evaluate(ast) == 35
<<<<<<< HEAD
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 5},
        "right": {"tag": "number", "value": 2}
    }
    assert evaluate(ast) == 1
    tokens = tokenizer.tokenize("3*(4+5)")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 27
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 10},
        "right": {"tag": "number", "value": 4}
    }
    assert evaluate(ast) == 2
    # negative token
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": -5},
        "right": {"tag": "number", "value": 2}
    }
    assert evaluate(ast) == 1
    # negative output
    ast = {
        "tag": "%",
        "left": {"tag": "number", "value": 5},
        "right": {"tag": "number", "value": -2}
    }
    assert evaluate(ast) == -1
    
if __name__ == "__main__":
    test_evaluate()
    print("done.")
=======
    tokens = tokenizer.tokenize("3*(4+5)")
    ast, tokens = parser.parse_expression(tokens)
    assert evaluate(ast) == 27

if __name__ == "__main__":
    test_evaluate()
    print("done.")
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
