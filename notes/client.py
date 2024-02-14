
class Client(object) : 
    def __init__(self) : # property를 사용하고자 하는 경우, 빈값으로 생성
        self._name = '' 
        self._year = 0
        self._client_id = 0
        
    @property # decorator
    def name(self) :
        return self._name
    
    @name.setter # setter
    def name(self, value) : # 외부로부터 정보를 받아들일 value 필요
        self._name = value # __init__에서 초기에 생성되는것과 달리, 따로 지정이 가능하다
        
    @property
    def year(self) :
        return self._year
    
    @year.setter
    def year(self, value) :
        self._year = value
        
    @property
    def client_id(self) :
        return self._client_id
    
    @client_id.setter
    def client_id(self, value) :
        self._client_id = value
        
    def introduce_client(self) :
        return self.name, self._year, self._client_id
