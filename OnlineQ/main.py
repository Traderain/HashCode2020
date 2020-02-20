

class Library:
    bookcount = 0
    signuplen = 0
    ship = 0
    books = list()


class Schedule:
    book_score = list()
    bookcount = 0
    days = 0
    scores = list()
    libs = list()


def main():
    lines = []

    fp = './a_example'


    with open(fp + '.in') as f:
        lines = f.readlines()

    split0 = lines[0].split(' ')

    sch = Schedule()

    # Read basics
    sch.bookcount = split0[0]
    libs = split0[1]
    sch.days = split0[2]

    for i in lines[1].split(' '):
        sch.book_score.append(i)

    for i in range(0, int(libs)):
        linenum = 1 + i*2 + 1
        
        l = Library()
        lsplit = lines[linenum].split(' ')
        l.bookcount = int(lsplit[0])
        l.signuplen = int(lsplit[1])
        l.ship = int(lsplit[2])

        for book in lines[linenum+1].split(' '):
            l.books.append(int(book))
        sch.libs.append(l)
    print('Meme')






    

if __name__ == "__main__":
    main()

