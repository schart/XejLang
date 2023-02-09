import json

class Data:  
    def __init__(self) -> None:
        self.path = 'works/'
    
    def config(self):
        #! Is support one file for now
        data_files: any = []
        with open("settings.json", "r") as file:
            deserialized_data = json.loads(file.read())

            for i in deserialized_data['files']:
                data_files.append(i)
            return list(data_files)

    def reader(self) -> list: #! return command as line 
        """ This is a mini-lexer"""
        data_files: list = self.config()

        for i in data_files:  
            
            with open(self.path+i, 'r') as f:
                _result: any = f.readlines(); _detect_comment: any; _list: list = []; _editedList: list = [];
                
                for i in _result:

                    _line = i.lstrip().rstrip(); _detect_comment = _line[0:2]
                    
                    if _detect_comment == '//' or _line == '':  continue; 
                    else: _list.append(i.rstrip().lstrip().split(' ')); 
                

                return list(_list)




    def iterator(self, _iterator: int) -> list:
        if _iterator > len(self.reader()): return None
        else: 
            next_list: list = self.reader()[_iterator-1]
            return list(next_list)   


    def edit(self, _count: int) -> list: #! return list as edited
        readedList = self.iterator(_count)
        if readedList == None: return None
        else:
            while True:
                try: readedList.remove('')
                except: return [list(readedList), len(self.reader())] 


print(Data().reader())