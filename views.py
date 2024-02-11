import builtins
class cache:
    def __init_subclass__(self):
        i  = b'/xcache'
        print(builtins.memoryview(i))
class memory(cache):
    def __init__(self):
        super(memory, self).__init__()
memory()