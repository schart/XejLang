process: list =  \
    [
        'FOLDER', 
        'FILE',
        'TEMPLATE'
    ]

already_templates: list = \
    [
        'MVC',
        'MVT'
    ]

prefix: list = \
    [
        'CREATE',
        'BUILD',
        'DELETE', 
    ]

flags: list = \
    {
        '-d': "STRING", #! Delete 
        '-n': "STRING",  #! Name
        '-e': "EXPLAIN", #! Explain Also Know Description
        '-at': "ARGUMENT" #! AlreadyTemplate
    }

from templates import Templates
from errors import Errors
from data import Data

class Main:
    def __init__(self) -> None:
        #? Counters
        self.lineLength: int = 0 #? length of all text
        self.counterCurrentText: int = 0
        self.counterListlement: int = 0

        #? These keep data relevant with text
        self.text: None or str = "non-initilazed"
        self.element: None or str = "non-initilazed"
        
        #? result of parsing
        self.prefix: None or str = None
        self.flag: None or str or dict[str, any] = {}
        self.process: None or str = None  #? also know optional arg

        #? 
        self.unLockSyntax: bool = False



    def add_text(self, current_text: list): 
        if current_text == None:  return  None
        else: self.text = current_text;  

    def add_element(self, current_element: list): 
        if current_element == None:  return None  
        else: self.element = current_element;   
    
    def next_text(self) -> None:
        DataClass = Data()
        if self.counterListlement > len(self.text)-1: return None;
        else: 
            try: 
                self.counterListlement+=1; 
                self.add_text(current_text=DataClass.edit(_count=self.counterListlement)[0]); self.lineLength = DataClass.edit(_count=self.counterListlement)[1];
                self.counterCurrentText = 0
            except:  self.text = None


    def next_element(self) -> None:
        if self.counterCurrentText > len(self.text)-1: return None
        else: 
            self.counterCurrentText+=1; 
            try: self.add_element(current_element=self.text[self.counterCurrentText-1]);     
            except: self.element = None
    
    def check_flag(self, _process: str, _flag: str) -> bool:
        if _flag == '-n':
            if _process == 'FILE' or _process ==  'FOLDER': return True
            else: return False

        if _flag == '-e':
            if _process == 'FOLDER' or self.text[0] == 'DELETE' or self.process == 'BUILD': return False
            else: return True
            
        if _flag == '-at':
            if self.text[0] == "BUILD": return True
            else: return False

    def parser(self) -> None:
        """
            We gonna do process according to prefix and optional arg
            To everytime, syntax have to be as CREATE/DELETE/BUILD FOLDER/FILE  <flag> <name>.
        """
        errors = Errors()
        n: int = 0
        templates: any = Templates()
        self.next_text() #? Text upload

        while n < self.lineLength:  
            self.next_element()            
            #! We check prefix for provide start argument as prefix
            if (self.text[0] in prefix) == False: return errors.error_syntax(_line=n+1, _word=self.element, _secretDescription = 'You should use syntax like that prefix(BUILD, CREATE...) process(FILE, FOLDER)')


            if self.text[0] == 'CREATE':
                self.next_element()
                self.flag = {}
                if (self.element in process) == True:
                    self.process = self.element

                    for i in range(len(self.text)-1):
                        self.next_element(); flag = self.element
                
                        #! 1- Phase flag settings
                        if (flag in flags) == True:
                            self.next_element()
                            if self.check_flag(_process=self.process, _flag=flag) == True:

                                if flags[flag] == "STRING":  

                                    if self.element[0] == '"' and self.element.endswith('"') == True: self.flag[f"{flag}-{i}"] = self.element
                                    else: return errors.error_syntax(_line=n+1, _word=self.element, _secretDescription = 'You should use syntax like that "arg"\n\t if you wanna use flag of string type')
                                
                                else: self.flag[f"{flag}-{i}"] = self.element
                                
                                if flags[flag] == "EXPLAIN":
                                    self.unLockSyntax = True #! Open syntax for extend
                                    splited: list = self.element.split(':')
                                    
                                    if len(splited) == 2:

                                        if self.element[0] == '"' and self.element.endswith('"') == True: self.flag[f"{flag}-{i}"] = splited
                                        else: return errors.error_syntax(_line=n+1, _word=self.element, _secretDescription = 'You should use syntax like that "arg"\n\t if you wanna use flag of string type')

                                    else: return errors.error_syntax(_line=n+1, _word=self.element, _secretDescription = 'You should use ":" for assigment')
                            
                            else: return print(f"Wrong flag {flag} for that process: {self.text[0]}/{self.process}")
                        
                        else: 
                            if self.unLockSyntax != True:
                                if self.element and (self.text[self.counterCurrentText-2] in flags) == False: return errors.error_flag(_line=n+1, _word=self.element) 
                            else: continue    

                    templates.create(_process=self.process, _flags=self.flag);  
            
                #! If you don't use process like FILE etc.
                else: return errors.error_process(_line=n+1, _word=self.element, _process=process)  

            
            if self.text[0] == 'BUILD':
                self.next_element()
                flag = self.element
                
                if len(self.text) == 3:

                    if self.element in flags:
                        self.next_element()

                        if self.check_flag(_process=self.process, _flag=flag) == True:
                        
                            if self.element in already_templates: templates.build(_flag=flag, _template=self.element)
                            else: errors.errror_templatenotFound(_line=n+1, _template=self.element)
                        
                        else: return print(f"Wrong flag {flag} for that process: {self.text[0]}/{self.process}")
                    
                    else: errors.error_flag(_line=n+1, _word=self.element)
                
                else: print(f"You must enter prefix(BUILD) flag(-at) and choose a ready template {already_templates}") 

            if  self.text[0] == 'DELETE':
                self.next_element()
                self.flag = {}

                if (self.element in process) == True:
                    self.process = self.element

                    for i in range(len(self.text)-2):
                        self.next_element(); flag = self.element

                        #! 1- Phase flag settings
                        if (self.element in flags) == True:
                            self.next_element()
                            if self.check_flag(_process=self.process, _flag=flag) == True:

                                if flags[flag] == "STRING":                                  
                                
                                    if self.element[0] == '"' and self.element.endswith('"') == True:  self.flag[f"{flag}-{1}"] = self.element
                                    else: return errors.error_syntax(_line=n+1, _word=self.element, _secretDescription='You should use syntax like that "arg" if you wanna use flag of string type')
                                
                                else: self.flag[f"{flag}-{2}"] = self.element #! with another flag       
                                
                            else: return print(f"Wrong flag {flag} for that process: {self.text[0]}/{self.process}")
                        
                            
                        else:  
                            if (self.text[self.counterCurrentText-2] in flags) == False: return errors.error_flag(_line=n+1, _word=self.element) 
                            #if self.element != "-n" and self.element and (self.text[self.counterCurrentText-2] in flags) == True: return print(f"you are can't use that {self.element} flag with DELETE proccess") 

                    templates.delete(_process=self.process, _flags=self.flag)
                else: return errors.error_process(_line=n+1, _word=self.element, _process=process)  
            

                    
            self.next_text()
            n+=1; 

if __name__ == '__main__':
        Main().parser()
        #_result = Main.parser();  


