# 클래스 Person의 iu 인스턴스(오브젝으)를 만들어봅시다. 
class Person: # 코드들의 묶음
    dna = 46
    def __init__(self, input_name, age, is_female, dna=None): # 생성자 method (__init__)
        # self(관례)로 시작, name 필수 인자 지정
        self.name = input_name
        self.age = age
        self.is_female = is_female
        if dna != None:
            self.dna = dna
        # self. 붙이면 자기 스스로에게 지정 그냥 name이면 인자
        
    def hello(self): # class 정의할 때, self항상 작성해야함
        print(f'안녕하세요 저는 {self.name}입니다.')
        print(f'저는 {self.age}살입니다.')
        print(f'저는 여성입니다.' if self.is_female else '저는 남성입니다.')
        print(f'나의 dna는 {self.dna}입니다.')

# class 선언 => __init__ 있는지 먼저 확인

iu = Person('iu', 26, 1) # create 인스턴스 객체, input_name = 'iu'
iu.hello()
john = Person('john', 28, 0, 5)
john.hello()