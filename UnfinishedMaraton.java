import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class UnfinishedMaraton {

    public String solution(String[] participant, String[] completion) {
        List<String> listParticipant = new ArrayList<>(Arrays.asList(participant));
        List<String> listCompletion = new ArrayList<>(Arrays.asList(completion));

        for(String c : listCompletion) {
            listParticipant.remove(c);
        }

        return listParticipant.get(0);
    }

    public static void main(String[] args) {
        String[] p = {"kiki", "kiki", "eden"};
        String[] c = {"eden", "kiki"};

        UnfinishedMaraton m = new UnfinishedMaraton();
        String result = m.solution(p, c);
        System.out.println(result);
    }
}