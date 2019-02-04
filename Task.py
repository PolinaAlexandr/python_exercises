class Color: 
    RED = '0;31'
    GREEN = '0;32'
    YELLOW = '1;33'
   

    def __init__(self, color):
        self.color = color 


    def __enter__(self):
        print('\033[{}m'.format(self.color))


    def __exit__(self, exc_type, exc_value, tb):
        print('\033[00m')
   
    
       


    
     
