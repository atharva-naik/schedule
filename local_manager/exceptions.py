from colors import color

class EventExistsError(Exception):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event=event.to_dict()
    
    def __str__(self):
        return color(f"This {self.event['type']} event ({self.event['name']}) already exists, starting at {self.event['start']} and lasts for {self.event['duration']} hours{self.event['']}", fg='red')

class EventDoesntExistError(Exception):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event=event.to_dict()
    
    def __str__(self):
        return color(f"This {self.event['type']} event ({self.event['name']}) doesn't exist.", fg='red')

class InvalidOperationType(Exception):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name=name 
    
    def __str__(self):
        return color(f"\"{self.name}\" is not a valid operation type", fg='red')

class InvalidScheduleType(Exception):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name=name 
    
    def __str__(self):
        return color(f"\"{self.name}\" is not a valid schedule type", fg='red')

class InvalidCommand(Exception):
    def __init__(self):
        pass 
    def __str__(self):
        return color("Malformed command!", fg='red', style='bold')