class TableDrivenAutonomousTaxi:
    def __init__(self):
        self.percept_history=[]

        self.table={
            (('Red', 'No'),): 'Stop',
            (('Yellow', 'No'),): 'Ready',
            (('Green', 'No'),): 'Move Forward',
            (('Green', 'Yes'),): 'Control Speed',

            
            (('Red', 'No'), ('Yellow', 'No')): 'Ready',
            (('Red', 'No'), ('Green', 'No')): 'Move Forward',   
            (('Red', 'No'), ('Green', 'Yes')): 'Control Speed',   
            (('Green', 'No'), ('Red', 'No')): 'Stop',
            

            
            (('Red', 'No'), ('Yellow', 'No'), ('Green', 'No') ): 'Move Forward',
            (('Red', 'No'), ('Yellow', 'No'), ('Green', 'No'),('Green','Yes')): 'Control Speed',
             }
            
    def act(self, current_percept):
        """Appends current percept to history and looks up the next action."""
        self.percept_history.append(current_percept)

        history_key = tuple(self.percept_history)
        action = self.table.get(history_key, 'Stop')

        return action
    
if __name__=="__main__":
    agent=TableDrivenAutonomousTaxi()
    percept_1=('Red','No')
    action_1 =agent.act(percept_1)
    print(f"percept:{percept_1}->Action:{action_1}")
    percept_2=('Yellow','No')
    action_2 =agent.act(percept_2)
    print(f"percept:{percept_2}->Action:{action_2}")
    percept_3=('Green','No')
    action_3 =agent.act(percept_3)
    print(f"percept:{percept_3}->Action:{action_3}")
    percept_4=('Green','Yes')
    action_4 =agent.act(percept_4)
    print(f"percept:{percept_4}->Action:{action_4}")
    
        
    
            
            
            
