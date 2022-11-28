import java.util.ArrayList;

public class User {
  private String     userName;
  private boolean    online;
  private ArrayList<Song> songList;

  
  public User()  {this("" ); }

  public User(String u)  {
    userName = u;
    online = false;
    songList = new ArrayList<Song>();
  }

  public String getUserName() { return userName; }
  public boolean isOnline() { return online; }
  public ArrayList<Song> getSongList() {return songList; }
  
  public String toString()  {
    String s = "" + userName + ": "  + songList.size() + " songs (";
    if (!online) s += "not ";
    return s + "online)";
  }

  public void addSong (Song s){
    songList.add(s);
    if (s.getOwner() == null){
      s.setOwner(this);
    }

  }

  public int totalSongTime(){
    int totalTime;
    totalTime = 0;
    for (Song song : songList) {
      totalTime += song.getDuration();
    }
    return totalTime;

  }

  public void register(MusicExchangeCenter m) {
    m.registerUser(this);
  }

  public void logon(){
    this.online = true;
  }
  public void logoff(){
    this.online = false;
  }

  public ArrayList<String> requestCompleteSonglist(MusicExchangeCenter m){
    ArrayList<String> songList = new ArrayList<String>();
    ArrayList<Song> songs = m.allAvailableSongs();
    songList.add(String.format("%2s%-30s%-15s%-7s%-3s","   ", "TITLE", "ARTIST", "TIME", "OWNER"));
    for (int i = 0; i < songs.size();i++ ){
      String s = String.format("%02d", songs.get(i).getDuration()%60);

      songList.add(String.format("%2s.%-30s%-15s%-7s%-3s", (i+1), songs.get(i).getTitle(), songs.get(i).getArtist(), (songs.get(i).getDuration() / 60) + ":" + s, songs.get(i).getOwner().getUserName()));

    }

    return songList;
  }

  public ArrayList<String> requestSonglistByArtist(MusicExchangeCenter m, String artist){
    ArrayList<String> songList = new ArrayList<String>();
    ArrayList<Song> songs = m.allAvailableSongs();
    int count = 0;
    for (Song song : songs) {
      if (song.getArtist().equals(artist)) {
        count += 1;
        String s = String.format("%02d", song.getDuration() % 60);
        songList.add(String.format("%2s.%-30s%-15s%-7s%-3s", (count), song.getTitle(), song.getArtist(), (song.getDuration() / 60) + ":" + s, song.getOwner().getUserName()));

      }
    }

      return songList;
  }

  public void downloadSong(MusicExchangeCenter m, String title, String ownerName){
    Song newSong = m.getSong(title, ownerName);
    if (newSong != null){
      this.addSong(newSong);
    }
  }

}
