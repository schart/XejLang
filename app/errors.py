
class Errors:
    def __init__(self) -> None:
        pass


    def error_syntax(self, _line: int, _word: str, _secretDescription: str) -> str: print(f'{_secretDescription}\n\tParsing error at line: {_line}, at  word = {_word}')
    def error_flag(self, _line: int, _word: str) -> str: print(f"You must use flag for create statement like name or description\n\tError at line: {_line} at word = {_word}")
    def error_process(self, _line: int, _word: str, _process: str) -> str: print(f"You must choose  process {_process}\n\tError: before from '{_word}' at line: {_line}");  
    def errror_templatenotFound(self, _line: int, _template: str) -> str: print(f"Template not found = {_template} at line: {_line}")
    def error_filenotFound(self, _arg: str) -> str: print(f"Could not, File: {_arg}")
    def error_alreadyFile(self, _arg: str) -> str: print(f"Already File with name: {_arg}")
    def error_usePrefix(self, _arg: str) -> str: print(f"You should start with prefix: {_arg}")
    def error_wrongFlag(self, _flag: str, _prefix: str, _template: str) -> str: print(f" You must enter prefix({_prefix}) flag({_flag}) and choose a ready template: {_template}")


    