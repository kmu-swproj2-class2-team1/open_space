class Guess:

    def __init__(self, word):
        #비밀로 선택된 단어를 인자로 받아, 그것을 기록해 둠
        #추측에 이용된 글자들의 집합을 빈 집합으로 초기화
        #실패한 추측의 회수를 기록하기 위한 변수를 0 으로 초기화
        #지금까지 알아낸 글자들과 그 위치를 가리키는 데이터를 초기화

        self.secretWord = word
        self.numTries = 0
        self.currentStatus = ()
        self.correctList = {x : '_' for x in range(len(word))}       #정답이 들어갈 부분을 딕셔너리로 만듬


    def display(self):
        #지금까지 알아낸 글자들과 그 위치를 가리키는 데이터를 화면에 출력
        #실패한 추측의 회수를 화면에 출력

        if self.numTries == 0 :
            print('Current :', len(self.secretWord) )
            print('Tries : ', self.numTries)
        else :
            print('Current :', self.currentStatus)
            print('Tries :', self.numTries)


    def guess(self, character):
        #이 클래스의 (그리고 이 게임 전체의) 핵심적인 기능을 수행
        #character에 의하여 주어지는 한 글자를 사용자가 추측하는 것으로 처리
        #전체 단어를 완성했는지 (모든 글자를 맞추었는지) 여부를 리턴
        #주어진 글자를 사용한 글자의 집합에 원소로 추가
        #비밀 단어에 주어진 글자가 없으면 실패한 회수가 증가
        #지금까지 알아낸 글자와 그 위치를 나타내는 데이터를 갱신
        #위에서 갱신한 데이터가 모든 위치의 글자를 알아낸 경우에 해당하면 True 를, 그렇지 않으면 False 를 리턴

        for i in range(len(self.secretWord)) :
            if character == self.secretWord[i] :
                self.correctList[i] = character

            elif character is not in self.secretWord :
                self.Life += 1