class Guess:

    def __init__(self, word):
        #비밀단어/중복단어 저장할 변수/최대 목숨/현재 상황/시도한 횟수/생명/정답 딕셔너리를 초기화하는 메소드

        self.secretWord = word
        self.guessedChars = set([''])
        self.maxTries = 6
        self.currentStatus = ''
        self.numTries = 0
        self.life = 0
        self.index_Alpha = {x:'_' for x in range(len(word))} #실제로 정답이 채워질부분

    def display(self):
        #화면에 출력해주는 메소드

        if self.numTries is 0:
            print("Current: %s" %('_'*len(self.secretWord)))
            print("Tries: %s" %self.numTries)
        else:
            print("Current: %s" %self.currentStatus)
            print("Tries: %s" %self.numTries)

    def guess(self, character):
        #사용자 입력을 차리하는 메소드

        character = character.lower() #입력이 대문자로 들어왔을때 예외처리

        if character.isalpha() is False: #입력받은 문자가 알파벳이 아닐경우 예외처리
            print("It's not an alphabet. Please re-enter.")
            return False

        for i in range(len(self.secretWord)):
            if character == self.secretWord[i]:
                self.index_Alpha[i] = character
            elif character not in self.secretWord:
                self.life += 1
                break

        self.currentStatus = self.make_word(self.index_Alpha) #딕셔너리에 있는 정보들을 문자열로 바꿔줌
        self.numTries += 1

        if self.currentStatus == self.secretWord:
            return True

        return False

    def make_word(self, answer):
        #딕셔너리에 있는 정보들을 문자열로 만들어 리턴해주는 메소드

        self.currentStatus = ''
        for i in range(len(self.index_Alpha)):
            self.currentStatus += self.index_Alpha[i]
        return self.currentStatus
