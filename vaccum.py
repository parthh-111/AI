class TableDrivenVacuumAgent:
    def __init__(self):
        self.percept_history = []

        self.table = {
        
            (('A', 'Clean'),): 'Right',
            (('A', 'Dirty'),): 'Suck',
            (('B', 'Clean'),): 'Left',
            (('B', 'Dirty'),): 'Suck',

            
            (('A', 'Clean'), ('B', 'Dirty')): 'Suck',
            (('A', 'Clean'), ('B', 'Clean')): 'Right',   
            (('A', 'Dirty'), ('A', 'Clean')): 'Right',   
            (('B', 'Dirty'), ('B', 'Clean')): 'Left',   

            
            (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Dirty')): 'Suck',
            (('A', 'Dirty'), ('A', 'Clean'), ('B', 'Clean')): 'Left',
        }

    def act(self, current_percept):
        """Appends current percept to history and looks up the next action."""
        self.percept_history.append(current_percept)

        history_key = tuple(self.percept_history)
        action = self.table.get(history_key, 'Right')  

        return action
if __name__="__main__":
    agent=TableDrivenVacuumAgent()
    percept_1=('A','Dirty')
    action_1 =agent.act(percept_1)
    print(f"percept:{percept_1}->Action:{action_1}")
    percept_2=('A','clean')
    action_2 =agent.act(percept_2)
    print(f"percept:{percept_2}->Action:{action_2}")
    percept_3=('B','Dirty')
    action_3 =agent.act(percept_3)
    print(f"percept:{percept_3}->Action:{action_3}")
    

    
    
    
    
