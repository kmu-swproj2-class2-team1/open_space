"""

예외처리와 del 모든 이름 삭제 기능 처리했습니다 find 기능과 inc명령 코드를 추가하려고 하면
unexpected unindent(공백오류)가 떠서 공백찾다가 못했습니다... 일단 주석에다가 달아두겠습니다

#find 기능
        elif parse[0] == 'find':
            try:
                for i in scdb:
                    if i['Name'] == parse[1]:
                        print(scdb)

#inc 기능
        elif parse[0] == 'inc':
                try:
                    for p in scdb:
                        if p['Name'] == parse[1]:
				print(parse[3]+20)

#아마 find와 inc기능 잘못구현한것같네요

"""
import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
        try:
            fH = open(dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", dbfilename)
            return []

        scdb = []
        try:
            scdb =  pickle.load(fH)
        except:
            print("Empty DB: ", dbfilename)
        else:
            print("Open DB: ", dbfilename)
        fH.close()
        return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
                
                try:
                    record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                    if parse[1:3] == str:
                        int(parse[1:3])
                    scdb += [record]

                except IndexError as e:
                    print(str(e))
			
        elif parse[0] == 'del':
                try:
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            scdb.remove(p)	
                            
                except:
                    print("Error) Select People or noting in DB")
                        
            
        elif parse[0] == 'show':
                try:
                    sortKey ='Name' if len(parse) == 1 else parse[1]
                    showScoreDB(scdb, sortKey)
                except:
                    print("error")
        
        elif parse[0] == 'quit':
                    break

        else:

            print("Invalid command: " + parse[0])
			

def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
