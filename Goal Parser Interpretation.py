class Solution:
    def interpret(self, command: str) -> str:
        x=command.count("()")
        y=command.count("(al)")
        
        command = command.replace('()', "o", x)
        command = command.replace('(al)', "al", y)
        return command
