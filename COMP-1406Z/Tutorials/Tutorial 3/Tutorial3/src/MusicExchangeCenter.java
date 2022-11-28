import java.util.ArrayList;

public class MusicExchangeCenter {
    private ArrayList<User> users;

    public MusicExchangeCenter() {
        users = new ArrayList<User>();
    }

    public ArrayList<User> onlineUsers() {
        ArrayList<User> onlineUsers = new ArrayList<User>();
        for (User user : users) {
            if (user.isOnline()) {
                onlineUsers.add(user);
            }
        }
        return onlineUsers;
    }

    public ArrayList<Song> allAvailableSongs() {
        ArrayList<Song> availableSongs = new ArrayList<Song>();
        for (User user : onlineUsers()) {
            availableSongs.addAll(user.getSongList());
        }
        return availableSongs;
    }

    public String toString() {
        return "Music Exchange Center (" + onlineUsers().size() + " users on-line, " + allAvailableSongs().size() + " songs available)";
    }

    public User userWithName(String s) {
        for (User user : users) {
            if (user.getUserName().equals(s)) {
                return user;
            }
        }
        return null;
    }

    public void registerUser(User x) {
        if (userWithName(x.getUserName()) == null) {
            users.add(x);
        }
    }

    public ArrayList<Song> availableSongsByArtist(String artist) {
        ArrayList<Song> availableSongs = new ArrayList<Song>();
        for (Song song : allAvailableSongs()) {
            if (song.getArtist().equals(artist)) {
                availableSongs.add(song);
            }
        }
        return availableSongs;
    }
}

