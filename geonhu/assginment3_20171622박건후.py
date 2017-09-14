import pickle

dbfilename = 'assignment3.dat'

def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')

    except FileNotFoundError as e:
        print("새로운 db이름 : ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
        for p in scdb:
            p["Score"] = int(p["Score"])
            p["Age"] = int(p["Age"])

    except:
        print("empty DB: ", dbfilename)

    else:
        print("open DB: ", dbfilename)

    fH.close()

    return scdb

def doScoreDB(scdb):
    while(True):
        inputstr = (input("score DB : "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        try:
            if parse[0] == 'add':
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]

            elif parse[0] == 'del':
                delDB(scdb,parse[1])

            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)

            elif parse[0] == 'find':
                findDB(scdb, parse[1])

            elif parse[0] == 'inc':
                incDB(scdb, parse[1], parse[2])

            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])

        except (ValueError,IndexError):
            print("입력 양식을 확인해주세요~")

        except:
            print("\n없는 명령을 입력하신 거 같네요")

def showScoreDB(scdb, keyname):

    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()

def delDB(scdb, parse):
    list_scdb = scdb[:]

    for p in list_scdb:
        if p['Name'] == parse:
            scdb.remove(p)

def findDB(scdb, name):
    find_complete = False

    for p in scdb:
        if p['Name'] == name:
            for attr in p:
                print(attr + "=" + str(p[attr]), end=' ')
            find_complete = True
            print()

    if find_complete == False:
        print("This name does not exist.")

def incDB(scdb, name, amount):
    inc_complete = False
    for i in range(len(scdb)):
        if scdb[i]['Name'] == name:
            for attr in scdb[i]:
                print(attr + "=" + str(scdb[i][attr]), end=' ')
            scdb[i]['Score'] = scdb[i]['Score'] + int(amount)
            inc_complete = True
            print("얼마만큼 높임 :", scdb[i]['Score'])

    if inc_complete == False:
        print("이름이 존재하지 않습니다.")


if __name__ == "__main__":
    scoredb = readScoreDB()
    doScoreDB(scoredb)
    writeScoreDB(scoredb)
