import math

class Zlomek:
    def __init__(self, citatel, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel

    def __str__(self):
        return f"{self.citatel}/{self.jmenovatel}"
    
    def zkrat(self):
        nsd = math.gcd(abs(self.citatel), abs(self.jmenovatel))
        self.citatel = int(self.citatel / nsd)
        self.jmenovatel = int(self.jmenovatel / nsd)
        return self
    
    def __add__(self, jiny):
        novy_citatel = self.citatel * jiny.jmenovatel + self.jmenovatel * jiny.citatel
        novy_jmenovatel = self.jmenovatel * jiny.jmenovatel
        novy_zlomek = Zlomek(novy_citatel, novy_jmenovatel)
        return novy_zlomek.zkrat()
    
    def __sub__(self, jiny):
        novy_citatel = self.citatel * jiny.jmenovatel - self.jmenovatel * jiny.citatel
        novy_jmenovatel = self.jmenovatel * jiny.jmenovatel
        novy_zlomek = Zlomek(novy_citatel, novy_jmenovatel)
        return novy_zlomek.zkrat()
    
    def __mul__(self, jiny):
        novy_citatel = self.citatel * jiny.citatel
        novy_jmenovatel = self.jmenovatel * jiny.jmenovatel
        novy_zlomek = Zlomek(novy_citatel, novy_jmenovatel)
        return novy_zlomek.zkrat()
    
    def __truediv__(self, jiny):
        if jiny.citatel != 0:
            novy_citatel = self.citatel * jiny.jmenovatel
            novy_jmenovatel = self.jmenovatel * jiny.citatel
            novy_zlomek = Zlomek(novy_citatel, novy_jmenovatel)
            return novy_zlomek.zkrat()
        
        else:
            print ("Jiný čitatel je 0")

    def __eq__(self, jiny):
        self.zkrat()
        self.zkrat()

        if (self.citatel * jiny.jmenovatel == self.jmenovatel * jiny.citatel):
            return True
        
        else:
            return False
    


z1 = Zlomek(1, 2)
z2 = Zlomek(2, 4)
print(z1 == z2)