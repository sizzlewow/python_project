import time

class utilities:
    def slowtype(text):
        for char in text():
            print(char, end='', flush=True)
            time.sleep(0.05)

class Opening:
    def intro():
        return ('Welcome to your life.'
               '\n'
               '\nYou have hit rock bottom, and are rebuilding from scratch...'
               '\n'
               '\nWhat is your name?'
              )
class Tavern:
    def intro(self):
        return (
                'The smell of yesterday\'s mead reminds'
                '\nyou to get back to work...'
                '\n\"Why am I here,\"you think to yourself, \"I need to find a job,'
                '\n where\'s the job board in this town anyway?'
                )
    
    def stay(self):
        return (
                'I really shouldn\'t...perhaps one drink isn\'t so bad though'
                )
    def leave():
        return (
                'Time to get back on the wagon!'
                )
class JobBoard:
    def intro(self):
        return (
                'You track down the job board, \"...got here too late\",'
                '\nyou grumble; realizing you did this to yourself'
                '\nYou find two jobs posted:'
                )
    def bakery(self):
        return (
                'BAKERY IN SEARCH OF WIZARD...'
                )
    def butcher(self):
        return (
                'BUTCHER NEEDS RAT CATCHER!'
                )



if __name__ == "__main__":
    utilities.slowtype(Opening.intro)
    name = input("what is your")
    utilities.slowtype()    




            # for char in tavern:
            # print(char, end='', flush=True)
            # time.sleep(.05)