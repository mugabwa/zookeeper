# write your code here
import re
from collections import deque


class Calculator:
    def __init__(self):
        """The constructor method"""
        self.end = False
        self.user_input = None
        self.other_options = ["/exit", "/help"]
        self.variables_dict = dict()
        self.stack = deque()
        self.regex = r'[()]|[/*^+-]+|[0-9]+|[A-z]+'
        self.help = "Smart calculator: please insert the expressions with the PEP 8 notation"

    # this method convert the expression into a list
    # with the respective signs for each value
    def calculator_eval(self, user_input):
        """Takes a user input, checks if the expression is valid and performs the calculation"""
        numbers = re.findall(self.regex, user_input)
        new_list = []
        if user_input.count('(') != user_input.count(')'):
            print('Invalid expression')
            return
        else:
            for i in numbers:
                minus = i.count('-')
                plus = i.count('+')
                if i.count('*') > 1:
                    print('Invalid expression')
                    return
                if i.count('/') > 1:
                    print('Invalid expression')
                    return
                if i.count('^') > 1:
                    print('Invalid expression')
                    return
                if minus % 2 == 0 and minus > 0:
                    new_list.append(i.replace(minus * '-', '+'))
                elif minus % 2 != 0 and minus > 0:
                    new_list.append(i.replace(minus * '-', '-'))
                elif minus == 0 and plus == 0:
                    new_list.append(i)
                elif plus > 0:
                    new_list.append(i.replace(plus * '+', '+'))
            self._infix2postfix(new_list)
            if self.stack:
                print(self.stack.pop())
            else:
                x = ''.join(new_list)
                if x.isdigit():
                    print(x)
                else:
                    raise ValueError

    def _infix2postfix(self, express):
        """Converts infix expression to postfix format"""
        sign_stack = deque()
        for x in express:
            if x.isdigit():
                self.stack.append(x)
            else:
                self._precedence(x, sign_stack)
        for _x in range(len(list(sign_stack))):
            self._operation(sign_stack.pop())

    def _precedence(self, sign, sign_stack):
        """Checks the order of sign preference and initializes a calculation"""
        if not sign_stack:
            sign_stack.append(sign)
        else:
            ln = len(list(sign_stack))
            for _x in range(ln):
                try:
                    x = sign_stack[-1]
                except IndexError:
                    # print("out of range ", sign_stack)
                    break
                else:
                    if sign == '(':
                        sign_stack.append(sign)
                        break
                    # power
                    elif sign == '^':
                        sign_stack.append(sign)
                        break
                    # Product
                    elif sign == '*':
                        ln1 = len(list(sign_stack))
                        for _y in range(ln1):
                            if x != '^' and x != '/':
                                sign_stack.append(sign)
                                break
                            else:
                                try:
                                    self._operation(sign_stack.pop())
                                    x = sign_stack[-1]
                                except IndexError:
                                    sign_stack.append(sign)
                                    return
                        break
                    elif sign == '/':
                        ln1 = len(list(sign_stack))
                        for _y in range(ln1):
                            if x != '^' and x != '*':
                                sign_stack.append(sign)
                                break
                            else:
                                try:
                                    self._operation(sign_stack.pop())
                                    x = sign_stack[-1]
                                except IndexError:
                                    sign_stack.append(sign)
                                    return
                        break
                    elif sign == '+':
                        ln1 = len(list(sign_stack))
                        for _y in range(ln1):
                            if x != '^' and x != '*' and x != '/' and x != '+' and x != '-':
                                sign_stack.append(sign)
                                break
                            else:
                                try:
                                    self._operation(sign_stack.pop())
                                    x = sign_stack[-1]
                                except IndexError:
                                    sign_stack.append(sign)
                                    return
                        break
                    elif sign == '-':
                        ln1 = len(list(sign_stack))
                        for _y in range(ln1):
                            if x != '^' and x != '*' and x != '/' and x != '+' and x != '-':
                                sign_stack.append(sign)
                                break
                            else:
                                try:
                                    self._operation(sign_stack.pop())
                                    x = sign_stack[-1]
                                except IndexError:
                                    sign_stack.append(sign)
                                    return
                        break
                    elif sign == ')':
                        # ln1 = len(list(sign_stack))
                        for _y in range(len(list(sign_stack))):
                            x = sign_stack[-1]
                            # print("check ", sign_stack)
                            if x == '(':
                                sign_stack.pop()
                                break
                            else:
                                self._operation(sign_stack.pop())
                        break

    def _operation(self, sign):
        """Performs the basic calculation"""
        try:
            xv = int(self.stack.pop())
            yv = int(self.stack.pop())
        except IndexError:
            # print("poor operation")
            pass
        else:
            if sign == "+":
                self.stack.append(xv + yv)
            elif sign == "-":
                self.stack.append(yv - xv)
            elif sign == "/":
                self.stack.append(yv / xv)
            elif sign == "*":
                self.stack.append(yv * xv)
            elif sign == "^":
                self.stack.append(pow(yv, xv))

    def calculator_commands(self):
        """Checks the commands in the user input"""
        if self.user_input == self.other_options[1]:
            print(self.help)

        elif self.user_input == self.other_options[0]:
            self.end = True
            print("Bye!")
        elif self.user_input.startswith('/') and self.user_input not in self.other_options:
            print('Unknown command')

    def update_dict(self):
        """Perform dictionary operations"""
        try:
            key, value = self.user_input.replace(' ', '').split('=')
            if key.isalpha():
                if value not in self.variables_dict.keys() and not value.isalpha():
                    try:
                        self.variables_dict[key] = int(value)
                    except ValueError:
                        print("Invalid assignment")
                elif value not in self.variables_dict.keys() and value.isalpha():
                    print('Unknown variable')
                else:
                    self.variables_dict[key] = self.variables_dict[value]
            else:
                print('Invalid identifier')

        except ValueError:
            print("Invalid assignment")

    def operate_variable(self):
        """Checks for variables in an expression"""
        new_user_input = self.user_input
        for element in re.findall(self.regex, self.user_input):
            if element in self.variables_dict.keys():
                new_user_input = new_user_input.replace(element, str(self.variables_dict[element]))
        return new_user_input

    def calculator_operation(self):
        """High level calculation"""
        if not self.user_input.startswith('/'):
            try:
                user_input = self.operate_variable()
                self.calculator_eval(user_input)
            except (ValueError, SyntaxError, NameError):
                print('Unknown variable')

    def main(self):
        """The main function"""
        while not self.end:
            self.user_input = input()
            if len(self.user_input) > 0:
                if '=' in self.user_input:
                    self.update_dict()
                else:
                    self.calculator_operation()
                    self.calculator_commands()


if __name__ == '__main__':
    Calculator().main()
