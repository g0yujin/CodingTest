import java.util.*;
import java.io.*;

public class Main {
    static PriorityQueue<Node> q = new PriorityQueue<>();
    static ArrayList<Node>[] graph;
    static boolean[] visit;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        int[] d = new int[V+1];
        Arrays.fill(d, Integer.MAX_VALUE);
        d[K] = 0;

        visit = new boolean[V+1];
        graph = new ArrayList[V+1];
        for(int i = 0; i<=V; i++) {
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i<E; i++) {
            st = new StringTokenizer(br.readLine());
            graph[Integer.parseInt(st.nextToken())].add(new Node(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        q.add(new Node(K, 0));

        while(!q.isEmpty()) {
            Node cur = q.remove();
            if(!visit[cur.x]) {
                visit[cur.x] = true;
                for(Node n : graph[cur.x]) {
                    if(d[n.x] > d[cur.x] + n.w) {
                        d[n.x] = d[cur.x] + n.w;
                        q.add(new Node(n.x, d[n.x]));
                    }
                }
            }
        }

        for(int i = 1; i<d.length; i++) {
            if(d[i] == Integer.MAX_VALUE) sb.append("INF\n");
            else sb.append(d[i]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();

    }

    static class Node implements Comparable<Node> {
        int x;
        int w;

        public Node(int x, int w) {
            this.x = x;
            this.w = w;
        }

        public int compareTo(Node o) {
            return w - o.w;
        }
    }
}