from pathlib import Path
from aocd import submit
import os;

class AoCException(Exception):
    """
    custom error class for issues related to creating/running solutions
    """

    pass

class BaseSolution():
    _year: int
    _day: int

    def __init__(self, lines = False, csv = False):
        if lines:
            self.input = self.read_input().splitlines()
        else:  
                if csv:
                    lines = self.read_input().splitlines()

                    self.input = [line.split(",") for line in lines]
                else:    
                    self.input = self.read_input()  

    @property
    def year(self):
        if not hasattr(self, "_year"):
            raise NotImplementedError("explicitly define Solution._year")
        return self._year

    @property
    def day(self):
        if not hasattr(self, "_day"):
            raise NotImplementedError("explicitly define Solution._day")
        return self._day

    def read_input(self) -> str:
        """
        handles locating, reading, and parsing input files
        """
        input_file = Path(
            Path(__file__).parent.parent.parent,
            f"input.txt",
        )
        if not input_file.exists():
            raise AoCException(
                f'Failed to find an input file at path "./{input_file.relative_to(Path.cwd())}". You can run `./start --year {self.year} {self.day}` to create it.'
            )

        data = input_file.read_text().strip("\n")

        if not data:
            raise AoCException(
                f'Found a file at path "./{input_file.relative_to(Path.cwd())}", but it was empty. Make sure to paste some input!'
            )
        return data
    
    def save(self, part, res):
        answer_path = Path(
            Path(__file__).parent.parent.parent,
            f"ans{part}.txt",
        )

        if os.path.exists(answer_path): 
            open(answer_path, 'w').close() # always overwrite

        f = open(answer_path, "a")
        f.write(res)
        f.close()

    def submit(self, part, res):
        submit(res, part=part, day=self.day, year=self.year)

    def solve(self, part, res):
        self.save(part, str(res))

        print(f"Part {part}:: {res}")

        self.submit(part = "a" if part == "1" else "b" , res = res)

class InputAsStringSolution(BaseSolution):
        def __init__(self):
            super().__init__(lines=False, csv=False)

class InputAsLinesSolution(BaseSolution):
        def __init__(self):
            super().__init__(lines=True, csv=False)

class InputAsCSVSolution(BaseSolution):
        def __init__(self):
            super().__init__(lines=False, csv=True)