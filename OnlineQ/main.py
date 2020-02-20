import io

class Library:
    id = 0
    bookcount = 0
    signuplen = 0
    ship = 0
    books = list()

    def __init__(self):
        self.id = 0
        self.bookcount = 0
        self.signuplen = 0
        self.ship = 0
        self.books = list()

    # Fitness of the library
    def fitness(self):
        return  self.ship * self.bookcount * ( 1 / self.signuplen)

    # Returns the books it sends for x days
    def getbook(self, fordays):
        max = self.ship * fordays
        if max > len(self.books):
            return self.books
        else:
            ret = list()
            for i in range(0, max):
                ret.append(self.books[i])
            return ret
    
    def toSchippingSchedule(self, fordays):
        return (self.id, self.getbook(fordays))





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
                currlib = self.sends[i]
                ## Write ID
                f.write(str(currlib[0]) + " " + str(len(currlib[1])) + "\n")
                currlib_books = self.sends[i][1]
                for j in range(0, len(currlib_books)):
                    f.write(str(currlib_books[j]))
                    if j != len(currlib_books):
                        f.write(" ")
                f.write("\n")           

def main():
    lines = []

    fp = './b_read_on.in'


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
        l.id = i
        lsplit = lines[linenum].split(' ')
        l.bookcount = int(lsplit[0].strip())
        l.signuplen = int(lsplit[1].strip())
        l.ship = int(lsplit[2].strip())

        for book in lines[linenum+1].split(' '):
            l.books.append(int(book.strip()))
        sch.libs.append(l)
    ss = ShippingSchedule()

    sch.libs.sort(key = (lambda a : a.fitness()))
    
    done = False
    iter = 0
    currdays = 0

    while not done and iter < len(sch.libs):
        elem = sch.libs[iter]
        if elem.signuplen + currdays < sch.days:
            ss.sends.append(elem.toSchippingSchedule(sch.days - (currdays + elem.signuplen)))
            currdays = currdays + elem.signuplen
            iter = iter + 1
        else:
            done = True
    ss.printtofile(fp + '.out')



if __name__ == "__main__":
    main()

