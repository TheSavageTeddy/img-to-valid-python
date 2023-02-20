import random

class Strategy:
    def __init__(self, target_string, image_array: list):
        self.target_string = target_string
        self.image_array = image_array
        self.character_densities = {
    '0': 80,
    '1': 30,
    '2': 70,
    '3': 70,
    '4': 80,
    '5': 70,
    '6': 80,
    '7': 50,
    '8': 90,
    '9': 80,
    'A': 80,
    'B': 80,
    'C': 70,
    'D': 80,
    'E': 70,
    'F': 60,
    'G': 80,
    'H': 80,
    'I': 30,
    'J': 50,
    'K': 80,
    'L': 60,
    'M': 90,
    'N': 80,
    'O': 80,
    'P': 80,
    'Q': 80,
    'R': 70,
    'S': 70,
    'T': 70,
    'U': 80,
    'V': 80,
    'W': 90,
    'X': 80,
    'Y': 70,
    'Z': 70,
    'a': 70,
    'b': 70,
    'c': 60,
    'd': 70,
    'e': 70,
    'f': 40,
    'g': 70,
    'h': 70,
    'i': 30,
    'j': 30,
    'k': 70,
    'l': 30,
    'm': 90,
    'n': 70,
    'o': 70,
    'p': 70,
    'q': 70,
    'r': 50,
    's': 60,
    't': 50,
    'u': 70,
    'v': 70,
    'w': 90,
    'x': 70,
    'y': 70,
    'z': 60,
}


    #warning: unreadable code
    def inlineFormat2(self):
        code = "print("
        
        # check if should be double or single quotes
        if (self.image_array[0][5:9] + self.image_array[-1][-21:-1]).count(1) > 3:
            format_type = "F"
            quote_type = '"'
        else:
            format_type = "f"
            quote_type = "'"
        
        code += format_type + quote_type * 3

        gen_array = list(self.image_array)
        gen_array[0] = self.image_array[0][10:]
        gen_array[-1] = self.image_array[-1][:-21]

        for i, row in enumerate(gen_array):
            minus = True
            mod = False
            endingind = 8
            for ind, target in enumerate(row):
                match ind:
                    case 0:
                        code += "{"
                    case _:
                        if ind == len(row) - 1:
                            code += "}"
                            continue
                        next_target = row[ind + 1]
                        if target == 1:
                            if next_target == 0 or ind == len(row) - endingind:
                                code += "8"
                                continue
                            code += "%" if mod else "8"
                            mod = not mod
                        else: #target = 0
                            if ind == len(row) - endingind:
                                code += '1'
                                continue
                            code += '-'
                            mod = False
                

            if i == len(gen_array) - 1: break
            code += '\n'
        
        
        code += quote_type * 3
        code += f".replace({quote_type}\\n{quote_type},{quote_type}{quote_type})"
        code += ")"

        when = ["1" for i in range(len(self.target_string))] + ["0" for i in range(len(code.split("\n")) - len(self.target_string))]
        random.shuffle(when)
        target_ind = 0
        code = code.split("\n")
        for i, line in enumerate(code):
            actual_code = line[line.index("{")+1 : line.index("}") - 6]
            replacementcode = line[line.index("{")+1 : line.index("}") - 6]
            result = eval(actual_code)
            if when[i] == "1":
                result -= ord(self.target_string[target_ind])
                target_ind += 1

            sign = "-" if result == abs(result) else "+"
            res_len = len(str(abs(result)))

            if res_len == -1:
                sign += "----"
            elif res_len == 0:
                sign += "+--"
            elif res_len == 1:
                sign += "--"
            elif res_len == 2:
                sign += "+"




            actual_code = f'{actual_code}{sign}{abs(result)}:c'
            code[i] = code[i][:code[i].index("{")+1] + actual_code + code[i][code[i].index("}"):]

        
        return "\n".join(code)
