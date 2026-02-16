<<<<<<< HEAD
#runner.py 
=======
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
import sys

from tokenizer import tokenize
from parser import parse
<<<<<<< HEAD
from evaluator import evaluate 

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("usage: python runner.py <expression>")
        sys.exit(1)
    expression = sys.argv[1]
    #reads in file that ends with .t
=======
from evaluator import evaluate

if __name__ == "__main__":  
    if len(sys.argv) != 2:
        print("Usage: python runner.py <expression>")
        sys.exit(1)
    expression = sys.argv[1]
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
    if expression.endswith(".t"):
        with open(expression, "r") as f:
            expression = f.read().strip()
    tokens = tokenize(expression)
    ast = parse(tokens)
    result = evaluate(ast)
<<<<<<< HEAD
    print(result)
=======
    print(result)
>>>>>>> 3d1af22a86d3ce350ec311a5c62629e5814848ec
