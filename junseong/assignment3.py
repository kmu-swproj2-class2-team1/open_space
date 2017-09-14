import pickle

dbfilename = 'assignment3.dat'


class UserNotFound(Exception):
    def __init__(self):
        super()


def read_score_db():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()

    for row in scdb:
        row['Score'] = int(row['Score'])
        row['Age'] = int(row['Score'])

    return scdb


def write_score_db(scdb):
    with open(dbfilename, 'wb') as fH:
        pickle.dump(scdb, fH)


def show_score_db(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


def do_score_db(scdb):
    while True:
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        command = parse[0]

        # add [name] [age] [score]
        if command == 'add':
            try:
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb.append(record)

            except IndexError:
                print("Please check your add command form")
                print("add [name] [age] [score]")

            except:
                print("Unknown exception occured")

        # show [default : Name / opt : Age, Score]
        elif command == 'show':
            try:
                sortKey = 'Name' if len(parse) == 1 else parse[1]

                if sortKey not in ['Name', 'Age', 'Score']:
                    raise KeyError

                show_score_db(scdb, sortKey)

            except KeyError:
                print("Please check your sorting key")
                print("[default : Name / opt : Age, Score]")

            except IndexError:
                print("Please check your add command form")
                print("show [default : Name / opt : Age, Score]")

            else:
                print("Unknown exception occured")

        # inc [name] [score]
        # handler : multiple user, user not found, argument error
        elif command == "inc":
            try:
                name = parse[1]
                found_users_index = []
                for user_index, row in enumerate(scdb):
                    if row["Name"] == name:
                        found_users_index.append(user_index)

                if len(found_users_index) == 1:
                    scdb[found_users_index[0]]["Score"] += int(parse[2])

                elif len(found_users_index) > 1:
                    try:
                        print("please chose which user to add score")
                        for index, user_index in enumerate(found_users_index):
                            print("- %d / %s" % index, str(scdb[user_index]))
                            select_index = int(input("Which want to delete (ex : 0, 1): "))
                            scdb[found_users_index[select_index]]["Score"] += int(parse[2])
                    except:
                        print("Please enter the index correctly")

                else:
                    raise UserNotFound

            except UserNotFound:
                print("No such user, check the user name")

            except IndexError:
                # if user didn't gave the name info
                print("please enter the name and score with inc command")
                print("ex : inc Junseong 30")

            else:
                print("Unknown exception occured")

        # del [name]
        # handler : multiple user, user not found, argument error
        elif command == "del":
            try:
                name = parse[1]
                found_users_index = []
                for user_index, row in enumerate(scdb):
                    if row["Name"] == name:
                        found_users_index.append(user_index)

                if len(found_users_index) == 1:
                    del scdb[found_users_index[0]]

                elif len(found_users_index) > 1:
                    try:
                        print("please chose which user to delete")
                        for index, user_index in enumerate(found_users_index):
                            print("- %d / %s" % index, str(scdb[user_index]))
                            select_index = int(input("Which want to delete (ex : 0, 1): "))
                            del scdb[found_users_index[select_index]]
                    except:
                        print("Please enter the index correctly")

                else:
                    raise UserNotFound

            except UserNotFound:
                print("No such user, check the user name")

            except IndexError:
                # if user didn't gave the name info
                print("please enter the name with del command")
                print("ex : del Junseong")

            else:
                print("Unknown exception occured")


        # find [name]
        # handler : multiple user, user not found, argument error
        elif command == "find":
            try:
                name = parse[1]
                found_users = []
                for row in scdb:
                    if row["Name"] == name:
                        found_users.append(row)

                if len(found_users) > 0:
                    print("%d users found" % len(found_users))
                    for user in found_users:
                        print(user)
                else:
                    raise UserNotFound

            except UserNotFound:
                print("No such user, check the user name")

            except IndexError:
                # if user didn't gave the name info
                print("please enter the name with find command")
                print("ex : find Junseong")

            else:
                print("Unknown exception occured")

        elif command == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


scoredb = read_score_db()
do_score_db(scoredb)
write_score_db(scoredb)
