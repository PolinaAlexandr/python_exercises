class Color: 
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    WHITE_b = '47'
    CYAN_b = '46'
   

    def __init__(self, color, back):
        self.color = color 
        self.back = back
        
        
    @staticmethod
    def int_to_color(input):
        int_to_color_dict = {
            1: Color.RED,
            2: Color.GREEN,
            3: Color.YELLOW,
            10: Color.WHITE_b,
            11: Color.CYAN_b,
        }

        return int_to_color_dict.get(input)

    def __enter__(self):
        print('\033[1;{}m\033[1;{}m'.format(self.color, self.back))


    def __exit__(self, exc_type, exc_value, tb):
        print('\033[00m')
   
    
       


    
     
