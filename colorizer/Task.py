class Color:
    BLACK = '30'
    BLACK_b = '40' 
    RED = '31'
    RED_b = '41'
    GREEN = '32'
    GREEN_b = '42'
    YELLOW = '33'
    YELLOW_b = '43'
    BLUE = '34'
    BLUE_b = '44'
    MAGENTA = '35'
    MAGENTA_b = '45'
    CYAN = '36'
    CYAN_b = '46'
    WHITE = '37'
    WHITE_b = '47'
    
    
   

    def __init__(self, color, back):
        self.color = color 
        self.back = back
        
        
    @staticmethod
    def int_to_color(input):
        int_to_color_dict = {
            1: Color.BLACK,
            10: Color.BLACK_b,
            2: Color.RED,
            20: Color.RED_b,
            3: Color.GREEN,
            30: Color.GREEN_b,
            4: Color.YELLOW,
            40: Color.YELLOW_b,
            5: Color.BLUE,
            50: Color.BLUE_b,
            6: Color.MAGENTA,
            60: Color.MAGENTA_b,
            7: Color.CYAN,
            70: Color.CYAN_b,
            8: Color.WHITE,
            80: Color.WHITE_b
        }

        return int_to_color_dict.get(input)

    def __enter__(self):
        print('\033[1;{}m\033[1;{}m'.format(self.color, self.back))


    def __exit__(self, exc_type, exc_value, tb):
        print('\033[00m')
   
    
       


    
     
