import sys
def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i % 3 == 0:
            print('fizz', end = ' ')
        if i % 5 == 0:
            print('buzz', end = ' ')
        if i % 3 and i % 5:
            print(i)

def main():
    num = int(sys.argv[1])
    fizz_buzz(num)

if __name__ == '__main__':
    main()
