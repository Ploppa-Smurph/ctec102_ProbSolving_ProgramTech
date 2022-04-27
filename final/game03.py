class Realm:    
    
    def __init__(self, name, year, description):
        self.__name = name
        self.__year = year
        self.__description = description
        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
        
    def get_description(self):
        return self.__description
    def set_description(self, description):
        self.__description = description
        
def create_Realm(self, name, year, description):
    "Japan" = {
            Japan.set_name("Japan"),
            Japan.set_year("1868 AD"),
            Japan.set_description("The land of the rising sun.")
            }
    "Rome" = {
            Rome.set_name("Rome"),
            Rome.set_year("0AD"),
            Rome.set_description("The expanding empire of the Roman Empire")
        }
    "Pacific" = {
            Pacific.set_name("Pacific Ocean"),
            Pacific.set_year("1492 AD"),
            Pacific.set_description("On the Santa Maria watching lights in the water dance next to the ship.")
            }
    "Portland" = {
            Portland.set_name("Portland"),
            Portland.set_year("1897 AD"),
            Portland.set_description("At the end of the Portland trail; Your realize you are on a busy street.")
            }
    "Buenos" = {
            Buenos.set_name("Buenos Aires"),
            Buenos.set_year("2401 AD"),
            Buenos.set_description("A sprawling neighborhood in a future Buenos Aires")
                    }
    realm_Set = [Japan, Rome, Pacific, Portland, Buenos]    
    
    return realm_Set
    

            

            
