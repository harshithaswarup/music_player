# music_player
Question Summary:

- An MP3 app is to be created, which consists of songs  and  different users .
- At any point of time the user should be able to download song from the music app.
- A playlist should be created.
- At any instance we  should be able to add new artists.
- We must be able to add new songs to the MP3 player.
- The users should be able to download and delete songs from app.
- Song's rate must be set.


Music Player:


The following are possible in this app:

- View types of users (information about each type of user..)
- Login/Register
- View types of songs available and the artists names
- Download song
- Delete song
- View downloads
- Adding artists
- Adding songs
- Create playlist
- Delete song from playlist

The main class are:

1. Class MusicPlayer :

-The basic features  are its storage capacity,user information,downloads,
 songs list that are available to download.

- All the basic operations like login/sign-in,downloading,listening,creating playlist
  adding new songs,artists takes place in this class.

2. Class WynkUsers:

- The features  are the general features of a user like Login_Id,Login_password,
  types of user [Free / Subscribed / Premium].

3. Class WynkSongs:

- The main features are song name,song Id,song type,artist name,duration of the song,
  movie name,rate of the song,cost of the song and name of the actor.
 

Functions called when:

- To check if the member is new to the app or not.If aldready existing , 
  they can login directly

      - check_if_member()
      - login()

- If new to app:

      - get_registerd()
      -	select_membership_type()

- To download songs:

       - select_category()
       - search_song()
       - download_song()

- To create a playlist,

       - search_through_downloads()
       - add_to_playlist()

- To add an artist or song:

       - add_song()
       - add_artist()


Log File contains:

- The details of the user. (Login ID, Login Password and type of user)
- The downloaded songs from the app and number of songs that can be downloaded
- Playlist created
- Artists list
- Songs added to the app and its details
- Lists of songs after a deleting song
