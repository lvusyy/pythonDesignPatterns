#!coding=utf-8

# 原函数
class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'rose', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users:\n\n{}\n'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


# 新的代理函数
class Info:
    '''SensitiveInfo的保护代理'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xabceef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('What is the secret?')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2.add user |==| 3.quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit(0)
        else:
            print('unkonw option: {}'.format(key))


if __name__ == '__main__':
    main()
