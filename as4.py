class as4:
    def __init__(self, std_style,mnt_style,fnish, ht_dig,ht_dec, bays):
        self.std_style = "N"
        self.mnt_style = "B"
        self.finish = "C"
        self.ht_dig = 97
        self.ht_dec = 0
        self.bays = []

    def prompt(self):
        print("Welcome to part number generator for AS4")
        self.std_mount = input("(N)ormal or (F)loor mount standards?:")

    def getHW(self):
        parts_list = []

        num_std = len(self.bays) + 1

        parts_list.append({"pn":"112-0003", "qty":num_std*2})
        parts_list.append({"pn":"200-0002", "qty":num_std*2})
        parts_list.append({"pn":"112-0005", "qty":num_std})
        parts_list.append({"pn":"100-0005", "qty":num_std})
        parts_list.append({"pn":"112-0002", "qty":num_std*2})
        parts_list.append({"pn":"100-0003", "qty":num_std*2})

        return parts_list

    def genPn(self):
        for bay in self.bays:
            print(bay)
            
        return"304-0001-{}{}{}-{}{}-{}".format(self.std_style, self.mnt_style, self.finish, self.ht_dig, self.ht_dec, bay_fmt)



