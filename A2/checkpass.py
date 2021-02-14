#!/usr/bin/env python3

import sys
import timeit
import random
import string

# sys.argv[1] Make a copy of the original password text file so that the new entries aren't added on to the original.
file = "passwords1.txt"
password_to_check = "ece345LoVe"  # sys.argv[2]
hash_table_size = 500  # Set Hashtable size

# The hashing approach that is being used is chaining.
# The hashing function that is being used is k mod m, where k = key, m = hashtable size
# The default hashtable size is 2000


def hash_file(file, size=2000):
    # Creates a hash table from the inputted file using chaining.
    hash_table = [[] for _ in range(size)]
    for line in open(file, "r"):
        if(line[-1] == '\n'):
            # Read file reads in with a new line chracter, which is being stripped off before hashing.
            hash_key = hash_function(line[:-1], size)
            hash_table[hash_key].append(line[:-1])
        else:
            hash_key = hash_function(line, size)
            hash_table[hash_key].append(line)

    return hash_table


def check_hash_table(hash_table, password, hash_table_size):
    # Checks if a password is already in the hash table
    hash_key = hash_function(password, hash_table_size)
    return (password in hash_table[hash_key])


def check_constraints(hash_table, password, file, hash_table_size):
    # Checks the constraints of the input password to determine if it is valid or not.
    # Constraints: 6-12 alphanumeric characters
    #             Password is not already in password.txt
    #             Reverse of the password is not in password.txt
    # Ensures all the conditions are met
    if((6 <= len(password) <= 12) and password.isalnum() and not check_hash_table(hash_table, password, hash_table_size) and not check_hash_table(hash_table, password[::-1], hash_table_size)):
        print("VALID")
        file = open(file, 'a')
        file.write(password + '\n')  # Adds the new password to the file
    else:
        print("INVALID")

    return hash_table


def hash_function(password, hash_table_size):
    # Takes in a password and returns the hash function applied to the password
    # Simple hash function k mod m
    hash_num = hash(password) % hash_table_size
    return hash_num


def generate_new_password_file(number, entries, random_seed):
    """
    Generate x number of files for n numnber of passwords and
    saves to root directory for part 2
    """
    random.seed(random_seed)
    file_names = []
    file_suffix = 1

    for file in range(number):
        pass_array = []
        while len(pass_array) < entries:
            gen = ''.join(random.choices(string.ascii_letters +
                                         string.digits, k=random.randint(6, 12)))
            if gen not in pass_array:
                pass_array.append(gen)

        with open('password1000_{}.txt'.format(file_suffix), 'w') as output:
            file_names.append('password1000_{}.txt'.format(file_suffix))
            for row in pass_array:
                output.write(row + '\n')

        file_suffix += 1

    return file_names


def hash_file_iterative(file_name, hash_size_list):
    """Create hash table for all hash sizes for a given input file"""

    entries = 1000
    # load_factor list for all hash sizes in hash_size_list
    load_factor = [(1000/i) for i in hash_size_list]

    # Create hash_tables for all hash sizes in hash_size_list
    hash_table_list = []
    for size in hash_size_list:
        hash_table = [[] for _ in range(size)]
        hash_table_list.append(hash_table)

    for m in range(len(hash_size_list)):
        for line in open(file_name, "r"):
            if(line[-1] == '\n'):
                # Read file reads in with a new line chracter, which is being stripped off before hashing.
                hash_key = hash_function(line[:-1], hash_size_list[m])
                hash_table_list[m][hash_key].append(line[:-1])
            else:
                hash_key = hash_function(line, hash_size_list[m])
                hash_table_list[m][hash_key].append(line)

    return hash_table_list, load_factor


def count_collisions(hash_table):
    """ Counts # of collisions given a hash_table."""

    collision_per_hash = []

    for hash_size in hash_table:
        collisions = 0
        for pos in hash_size:
            if len(pos) > 1 and pos:
                collisions += len(pos) - 1
        collision_per_hash.append(collisions)

    return collision_per_hash


def plots(loading_factor, collisions, name):
    """Plots collision factor vs # of collisions for a given file"""

    import matplotlib.pyplot as plt

    plt.plot(loading_factor, collisions, marker='.')
    plt.xlabel('Loading Factor (n/m)')
    plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.ylabel('Number of Collisions')
    plt.title('Loading Factor vs Collisions for "{}"'.format(name))
    plt.grid()
    plt.tight_layout()
    plt.show()


def part2Combine(file_names_list, hash_size_list, file_number):
    """Combines function calls for easier usage in main()"""

    hash_table_list, load_factor_list = hash_file_iterative(
        file_names_list[file_number], hash_size_list)

    collision = count_collisions(hash_table_list)
    plots(load_factor_list, collision, file_names_list[file_number])

    return collision


if __name__ == '__main__':

    # True to execute part 1, false to execute part 2 plotting
    submission = False

    if submission:

        start_time = timeit.default_timer()
        hash_table = hash_file(file, hash_table_size)
        updated_hash_table = check_constraints(
            hash_table, password_to_check, file, hash_table_size)
        stop_time = timeit.default_timer()

        print('Runtime: ', stop_time-start_time)

    else:

        # Creating various hash table sizes
        n = 1000
        stop = 2000000
        j = 1
        i = 1000

        hash_size_list = []
        while i < stop:
            hash_size_list.append(i)
            i = 1000*(2**j)
            j += 1
        print(hash_size_list)

        # Generating 5 files with randomized alphanumeric
        file_names_list = generate_new_password_file(
            number=5, entries=1000, random_seed=999)

        # Generate plots and return collision count for all 5 files
        collision1 = part2Combine(file_names_list, hash_size_list, 0)
        collision2 = part2Combine(file_names_list, hash_size_list, 1)
        collision3 = part2Combine(file_names_list, hash_size_list, 2)
        collision4 = part2Combine(file_names_list, hash_size_list, 3)
        collision5 = part2Combine(file_names_list, hash_size_list, 4)

        print(collision1, '\n', collision2, '\n',
              collision3, '\n', collision4, '\n', collision5)
