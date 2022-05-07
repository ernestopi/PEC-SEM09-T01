def seq():
    for num in range(10, 1001, 10):
        if num < 1000:
            print(f'{num}, ', end = '')
        else:
            print(f'{num}.')

def main():
    seq()

if __name__ == '__main__':
    main() 