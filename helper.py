import time


class utilities():

    def slowPrint(self):
        if self is not None:
            for char in (self):
                print(char, end='', flush=True)
                time.sleep(0.025)
        print("\n")

                    
            
