from clip import Clip
from anime import Anime
from movie import Movie
from series import Series
#from Actors import Actors


class Main:
    def __init__(self):
        
        try:
            myfile = open('data.csv' , 'r')
        except:
            print('can not open database file')

        general_data = myfile.read()
        seprated_lines = general_data.split('\n')  

        self.media_list = []


        i = 0
        while i < len(seprated_lines):

            seprated_parts = seprated_lines[i].split(',')

            if seprated_parts[2] == 'series':
                self.media_list.append(Series(seprated_parts))
            elif seprated_parts[2] == 'movie':
                self.media_list.append(Movie(seprated_parts))
            elif seprated_parts[2] == 'anime':
                self.media_list.append(Anime(seprated_parts))
            elif seprated_parts[2] == 'clip':
                self.media_list.append(Clip(seprated_parts))
            else:
                print('error,data not found!')

            i += 1
        
        print('media:' , self.media_list)
        self.showmenu()


    def show_casts_info(self):
        input_id = input('enter the id of the media to show casts list:')
        for i in self.media_list:
            if input_id == i.id :
                i.show_casts()
        else:
            print('sorry there is no media by this id')



        self.showmenu()
        
    def show_info(self):

        for i in self.media_list:
            i.show_info() 

        self.showmenu()  

    def show_actors_info(self):
        for i in self.casts_list:
            i.show_cast_info()
        self.showmenu()
        

    def add_media(self):
        while True:
            id = (int(input('enter media id:')))
            name = (input('enter name:'))

            print('1.clip' , '\n' , '2.movie' , '\n' ,'3.anime' , '\n' ,'4.series')

            category= (input('enter category:'))
            imdb_rate= (float(input('enter imdb rate:')))
            url= (input('enter url:'))
            duration= (input('enter duration:'))
            cast= (input('enter cast:'))

            #info_list = [id,name,category,imdb_rate,url,duration,cast]


            
            if category == 'clip':
                concept = (input('enter concept:'))
                singer = (input('enter name of the singer:'))
                info_list = [id,name,category,imdb_rate,url,duration,cast,concept,singer]
                self.media_list.append(Clip(info_list))
                print(f'{info_list[1]}added succesfully!')
                break

            elif category == 'movie':
                genre = (input('enter genre:'))
                #info_list.append(genre)
                info_list = [id,name,category,imdb_rate,url,duration,cast,genre]
                self.media_list.append(Movie(info_list))
                print(f'{info_list[1]}added succesfully!')
                break

            elif category == 'anime':
                seasons = int(input('enter number of seasons:'))
                episodes = int(input('enter number of episodes:'))
                info_list = [id,name,category,imdb_rate,url,duration,cast,seasons,episodes]
                self.media_list.append(Anime(info_list))
                print(f'{info_list[1]}added succesfully!')
                break

            elif category == 'series':
                seasons = int(input('enter number of seasons:'))
                episodes = int(input('enter number of episodes:'))
                info_list = [id,name,category,imdb_rate,url,duration,cast,seasons,episodes]
                self.media_list.append(Series(info_list))
                print(f'{info_list[1]}added succesfully!')
                break 

            else:
                print('wrong info')
                break

        self.showmenu()

    def edit_media(self):
        
        input_id = input('first of all enter the id of the media:')  

        for i in self.media_list:
            
            # print('i:', i)
            # print(input_id,i.id)
            # print(len(self.media_list))

            if input_id == i.id:
                print('loading data...')

                if i.category == 'clip':
                   i =  i.edit_clips_info()
                    

                elif i.category == 'movie':                   
                   i = i.edit_movies_info()  


                elif i.category == 'anime':                    
                    i = i.edit_animes_info()
                                       
                elif i.category == 'series':                    
                    i= i.edit_series_info()

                else:
                    print('error!!wrong input!')


        else:
            print('this id doesnt exist in the media list!')

        self.showmenu()


    def delete_media(self):
        
        input_id = input('enter the id of the media you want to delete:')  

        for i in self.media_list:

            if input_id == i.id:
                
                self.media_list.remove(i)
                print('this item has been deleted succesfuly!')
                break

            else:
                print('error!!data not found!')


        self.showmenu()


    def search_media(self):
        pass

        # start_duration = input('enter the first duration:')
        # start_duration = start_duration.split(':')

        # end_duration = input('enter the second duration:')

        # for i in self.media_list:


    def save_and_exit(self):
        myfile = open('database.csv' , 'w')
        for i in self.media_list:
            if i.category == 'anime' or i.category == 'series':
                myfile.write(i.id + ',' + i.name + ',' + i.category + ',' + i.IMDB_rate + ',' + i.url + ',' + i.duration + ',' + i.casts + ',' + i.seasons + ',' + i.episodes)
            
            elif i.category == 'clip':
                myfile.write(i.id + ',' + i.name + ',' + i.category + ',' + i.IMDB_rate + ',' + i.url + ',' + i.duration + ',' + i.casts + ',' + i.concept + ',' + i.singer)
            
            elif i.category == 'movie':
                myfile.write(i.id + ',' + i.name + ',' + i.category + ',' + i.IMDB_rate + ',' + i.url + ',' + i.duration + ',' + i.casts + ',' + i.genre)
        
        if i != self.media_list[-1]:
                myfile.write('\n')

        print('your data has been saved succesfully :)')
        myfile.close()

        # self.show_info()
        # self.showmenu()
        

        
    def download_media(self):
        input_name = input('enter the media name to download:')
        for i in self.media_list:
            if i.name == input_name:
                i.downoad_media()
                print('downloading data')
        else:
            print(f'theres no media named {input_name}')

        self.showmenu()

    def showmenu(self):

        print('1-Add media' , '\n' ,'2-edit media' , '\n' ,'3-show info' , '\n' ,'4-delete' ,'\n' ,'5-search by duration', '\n' ,'6-show casts list', '\n' ,'7-download media' , '\n' ,'8-save and exit' )
        result = int(input('choose one of the options:'))
        if result == 1:
            self.add_media()
        elif result == 2 :
            self.edit_media()
        elif result == 3 :
            self.show_info()
        elif result == 4 :
            self.delete_media()
        elif result == 5:
            self.search_media()
        elif result == 6:
            self.show_casts_info()
        elif result == 7:
            self.download_media()
        elif result == 8:
            self.save_and_exit()
        else :
            print('error')

            
main = Main()
