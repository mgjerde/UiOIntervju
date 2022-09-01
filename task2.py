class Cafeteria:
    '''
    Class made to initiate the cafeteria UI 
    '''
    def __init__(self):
        self.meal_sum = 0
        self.total_sum = 0
        self.menu = (
                {'name': 'Dagens', 'price': 53.90},
                {'name': 'Vegetar', 'price': 52.50},
                {'name': 'Halal', 'price': 59.90}
        )
    def findmenuindex(self,item):
        '''
        Finds the index of `item` if it exists in the menu, else returns `None`

        Parameters
        ----------
            item `string`
                Item to search for in the menu
        
        Returns
        -------
            menuindex 
                `int`: the index of the item if found OR `None` if it can't be found
        '''

        menuindex = 0
        for menuitem in self.menu:
            if menuitem['name'].lower() == item.lower():
                return menuindex
            menuindex += 1
        return None 
        
    def sell(self, meal):
        '''
        Tries to calculate sale of given user input if it exists on the menu

        Parameters
        ----------
            meal `string`: meal to search for in the menu.
        '''
        menuindex = 0
        menuindex = self.findmenuindex(meal)
        if type(menuindex) is int:
            self.meal_sum += self.menu[menuindex]['price']
            self.total_sum += self.menu[menuindex]['price']
            print(f"{meal.capitalize()}, here you go.\n")        
        else:
            print(f"{meal.capitalize()} is not on the menu!\n")
                
    def empty_cash_registry(self):
        '''
        Clears the value of the current cash registry
        '''
        self.meal_sum = 0
        print("Cash registry emptied. Thieves be warned!\n")

    def main(self):
        '''
        Main interface for the user.
        '''
        while True:
            print("What would you like today? (type 'how is business?' to attempt small talk, or 'not hungry' to stop)")
            user_input = input("> ")
            
            if user_input == 'how is business?':
                if self.total_sum == 0:
                    print("Not good so far. No one seems to be hungry today!\n")
                elif self.total_sum > 0 and self.total_sum <= 500:
                    print("Alright. Could have been better\n")
                elif self.total_sum > 500:
                    print("Excellent! Lots of hungry students around today.\n")
            elif user_input == 'not hungry':
                print("Welcome back later!\n")
                break
            else:
                self.sell(user_input)
                if self.meal_sum > 200:
                    self.empty_cash_registry()

if __name__ == '__main__':
    cafeteria = Cafeteria()
    cafeteria.main()
