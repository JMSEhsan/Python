# Reference: Head First Learn to Code
def hook_fish():
    print('I got a fish!')

def wait():
    print('Waiting ...')

print('Get worm')
print('Put worm on hook')
print('Throw in lure')

while True:
    response = input('Is bobber underwater? ')
    if response == 'yes':
        is_moving = True
        print('I got a bite!')
        hook_fish()
    else:
        wait()