import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


from objects.peploe import Peploe

class PeploeTest(Peploe):
    def __init__(self, name="Bruno", age=18):
        super().__init__(name, age)

    def test_how_is_anyone_specific(self, visualization="phrase"):
        print(self.how_is_anyone_specific(visualization))
    
    def test_how_is_anyone_all(self):
        print(self.how_is_anyone_all())

    def test_ask_job_specific(self, visualization="phrase"):
        print(self.ask_job_specific(visualization))
    
    def test_ask_job_all(self):
        print(self.ask_job_all())

p1 = PeploeTest()
p1.test_ask_job_specific("phrase")