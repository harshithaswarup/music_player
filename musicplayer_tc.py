import unittest
from music_player import WynkUser
from music_player import WynkSongs
from music_player import MusicPlayer

class TestString(unittest.TestCase):
    def test_check_if_member(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.check_if_member('yes')
        self.assertEqual(check,None)
    
        
    def test_check_username(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check  = wynk.check_user_name('Harshi')
        self.assertEqual(check,True)

    def test_check_user_name(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check  = wynk.check_user_name('hARSHI')
        self.assertNotEqual(check,True)

    def test_user_ID(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.check_user_ID('WYNK08')
        self.assertEqual(check,True)

    def test_userid(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.check_user_ID('wynk08')
        self.assertNotEqual(check,True)

    def test_login_name(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.check_signin_name('Harsh')
        self.assertNotEqual(check,False)

    
    def test_user_login(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.check_signin_name('haRsH')
        self.assertEqual(check,False)

    def test_user_password(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.check_signin_password('ABC!*')
        self.assertNotEqual(check,True)
        

    def test_member2(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.select_membership_type('Free')
        self.assertEqual(check,'Free')
        
    def test_member3(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.select_membership_type('Free')
        self.assertNotEqual(check,'Premium')

    def test_artist(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        artist = wynk.add_artist('Karthik')
        self.assertEqual(artist,['Anirudh','ARR','Ankit Tiwari','Karthik'])

    def test_artists(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        artist = wynk.add_artist('ARR')
        self.assertNotEqual(artist,['Anirudh','ARR','Ankit Tiwari','Karthik'])


    def test_add_palylist(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        song = wynk.add_to_playlist('Pachai Nirame')
        self.assertEqual(song,['Pachai Nirame'])

    def test_create_palylist(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        song = wynk.add_to_playlist('Pachai Nirame')
        self.assertNotEqual(song,['Mazhai kuruvi'])

    def test_delete_song(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],['Pachai Nirame'])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        song_list= wynk.delete_from_playlist('Pachai Nirame')
        self.assertEqual(song_list,[])

    def test_remove_song(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],['Pachai Nirame'])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        song_list= wynk.delete_from_playlist('Mazhai Kuruvi')
        self.assertEqual(song_list,None)

    def test_remove_song(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        song_list= wynk.delete_from_playlist('Mazhai Kuruvi')
        self.assertEqual(song_list,None)

    def test_login(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.login('Harshi','WYNK08')
        self.assertEqual(check,('Harshi','WYNK08'))

    def test_loginn(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.login('Harshi','wynk08')
        self.assertNotEqual(check,('Harshi','WYNK08'))
    

class TestString1(unittest.TestCase):
    def test_select_category(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.select_category('Anirudh')
        self.assertEqual(check,True)

    def test_choose_category(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        check = wynk.select_category('karthik')
        self.assertEqual(check,None)

    def test_search_song(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        search = wynk.search_song('Barish')
        self.assertEqual(search,'Barish')

    def test_search_songs(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        search = wynk.search_song('Raanjhna')
        self.assertNotEqual(search,'VIP')

    def test_download_song(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        downloads = wynk.download_song('Yaanji')
        self.assertEqual(downloads,['Pachai Nirame','Yaanji'])

    def test_delete_songs(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        download = wynk.delete_song('VIP')
        self.assertNotEqual(download, ['Pachai Nirame'])

    def test_add_song(self):
        wynk = MusicPlayer(10,9,4,'Harshi','WYNK08','premium',['Pachai Nirame'],['descpasito'],['Tamil','Hindi','English'],1,['Premium','Free','Subscribed'],['Anirudh','ARR','Ankit Tiwari'],{'Anirudh':['Yaanji','VIP'],'Dhanush':['Maruvarthai','Vada chennai','Visiri'],'Hindi':['ADHM','Dekthe','Barish']},['Nostalgic','Love','English'],[])                 
        song = WynkSongs('mazhai kuruvi','MK',4,'ARR','Tamil','STR','CCV','5 mins','xx',10)
        downloads = wynk.add_song('cheap thrills','Sia','album','Sia','English',10)
        self.assertEqual(downloads,{'album': ['cheap thrills'], 'Sia': ['cheap thrills'], 'Dhanush': ['Maruvarthai', 'Vada chennai', 'Visiri'], 'Hindi': ['ADHM', 'Dekthe', 'Barish'], 'Anirudh': ['Yaanji', 'VIP'], 'English': ['cheap thrills']})
      
if __name__=='__main__':
    unittest.main()


