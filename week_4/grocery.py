def main():
    kid = []
    try:
        while True:
            x = life()
            if x not in kid:
                kid.append(x)
    except KeyboardInterrupt:
        for i in range(3):
            print()
        for i in sorted(kid):
            print(i.upper())
        
def life():
    return input()
    
main()