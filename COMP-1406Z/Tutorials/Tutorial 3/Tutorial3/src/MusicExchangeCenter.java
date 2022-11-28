import java.sql.Array;
import java.util.*;

public class MusicExchangeCenter {
    private ArrayList<User> users = new ArrayList<User>();

    private HashMap<String, Integer> royalties = new HashMap();

    private ArrayList<Song> downloadedSongs = new ArrayList<Song>();


    public ArrayList<User> onlineUsers() {
        ArrayList<User> onlineUsers = new ArrayList<User>();
        for (User user : users) {
            if (user.isOnline()) {
                onlineUsers.add(user);
            }
        }
        return onlineUsers;
    }

    public ArrayList<Song> getDownloadedSongs(){
        return downloadedSongs;
    }

    public ArrayList<Song> allAvailableSongs() {
        ArrayList<Song> availableSongs = new ArrayList<Song>();

        for (int i = 0; i < onlineUsers().size(); i++) {
            availableSongs.addAll(onlineUsers().get(i).getSongList());
        }

        return availableSongs;
    }

//    public ArrayList<Song> allAvailableSongs(){
//        ArrayList<Song> availableSongs = new ArrayList<Song>();
//
//        for (int i = 0; i < onlineUsers().size(); i++){
//            for (int j = 0; j < onlineUsers().get(i).getSongList().size(); j++ ){
//                availableSongs.add(onlineUsers().get(i).getSongList().get(j));
//            }
//        }
//
//        return availableSongs;
//    }

    public String toString() {
        return "Music Exchange Center (" + onlineUsers().size() + " users online, " + allAvailableSongs().size() + " songs available)";
    }

    public User userWithName(String s) {
        if (users.isEmpty()) {
            return null;
        }
        for (User user : users) {
            if (user.getUserName().equals(s)) {
                return user;
            }
        }
        return null;
    }

    public void registerUser(User x) {
        if ((userWithName(x.getUserName()) == null)) {
            users.add(x);
        }
    }

    public ArrayList<Song> availableSongsByArtist(String artist) {
        allAvailableSongs();
        ArrayList<Song> songsByArtist = new ArrayList<Song>();
        for (int i = 0; i < allAvailableSongs().size(); i++) {
            if (allAvailableSongs().get(i).getArtist().equals(artist)) {
                songsByArtist.add(allAvailableSongs().get(i));
            }

        }
        return songsByArtist;
    }

    public Song getSong(String title, String ownerName) {
        Song aSong = null;
        for (User user : users) {
            if ((user.getUserName().equals(ownerName)) && user.isOnline()) { // checks if user is the owner and if the user is online
                for (int j = 0; j < user.getSongList().size(); j++) {
                    if (user.getSongList().get(j).getTitle().equals(title)) {
                        aSong = user.getSongList().get(j);
                        downloadedSongs.add(aSong);
                        if (!(royalties.containsKey(aSong.getArtist()))) { // Adding to the royalties hashmap
                            royalties.put(aSong.getArtist(), 0);
                        }
                        royalties.put(aSong.getArtist(), royalties.get(aSong.getArtist()) + 1);
                    }
                }
            }
        }
        return aSong;
    }

    public void displayRoyalties(){
        System.out.println(String.format("%-15s%-9s", "Amount","Artist"));
        System.out.println("------------------------");
        for (HashMap.Entry<String, Integer> entry : royalties.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            Double payOut = value * 0.25;
            String valueString = String.format("%.02f", payOut);
            System.out.println(String.format("$%-14s%-9s", valueString, key));
        }

    }


    public TreeSet<Song> uniqueDownloads(){
        TreeSet<Song> uniqueSongs = new TreeSet<Song>();
        for (Song song: downloadedSongs){
            if (!(uniqueSongs.contains(song))){
                uniqueSongs.add(song);
            }
        }


    return uniqueSongs;
    }

    public ArrayList<Pair<Integer,Song>> songsByPopularity(){
        ArrayList<Pair<Integer, Song>> popularSongs = new ArrayList<Pair<Integer,Song>>();
        ArrayList<Song> duplicateSongs = new ArrayList<Song>();
        HashMap<Song,Integer> addedSongs = new HashMap<Song,Integer>();
        for (int i = 0; i < downloadedSongs.size(); i++){
            if (!(duplicateSongs.contains(downloadedSongs.get(i)))){
                popularSongs.add(new Pair(0, downloadedSongs.get(i)));
            }
            for (int j = 0; j < popularSongs.size(); j++){
                if (popularSongs.get(j).getValue().equals(downloadedSongs.get(i))){
                    popularSongs.set(j, new Pair(popularSongs.get(j).getKey()+ 1, popularSongs.get(j).getValue()));
                }
            }
            duplicateSongs.add(downloadedSongs.get(i));

        }
        // Commented out code for using a hashmap. I used another arraylist to check for duplicate songs instead.
//        for (Song song: downloadedSongs) {
//            if (!(addedSongs.containsKey(song))) {
//                addedSongs.put(song, 0);
//            }
//            addedSongs.put(song, addedSongs.get(song) + 1);
//        }
//        for (HashMap.Entry<Song, Integer> entry :addedSongs.entrySet()) {
//            Song key = entry.getKey();
//            Integer value = entry.getValue();
//            popularSongs.add(new Pair(value,key));
//                }

        Collections.sort(popularSongs, new Comparator<Pair<Integer, Song>>(){
            public int compare (Pair<Integer, Song> p1, Pair<Integer, Song> p2){
                return p2.getKey().compareTo(p1.getKey());
            }
        });



        return popularSongs;
    }

}