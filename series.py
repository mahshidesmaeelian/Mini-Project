from media import Media

class Series(Media):
    def __init__(self , media_pack):
        super().__init__(media_pack[0], media_pack[1], media_pack[2], media_pack[3], media_pack[4], media_pack[5],media_pack[6])
        self.seasons = media_pack[7]
        self.episodes = media_pack[8]

    def edit_series_info(self):
        print('1-id , 2-name , 3-category , 4-imdb rate , 5-url , 6-duration , 7-casts , 8-seasons , 9-episodes')
        
        choise = int(input('choose the item you want to edit:'))

        user_replacement_input = input('enter replacement value:')

        if choise == 1:
            self.id = user_replacement_input

        elif choise == 2:
            self.name = user_replacement_input

        elif choise == 3:
            self.category = user_replacement_input

        elif choise == 4:
            self.IMDB_rate = user_replacement_input

        elif choise == 5:
            self.url = user_replacement_input

        elif choise == 6:
            self.duration = user_replacement_input

        elif choise == 7:
            self.casts = user_replacement_input

        elif choise == 8:
            self.seasons = user_replacement_input

        elif choise == 9:
            self.episodes = user_replacement_input
        else:
            print('error!you must enter a number!')
        self.show_info()