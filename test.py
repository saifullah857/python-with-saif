appointments = ['09:00', '09:30', '09:00', '10:15', '11:00', '10:15', '09:00']




print(type(appointments))
def analyze(appointments):
    
    
    
    unique = set()
    duplicate = set()          
    
    for appointment in appointments:
        
        if appointment in unique:
            duplicate.add(appointment)
        else:
            unique.add(appointment)
            
    print(f"All unique appointments are = {unique}")
    print(f"All duplocates appointments are = {duplicate}")
    
    
    
analyze(appointments)
    
