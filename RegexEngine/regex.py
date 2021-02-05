def comparing(regex, string):
    if regex == ".":
        regex = string

    if not regex:
        return True
    elif not string:
        return True if not regex else False
    else:
        return True if regex == string else False


def matching(regex, string):
    metachar_lst = ["?", "*", "+"]

    if regex:
        if string:
            if len(regex) > 1 and regex[1] in metachar_lst and regex[0] != '\\':
                return stage_5(regex, string)
            elif regex == "\\\\" and string == "\\":
                return True
            else:
                regex = regex.strip('\\')
                if comparing(regex[0], string[0]):
                    regex = regex[1:]
                    string = string[1:]
                    return matching(regex, string)
                else:
                    return False
        else:
            if regex[0] == "$":
                return True
            else:
                return False
    else:
        return True


def stage_3(regex, string):
    if comparing(regex, string):
        return True
    else:
        if not string:
            return False
        else:
            if matching(regex, string):
                return True
            else:
                string = string[1:]
                return stage_3(regex, string)


def stage_4(regex, string):
    if "^" in regex:
        regex = regex[1:]
        return matching(regex, string)
    elif "$" in regex:
        return stage_3(regex, string)
    else:
        return stage_3(regex, string)


def stage_5(regex, string):
    if regex[1] == "?":
        return what(regex, string)
    elif regex[1] == "*":
        return mult(regex, string)
    elif regex[1] == "+":
        return plus(regex, string)


def what(regex, string):
    if comparing(regex[0], string[0]):
        regex = regex[2:]
        string = string[1:]
        return matching(regex, string)
    else:
        regex = regex[2:]
        return matching(regex, string)


def mult(regex, string):
    if comparing(regex[0], string[0]):
        if len(string) == 1:
            regex = regex[2:]
            return matching(regex, string)
        else:
            string = string[1:]
            return matching(regex, string)
    else:
        regex = regex[2:]
        return matching(regex, string)


def plus(regex, string):
    if comparing(regex[0], string[0]):
        if len(string) == 1:
            regex = regex[2:]
            return matching(regex, string)
        else:
            if comparing(string[0], string[1]):
                string = string[1:]
                return matching(regex, string)
            else:
                regex = regex[2:]
                string = string[1:]
                return matching(regex, string)
    else:
        return False


user_regx, user_inpt = input().split("|")
print(stage_4(user_regx, user_inpt))
