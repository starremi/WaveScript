from textx import metamodel_from_file
from interpreter.interpreter import WaveScriptInterpreter
import json

def main():
    # 1. Load the grammar and create a metamodel
    # This points to your .tx file in the grammar folder
    mm = metamodel_from_file('grammar/wavescript.tx')

    # 2. Read your FizzBuzz sample program
    # Assuming the file is in the examples folder
    try:
        with open('examples/fizzbuzz.wave', 'r') as f:
            program_code = f.read()
    except FileNotFoundError:
        print("Error: fizzbuzz.wave not found in examples/ folder.")
        return

    # 3. Parse the code into an AST (Model)
    model = mm.model_from_str(program_code)

    # 4. Initialize and run Jania's Interpreter
    # This handles variables, loops, and event generation
    interpreter = WaveScriptInterpreter()
    events = interpreter.interpret(model)

    # 5. Print the Output
    print("--- Execution Output ---")
    # The print statements inside the interpreter will appear here
    
    print("\n--- Generated Sound Events (JSON) ---")
    # This is the "Shared Contract" for Greta
    print(json.dumps(events, indent=2))

if __name__ == "__main__":
    main()