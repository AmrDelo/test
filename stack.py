class stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def popp(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Empty Stack"
    def print_stack(self):
        for ele in self.items:
            print(ele)
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    
st = stack()
st.push(10)
st.push(9)
removed = st.popp()
print("Removed ",removed)
st.push(15)

print("Stack size ",st.size())
print("Stack items ")
st.print_stack()
