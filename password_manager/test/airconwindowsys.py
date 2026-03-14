class Aircon:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False
        self.current_temperature = 18
    def increase_temperature(self):
        if self.current_temperature < 30:
            self.current_temperature += 1
    def decrease_temperature(self):
        if self.current_temperature > 0:
            self.current_temperature -= 1
    def is_turned_on(self):
        return self.is_on
    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            return 'Turned on succesfully'
        return "Already Turned on"
    def turn_off(self):
        if self.is_on:
            self.is_on = False
            return "Turned off successfully"
        return "Already Turned off"

class Window:
    def __init__(self, area):
        self.area = area
        self.is_open = False
    def is_opened(self):
        return self.is_open
    def close_window(self):   
        if self.is_open:
            self.is_open = False
            return "Closed successfully"
        return "Already Closed"
    
    def open_window(self):    
        if not self.is_open:
            self.is_open = True
            return "Opened Successfully"
        return "Already Opened"
    
class System:
    def __init__(self):
        self.ac = Aircon("Samsung")
        self.wd = Window(10)

    def turn_on_ac(self):
        if self.wd.is_opened():
            return "window must be closed first"
        return self.ac.turn_on()
      
    def open_wd(self):
        if self.ac.is_turned_on():
            return "aircon must be closed first"
        return self.wd.open_window()
    def turn_off_ac(self):
        return self.ac.turn_off()
    def close_window(self):
        return self.wd.close_window()
  
class UI:
    def __init__(self):
        self.sys = System()

    def display_option(self):
        print("[1] Turn on AC\n"
              "[2] Open window\n"
              "[3] Turn off AC\n"
              "[4] Close Window\n")
        
    def usr_input(self):       
        valid_option = (1,2,3,4)
        while True:
            usr = input("Choice: ")
            try:
                usr = int(usr)
                if usr not in valid_option:
                    print("Out of range")
                    continue
                return usr
            except ValueError:
                print("Invalid Input")
                continue
    def print_feedback(self, feedback):
         print(feedback)
    
    def start(self):
        self.display_option()
        
        commands = {
                    1: self.sys.turn_on_ac,
                    2: self.sys.open_wd,
                    3: self.sys.turn_off_ac,
                    4: self.sys.close_window,
                } 
        usr = self.usr_input()
        self.print_feedback(commands[usr]())

ui = UI()
while True:
    ui.start()
