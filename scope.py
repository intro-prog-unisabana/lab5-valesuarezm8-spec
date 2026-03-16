global_str= None
global_int= None
def set_globals(some_int, some_str):
    global global_int
    global global_str
    global_int = some_int
    global_str = some_str

def get_globals():
    return (global_int, global_str)
    
print(get_globals())       # Salida: (None, None)
set_globals(10, "Hello")
print(get_globals())       # Salida: (10, "Hello")