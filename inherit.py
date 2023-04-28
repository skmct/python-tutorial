class alphabet:
    url="alphabet.com"
    def __init__(self):
        self.name="alphabet"
class youtube(alphabet):
    def show(self):
        print(self.name)
e1=youtube()
e1.show()
print(e1.url)