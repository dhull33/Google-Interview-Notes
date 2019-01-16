


def slice_my_string():
    """
    Given a string S, of length N that is indexed from 0 to N-1, print its even
    indexed and odd-indexed characters as 2 space separated strings on a single
    line. 0 is considered an even index in this exercise.
    """
    test_cases = int(input('How many strings do you want to slice? '))
    for i in range(test_cases):
        my_string = input('Enter your string: ')
        n = len(my_string)
        # using string indexing where the first number is the inclusive
        # starting point; n+1 is the exclusive ending point; 2 is the steps
        # to take
        print(my_string[0:n+1:2], my_string[1:n+1:2])



def print_number_as_string():
    """
    Read an integer N. Without any string methods, print the following: 1234...N.
    Note that "..." represents the values in between.
    """
    n = int(input("Enter an integer: "))
    i_exponent = len(str(n))
    i = 10**i_exponent
    j = 1
    sum_total = n
    while j < n:
        sum_total = (sum_total + (n-j)*i)
        j += 1
        i_exponent = len(str(sum_total))
        i = 10**i_exponent
    print(sum_total)


def reverse_array_of_numbers():
    """
    Given an array, A, of N integers, print A's elements in reverse order
    as a single line of space separated numbers
    """
    given_array = list(map(int, input("Enter a space separated sequence of "
                                      "numbers: ").rstrip().split()))

    reverse_array = given_array[::-1]
    for num in reverse_array:
        print(num, end=" ")


def friend_phone_book():
    """
    Given n names and phone numbers, assemble a phone book that maps
    friends' names to their respective phone numbers. You will then be given
    an unknown number of names to query your phone book for. For each name
    queried, print the associated entry from your phone book on a new line in
    the form name=phoneNumber; if an entry for name is not found, print Not
    found instead.
    """
    num_entries = int(input("How many entries? "))
    phone_book = {}
    for i in range(0, num_entries):
        entries = input("Input your friends name and phone number: ")
        my_friend = entries.split()
        phone_book[my_friend[0]] = my_friend[1]

    lookup_value = input("Lookup value: ")
    while True:
        phone_number = phone_book.get(lookup_value)
        if phone_number is None:
            print("Not found")
        else:
            print(lookup_value + "=" + phone_number)

        lookup_value = input("Lookup value: ")
        if lookup_value == "":
            return False

def factorial(n):
    """
    Write a factorial function that takes a positive integer N as a
    parameter and prints the result of N!
    """
    if n <= 1:
        return 1
    return n * factorial(n-1)

