#!coding=utf-8
# mvc 框架

# data
quotes = ('A man is not complete until he is married. Then he is finshed.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')


# model
class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found~!'
        return value


# view
class QuoteTerminalView:
    def show(self, quote):
        print('And the quote is : "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see?')


# controller
class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = int(self.view.select_quote())
                valid_input = True
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    # call controller
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
