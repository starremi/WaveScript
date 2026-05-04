import math

class WaveScriptInterpreter:
    def __init__(self):
        print("--- WaveScript Interpreter ---")
        self.variables = {}
        self.events = []
        self.current_time = 0.0
        self.tempo = 120
        self.dur_map = {'w': 4, 'h': 2, 'q': 1, 'e': 0.5, 's': 0.25}

    def note_to_freq(self, note):
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        letter = note[:-1]
        octave = int(note[-1])
        n = notes.index(letter) + (octave - 4) * 12
        return 440 * (2 ** (n / 12.0))

    def add_event(self, note, duration_code):
        seconds = self.dur_map[duration_code] * (60 / self.tempo)
        freq = self.note_to_freq(note)
        event = {
            "pitch": note,
            "frequency": round(freq, 2),
            "start": round(self.current_time, 3),
            "duration": round(seconds, 3)
        }
        self.events.append(event)
        self.current_time += seconds

    def eval_expr(self, expr):
        # 1. Unpack lists immediately (handles textX wrapping)
        while isinstance(expr, list):
            if not expr:
                return None
            expr = expr[0]

        # 2. Base cases (Numbers, Variables, Strings)
        if isinstance(expr, (int, float)):
            return expr
        
        if isinstance(expr, str):
            if expr in self.variables:
                return self.variables[expr]
            return expr.strip('"')

        # 3. Handle Binary Objects (e.g., i % 3 == 0)
        if hasattr(expr, 'left'):
            left = self.eval_expr(expr.left)
            
            if hasattr(expr, 'op') and expr.op:
                right = self.eval_expr(expr.right)
                
                # Force numeric evaluation where possible for math ops
                try:
                    l, r = float(left), float(right)
                except (ValueError, TypeError):
                    l, r = left, right

                ops = {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b if b != 0 else 0,
                    '%': lambda a, b: int(a) % int(b) if b != 0 else 0,
                    '==': lambda a, b: a == b,
                    '!=': lambda a, b: a != b,
                    '>': lambda a, b: a > b,
                    '<': lambda a, b: a < b,
                    '>=': lambda a, b: a >= b,
                    '<=': lambda a, b: a <= b,
                }
                return ops[expr.op](l, r)
            return left

        # 4. Final fallback for wrapper objects
        if hasattr(expr, 'value'):
            return self.eval_expr(expr.value)
            
        return expr

    def execute(self, stmt):
        name = stmt.__class__.__name__

        if name == "TempoStatement":
            self.tempo = stmt.value

        elif name == "PrintStatement":
            self.add_event(stmt.note, stmt.duration)
            print(self.eval_expr(stmt.expr))

        elif name == "LetStatement":
            self.add_event(stmt.note, stmt.duration)
            self.variables[stmt.name] = self.eval_expr(stmt.expr)

        elif name == "ForStatement":
            self.add_event(stmt.note, stmt.duration)
            for i in range(stmt.start, stmt.end + 1):
                self.variables[stmt.var] = i
                self.run_block(stmt.block)

        elif name == "IfStatement":
            self.add_event(stmt.note, stmt.duration)
            
            # Evaluate the condition tree to a Boolean
            if bool(self.eval_expr(stmt.condition)):
                self.run_block(stmt.then_block)
                return

            # Handle Else Ifs
            if hasattr(stmt, 'else_if_condition') and stmt.else_if_condition:
                for i in range(len(stmt.else_if_condition)):
                    if self.eval_expr(stmt.else_if_condition[i]):
                        self.add_event(stmt.else_if_note[i], stmt.else_if_dur[i])
                        self.run_block(stmt.else_if_block[i])
                        return

            # Handle Else
            if hasattr(stmt, 'else_block') and stmt.else_block:
                if hasattr(stmt, 'else_note') and stmt.else_note:
                    self.add_event(stmt.else_note, stmt.else_dur)
                self.run_block(stmt.else_block)

        elif name == "EndStatement":
            self.add_event(stmt.note, stmt.duration)

    def interpret(self, model):
        for stmt in model.statements:
            self.execute(stmt)
        return self.events

    def run_block(self, block):
        if not block: 
            return
        if hasattr(block, 'statements'):
            for s in block.statements:
                self.execute(s)
        else:
            self.execute(block)