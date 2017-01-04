class as4:
    def __init__(self, std_style,mnt_style,finish, ht_dig,ht_dec, bays):
        self.std_style = std_style
        self.mnt_style = mnt_style
        self.finish = finish
        self.ht_dig = ht_dig
        self.ht_dec = ht_dec
        self.bays = bays

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
        bay_fmt = ""
        for bay in self.bays:
            bay_fmt = "{}{}".format(bay_fmt, bay)
            
        return"304-0001-{}{}{}-{}{}-{}".format(self.std_style, self.mnt_style, self.finish, self.ht_dig, self.ht_dec, bay_fmt)



