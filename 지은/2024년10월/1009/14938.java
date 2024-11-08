import java.util.*;
import java.io.*;

public class Main {
    static PriorityQueue<Node> q = new PriorityQueue<>();
    static ArrayList<Node>[] graph;
    static int[] item;
    static boolean[] visit;
    static int[] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        item = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=n; i++) {
            item[i] = Integer.parseInt(st.nextToken());
        }

        graph = new ArrayList[n+1];
        for(int i = 0; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }

        for(int i=1; i<=r; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a].add(new Node(b,c));
            graph[b].add(new Node(a,c));
        }

        distance = new int[n+1];
        visit = new boolean[n+1];

        int res = 0;
        for(int i=1; i<=n; i++) {
            res = Math.max(res,dijkstra(i, m));
        }


        bw.write(String.valueOf(res));
        bw.flush();
        bw.close();

    }

    static int dijkstra(int start, int scope) {
        Arrays.fill(distance, Integer.MAX_VALUE);
        Arrays.fill(visit, false);
        distance[start] = 0;

        q.add(new Node(start,0));
        while(!q.isEmpty()) {
            Node cur = q.remove();
            if(!visit[cur.x]) {
                visit[cur.x] = true;
                for(Node n : graph[cur.x]) {
                    if(distance[n.x] > distance[cur.x] + n.w) {
                        distance[n.x] = distance[cur.x] + n.w;
                        q.add(new Node(n.x,distance[n.x]));
                    }
                }
            }

        }

        int res = 0;
        for(int i = 1; i<distance.length; i++) {
            if(distance[i] <= scope) {
                res += item[i];
            }
        }

        return res;


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