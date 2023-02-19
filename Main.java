import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> line1 = Arrays.stream(br.readLine().split(" ")).map(x -> Integer.parseInt(x))
                .collect(Collectors.toList());
        List<Integer> line2 = Arrays.stream(br.readLine().split(" ")).map(x -> Integer.parseInt(x))
                .collect(Collectors.toList());
        int B = line2.get(0);
        int C = line2.get(1);

        System.out.println(line1.stream().map(x -> {
            if (x == 0)
                return 0;
            int remain = x - B;
            if (remain <= 0)
                return 1;
            int count = remain % C == 0 ? remain / C : remain / C + 1;
            return count + 1;
        }).reduce((a, b) -> a + b).get());
    }
}