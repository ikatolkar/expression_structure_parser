#!/usr/bin/env python3
import sys

class ESPApp():
    def __init__(self):
        self.input = None
        self.output = None

    def get_multiline_input(self) -> str:
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            lines.append(line)
        return ' '.join(lines)

    def handle_expr_to_struct(self):
        self.output = self.input

    def handle_struct_to_expr(self):
        self.output = ''

    def interact(self) -> int:
        print("Select a task:\n1. Expression to structure(json string)\n2. Structure(json string) to expression")
        inp = str(input()).strip()
        if inp == "1":
            # handle exp to json
            print("Input expression:")
            self.input = self.get_multiline_input()
            self.handle_expr_to_struct()

        elif inp == "2":
            #TODO: Json to exp not implemented yet
            print("Not implemented yet")
            return -1
            # handle json to exp
            print("Input structure (json string):")
            self.input = self.get_multiline_input()
            self.handle_struct_to_expr()
        else:
            # fail
            print(f'Invalid selection {inp}')
            return -1

        print("Output: ")
        print(self.output)
        return 0
