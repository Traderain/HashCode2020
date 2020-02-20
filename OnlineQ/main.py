import io

class Library:
    bookcount = 0
    signuplen = 0
    ship = 0
    books = list()

    def __init__(self):
        self.bookcount = 0
        self.signuplen = 0
        self.ship = 0
        self.books = list()

    def fitness(self):
        return  self.ship * self.bookcount * ( 1 / self.signuplen)





class Schedule:
    book_score = list()
    bookcount = 0
    days = 0
    scores = list()
    libs = list()

    def __init__(self):
        self.book_score = list()
        self.bookcount = 0
        self.days = 0
        self.scores = list()
        self.libs = list()

class ShippingSchedule:

    sends = list()

    def __init__(self):
        self.sends = list()
    
    def printtofile(self, path):
        with open(path, 'w') as f:
            # Library count
            f.write(str(len(self.sends)) + "\n")

            for i in range(0, len(self.sends)):
                f.write(str(self.sends[i][0]) + " ")
                for j in range(0, len(self.sends[i][1])):
                    f.write(str(self.sends[i][1][j]) + " ")
                f.write("\n")                

def main():
    lines = []

    fp = './a_example.in'


    with open(fp) as f:
        lines = f.readlines()

    split0 = lines[0].split(' ')

    sch = Schedule()

    # Read basics
    sch.bookcount = int(split0[0].strip())
    libs = int(split0[1].strip())
    sch.days = int(split0[2].strip())

    for i in lines[1].split(' '):
        sch.book_score.append(int(i.strip()))

    for i in range(0, int(libs)):
        linenum = 1 + i*2 + 1
        
        l = Library()
        lsplit = lines[linenum].split(' ')
        l.bookcount = int(lsplit[0].strip())
        l.signuplen = int(lsplit[1].strip())
        l.ship = int(lsplit[2].strip())

        for book in lines[linenum+1].split(' '):
            l.books.append(int(book.strip()))
        sch.libs.append(l)
    print('Meme')
    ss = ShippingSchedule()

    vals = list()
    vals.append(0)
    vals.append(1)
    vals.append(2)
    ss.sends.append((0,vals))
    ss.sends.append((0,vals))
    ss.sends.append((0,vals))

    ss.printtofile('test.out')






    

if __name__ == "__main__":
    main()

