#
# Example file for working with conditional statements
#


def main():
   
    # conditional flow uses if, elif, else
    #x, y = 10, 100
    #if ( x < y ):
    #    st = "x is less than y"
    #print(st)

    #x, y = 1000, 100
    #if ( x < y ):
    #    st = "x is less than y"
    #else:
    #    st = "x is greater than y"
    #print(st)

    #x, y = 100, 100
    #if ( x < y ):
    #    st = "x is less than y"
    #elif (x == y):
    #    st = "x is the sae as y"
    #else:
    #    st = "x is greater than y"
    #print(st)

    # conditional statements let you use "a if C else b"
    # this is a consice way of writing the comparison logic in one line.
    #similar to terniary 
    x, y = 1000, 100
    st = "x is less than y" if (x < y) else "x is greater than or equal to y"
    print(st)

if __name__ == "__main__":
    main()
