import string
def print_table(table):
    table = []
    for letter in string.ascii_lowercase[:10]:
        table.append(["{0}" + [" 0 "].format(letter)])
    print(table)
    #lines = ["{0}".format(letter)]+[" 0 "] * 10
    #for i in range(10):
    #    print(lines)
print_table("table")
