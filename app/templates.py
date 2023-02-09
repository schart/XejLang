import os
import shutil


class Templates: 
    def __init__(self) -> None:
        self.mvc = ["Model", "View", "Controller"]
        self.mvt = ["Model", "View", "Template"]

    def builder(self, _chooses: str, _parentDir: str):
        os.mkdir(_parentDir)
        for i in _chooses:
            os.mkdir(_parentDir+'/'+i)

    def build(self, _prefix: str = "BUILD", _flag: str = None, _template: str = None) -> None:
        print("BUILDED: ", _flag, _template)

        if _template.lower() == 'mvc':
            try: 
                self.builder(_chooses=self.mvc, _parentDir=_template)
            except: 
                return print("File/Folder already exist")

        if _template.lower() == 'mvt':
            try: 
                self.builder(_chooses=self.mvt, _parentDir=_template)
            except: 
                return print("File/Folder already exist")



    def delete(self, _prefix: str = "DELETE",  _process: str = None, _flags: dict = {None, None}) -> None:
        print("DELETED: ", _flags)
        
        for i in _flags:
            arg: any = _flags[i].split('"')[1]
            try: 
                if _process.lower() == 'folder':
                    shutil.rmtree(os.getcwd()+'/'+arg)

                if _process.lower() == 'file': 
                    os.remove(os.getcwd()+'/'+arg)

            except: print("File not found: ", arg)



    def create(self, _prefix: str = "CREATE", _process: str = None, _flags: dict = {None, None}) -> None:
        z: int = 0;        
        print("CREATED: ", _flags)

        for i in _flags:
            if _process.lower() == "file":       

                flag = i.split('-')[1]
                

                if flag == 'n':
                    name = _flags[i].replace('"', "") 
                    
                    try: 
                        f = open(os.getcwd()+'\\'+name, "w")
                        f.close()
                    except: return print("Already exist file") 
                
                if flag == 'e':
                    file_name: str = _flags[i][0].replace('"', "") 
                    file_description: str = _flags[i][1].replace('"', "")
                    

                    if os.path.exists(os.getcwd()+'\\'+file_name) == True:
                        f = open(os.getcwd()+'\\'+file_name, "a")
                        f.write(file_description)
                        f.close()
                    else: return print("File not found")
                
            else: 
                try: 

                    os.mkdir(os.getcwd()+'/'+name)
                except: print("File not found: ")

        z+=1



