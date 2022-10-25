def check_input(input):
    try:
        val = int(input)
        print('it int')
    except ValueError:
        try:
            val = float(input)
            print('it float')
        except ValueError:
            print('it str')
input1 = input()
check_user_input(input1)