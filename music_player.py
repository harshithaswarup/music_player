import logging
import re
logging.basicConfig(filename='music.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
       

class WynkUser:
    def __init__(self,user_name,user_ID,user_type):
        self.user_name = user_name
        self.user_ID = user_ID
        self.user_type = user_type

class WynkSongs:
    def __init__(self,song_name,song_ID,song_rate,singer_name,language,actor_name,movie_name,song_duration,song_type,song_cost):
        self.song_name = song_name
        self.song_ID = song_ID
        self.song_rate = song_rate                                
        self.singer_name = singer_name
        self.language = language
        self.actor_name = actor_name
        self.movie_name = movie_name
        self.song_duration = song_duration
        self.song_type = song_type
        self.song_cost = song_cost



class MusicPlayer(object):
    def __init__(self,max_download_limit,space,app_rating,account_holder_name,holder_ID,user_type,my_music,local_mp3,languages,no_of_downloaded_songs,types_of_users,artists,songs,song_type,playlist):
        self.max_download_limit = max_download_limit    # Maximum number of songs that can be downloaded or max space of the app
        self.space = space                              # Space available after each download
        self.app_rating = app_rating                    # Rating given for the app        
        self.account_holder_name = account_holder_name
        self.holder_ID = holder_ID
        self.user_type = user_type                      # The type of user, Free,premium or subscribed             
        self.my_music = my_music                        # Songs downloaded from the app       
        self.local_mp3 = local_mp3                      # Songs added to the app from the other source        
        self.languages = languages                              
        self.no_of_downloaded_songs = no_of_downloaded_songs
        self.types_of_users = types_of_users            # Free/Premium/Subscribed            
        self.artists = artists
        self.songs = songs                              # Songs available in the app to download                                   
        self.song_type = song_type                              
        self.playlist = playlist                        # List created as the song gets played / clicked
        

    ' The following functions are to either login or register into the app..'   

    """ The user is asked if he/she is an existing member.
        If member he/she can just login with the registered name and ID.
        The the user name and user ID are validated. """

    def check_if_member(self,member):
        membership = ['yes','no']
        if(member == 'no'):
            return member

    def login(self,user_name,user_ID):
        if(user_name == user1.user_name and user_ID == user1.user_ID): # If member,the given user name and ID is matched with the registered name and ID
            return user_name,user_ID
        else:
            return False

    def check_user_name(self,user_name):
        if re.match("^[A-Z]{1}[a-z]{5}",user_name):      # The user name is validated
            return True
        else:
            return False

    def check_user_ID(self,user_ID):
        if re.match("^[WYNK]{4}[0-9]{2}",user_ID):      # The user ID is validated
            return True
        else:
            return False
    

    """ If the person is new to the app,he/she should sign in and select the type of member.
         The user name and password is set which is then validated"""
                           
    def get_registerd(self,user_name,user_password):
        if(len(user_name) == 5 and len(user_password) == 5):   # The user's name and user's password must be of length 5 
            return user_name,user_password
        else:
            return False

    def check_signin_name(self,user_name):
        if re.match("^[A-Z]{1}[a-z]{4}",user_name):             # The sign in  name is validated
            return True
        else:
            return False
        
    def check_signin_password(self,user_password):
        if re.match("^[a-z]{3}[!]{1}[*]{1}",user_password):   # The  Password is validated
            return True 
        else:
            return False
        

    def select_membership_type(self,member_type):
        if(member_type in self.types_of_users):               # The user is asked to select the type of user..Free,subscribed or Premium            
            return member_type
        else:
            return False
        

    ' The following set of functions are to download the song from the app..'
        
    ''' Songs are available under different categories.
        The user is asked to select any one to download'''
    
    def select_category(self,category):
        for keys in self.songs:
            if(category == keys):        # The selected category is matched with the all the available categories                              
                return True
            
                
    """ The list of songs available under the selected category gets displayed.
        The user searches for the song to download and if the song is available.
        it is added to the downloads list.
        The remaining space available to download is returned"""
    
    def search_song(self,song_title):
        for keys in self.songs:
            for song in self.songs[keys]:
                if(song_title == song):    # The searched song is matched with the available list of songs.                             
                    return song_title

    def download_song(self,song_title):
        if song_title in self.my_music:
            return self.my_music
        else:
            self.my_music.append(song_title)   # The song is added to the list of downloads.                     
            return self.my_music

    def delete_song(self,song_name):
        try:
            if song_name in self.my_music:
                self.my_music.remove(song_name)  # The song is deleted from the music app
                print self.my_music
        except ValueError:
            return self.my_music
    

    def get_available_space(self):
        self.space = (self.max_download_limit)-(len(self.my_music))   # The remaining space available to download or number of songs that can be downloaded
        return self.space
            
                
       

    ' The following functions are to add the songs into the playlist'        

    """ The user  searches for the song to listen..as he/she clicks the song ,a playlist will get created.
        The songs will get into repeat mode. """
        
    def search_through_downloads(self,song_track):
        if song_track in self.my_music:                            # If the searched song is there in downloads, it gets returned
            return song_track
        
        
    def add_to_playlist(self,song_track):
        if song_track in self.playlist:                       # The  song gets added to the playlist    
            return self.playlist
        else:
            self.playlist.append(song_track)
            return self.playlist
            


    def delete_from_playlist(self,song_track):
        try:
            if song_track in self.playlist:                       # The song is removed from the playlist, if present
                self.playlist.remove(song_track)
                return self.playlist
        except ValueError:
            return self.playlist
          


    """ The new song is added to the music app.
        The details of the song are matched with the categories(keys).
        If they match, the song will get added respectively
        or a new key-value pair will get created."""

    def add_song(self,song_title,artist_name,movie_name,actor_name,song_language,song_cost):
        new_song_list = []
        new_song_list.append(song_title)     # New songs are added to the list.
        for keys in self.songs:
            if(artist_name == keys or movie_name == keys or actor_name == keys or song_language == keys):
                if (artist_name or actor_name or movie_name or song_language in keys):
                    self.songs[keys].extend(new_song_list)  # The song list is then appended to the respective keys of the dict      
                    return self.songs
            else:
                self.songs.update(dict.fromkeys([artist_name,movie_name,actor_name,song_language],new_song_list))  # A new key-value pair is generated 
                return self.songs
            

    ' The function is used to add an artist to the existing artist list'

    def add_artist(self,artist_name):
        if artist_name in self.artists:                       # If the name of the artist aldready exists,the same old list gets returned    
            return self.artists                                 
        else:
            self.artists.append(artist_name)                  # Artists name gets added to the list           
            return self.artists

   


user1 = WynkUser('Harshi','WYNK08','premium')
wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)


if __name__=='__main__':

    process = True
              
    
    while process:
        print('press 0 to view membership plans')
        print('press 1 to login/register')
        print('press 2 to view the types of songs  and the songs available in the app')
        print('press 3 to download songs')
        print('press 4 to delete from downloads')
        print('press 5 to view downloads')
        print('press 6 to add an artist')
        print('press 7 to add a song')
        print('press 8 to add playlist')
        print('press 9 to delete song from playlist')
        print('press 10 to exit')

        choice = int(input("Enter your choice"))

        if(choice == 0):
            print wynk.types_of_users
            member_type = raw_input("select the type of member:")
            if(member_type == wynk.types_of_users[0] ):
                print "Unlimited downloads..!! Add Free Songs..!! @ just Rs 99 only..!!!...special rate for airtel users..@ Rs 49..!!"
            elif(member_type == wynk.types_of_users[1]):
                print " Free and Unlimited downloads for all AIRTEL users...!!!"
            else:
                print "The unlimited streams and downloads (Rs.50) but 'FREE' till march 2019"


        
        elif(choice == 1):
            member = raw_input("Are you new to wynk?:")
            if(member == 'no'):
                member=wynk.check_if_member(member)
                user_name = raw_input("Enter the user name:")
                user_ID = raw_input("Enter your user ID:")
                user_name,user_ID=wynk.login(user_name,user_ID)
                if(user_name == user1.user_name and user_ID == user1.user_ID):
                    wynk.check_user_name(user_name)
                    if re.match("^[A-Z]{1}[a-z]{5}",user_name):
                        wynk.check_user_ID(user_ID)
                        if re.match("^[WYNK]{4}[0-9]{2}",user_ID):
                            print "Welcome to Wynk World of music...!!!!"
                else:
                    print "Invalid username and ID...!!"

            else:
                print "Please do register...!!"
                user_name = raw_input("Set the user name:")
                user_password = raw_input("Set your password:")
                user_name,user_password = wynk.get_registerd(user_name,user_password)
                member_type = raw_input("select the type of member:")
                wynk.check_signin_name(user_name)
                if re.match("^[A-Z]{1}[a-z]{4}",user_name):
                    wynk.check_signin_password(user_password)
                    if re.match("^[a-z]{3}[!]{1}[*]{1}",user_password):
                        print "You have successfully registered..!! Welcome to WYNK..!!"
                        logging.info("The user name,user password and user_type are: %s %s %s",user_name,user_password,member_type)              
                else:
                    print "Invalid user name and password..!!"
                wynk.select_membership_type(member_type)
                   
        elif(choice == 2):
            print "The types of songs available are : %s",wynk.song_type
            for keys in wynk.songs:
                print "The available songs in the app are :%s", wynk.songs[keys]


        elif(choice == 3):
            print "Search song from:",wynk.songs
            category = raw_input("Enter the category from which you want to download:")
            wynk.select_category(category)
            for keys in wynk.songs:
                if(category == keys):
                    print wynk.songs[keys]
            song_title = raw_input("Search song:")
            song_title = wynk.search_song(song_title)
            if song_title in wynk.my_music:
                print "Aldready downloaded..!!"
            if(song_title == song):
                print "The song is available to download !!"
            else:
                print "No results found...!!"
            wynk.download_song(song_title)
            wynk.get_available_space()
            logging.info("The downloaded songs are :%s",wynk.my_music)
            logging.info("The number of songs that can be downloaded are : %s",wynk.space)

        elif(choice == 4):
            song_name = raw_input("Enter the name of the song to delete:")
            wynk.delete_song(song_title)
            logging.info("The downloads are: %s",wynk.my_music)
            logging.info("The number of songs that can be downloaded are : %s",wynk.space)

        elif(choice == 5):
            logging.info("The downloaded songs are :%s",wynk.my_music)


        elif(choice == 6):
            artist_name = raw_input("Enter the name of the artist")
            if artist_name in wynk.artists:
                print "Artist name aldready exists..!!"
            wynk.add_artist(artist_name)
            logging.info("The artists available are : %s",wynk.artists)

        elif(choice == 7):
            song_title = raw_input("Enter the name of the song to be added:")
            artist_name = raw_input("Enter the name of the artist")
            movie_name = raw_input("Enter the name of the movie:")
            actor_name = raw_input("Enter the name of the actor:")
            song_language = raw_input("Enter the language of the song:")
            song_cost = int(input("Enter the cost of the song:"))
            wynk.add_song(song_title,artist_name,movie_name,actor_name,song_language,song_cost)
            logging.info("Available songs are: %s",wynk.songs)
            logging.info("The details of the song  are: %s %s %s %s %s %s",song_title,artist_name,movie_name,actor_name,song_language,song_cost)

        elif(choice == 8):
            print "The available songs are:",wynk.my_music
            song_track = raw_input("Enter the song you want to listen to:")
            if song_track not in wynk.my_music:
                print "The song is not available"
            song_track = wynk.search_through_downloads(song_track)
            print "The currently playing song is :",song_track
            if song_track in wynk.playlist:
                print "song aldready added..!"
            wynk.add_to_playlist(song_track)
            logging.info("The playlist is :%s",wynk.playlist)

        elif(choice == 9):
            sound_track=raw_input("Enter the song to be removed:")
            wynk.delete_from_playlist(sound_track)
            logging.info("The playlist after removing the song: %s", wynk.playlist)


        else:
            process = False
            
            



        
    
    
