"""
project: Just moved in
"""


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area   # no need to pass
        self.item_list = []     # no need to pass

    def __str__(self):
        s = "House information:\n" \
            "The house type is {},\n" \
            "Total area is {:.1f},\n" \
            "Free area is {:.1f},\n" \
            "House item list is {}\n".format(self.house_type,self.area,self.free_area,self.item_list)
        return s

    def add_item(self, houseItem):

        # check if it is possible to place
        if houseItem.area > self.free_area:
            print("Not enough space")
            return

        # place
        self.item_list.append(houseItem)

        # calculate the free_area
        self.free_area -= houseItem.area
