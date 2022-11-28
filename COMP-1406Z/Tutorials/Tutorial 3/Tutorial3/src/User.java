import java.util.ArrayList;

public class User {
  private String     userName;
  private boolean    online;
  private ArrayList<Song>    songList; // Songs on the user's hard drive
  
  public User()  { this(""); }
  
  public User(String u)  {
    userName = u;
    online = false;
    songList = new ArrayList<Song>();
  }
  
  public String getUserName() { return userName; }
  public boolean isOnline() { return online; }
  
  public String toString()  {
    String s = "" + userName + ": " + songList.size() + " songs (";
    if (!online) s += "not ";
    return s + "online)";
  }

  public ArrayList<Song> getSongList() {
    return songList;
  }
  public void addSong(Song s)  {
    songList.add(s);
  }

  public int totalSongTime()  {
    int total = 0;
    for (Song s : songList)  {
      total += s.getDuration();
    }
    return total;
  }

  public void register(MusicExchangeCenter m)  {
    m.registerUser(this);
  }

  public void logon()  {
    online = true;
  }

  public void logoff()  {
    online = false;
  }
}
