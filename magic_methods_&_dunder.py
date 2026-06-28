class Squire:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __add__(self, other):
        return Squire(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return (f"Hello world from bangladesh");

    def __call__(self):
        print("HELLO WORLD!"); # THIS CALLED IS MAGIC METHOD - FARTHER MORE INFORMATION CHECK DOCS.

    def gratings(self, name):
        print(f"Welcome {name}!");

__hello_world__ = "4";
print(__hello_world__);

squire = Squire(4, 5);
squire2 = Squire(6, 5);
combine = squire + squire2;

combine.gratings('Dolon Roy');
