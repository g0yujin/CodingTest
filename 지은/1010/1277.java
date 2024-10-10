import java.util.*;
import java.io.*;

public class Main {
    static PriorityQueue<Point> pq = new PriorityQueue<>();
    static double[][] graph;
    static Point[] points;
    static Point[] distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        double M = Double.parseDouble(br.readLine());

        //발전소 위치 저장
        points = new Point[N +1];
        for(int i = 1; i<= N; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            points[i] = new Point(i,r,c);
        }

        //거리 저장
        graph = new double[N+1][N +1];
        for(double[] g : graph) Arrays.fill(g, Double.MAX_VALUE);

        for(int i=1; i<=N; i++) {
            Point p1 = points[i];
            for(int j=1; j<=N; j++) {
                if(i == j) graph[i][j] = 0;
                else {
                    Point p2 = points[j];
                    double d = p1.getDistance(p2);
                    if(d<=M) graph[i][j] = graph[j][i] = d;
                }
            }
        }

        //연결 정보를 바탕으로 업데이트
        for(int i=1; i<=W; i++) {
            st = new StringTokenizer(br.readLine());
            int p1 = Integer.parseInt(st.nextToken());
            int p2 = Integer.parseInt(st.nextToken());
            graph[p1][p2] = graph[p2][p1] = 0;
        }

        distance = new Point[N+1];
        dijkstra();

        bw.write(String.valueOf((int) (distance[N].w*1000)));
        bw.flush();
        bw.close();

    }

    static void dijkstra() {
        for(int i = 1; i<distance.length; i++) {
            Point p = new Point(i,Double.MAX_VALUE);
            if(i == 1) {
                p.w = 0;
                pq.add(p);
            }
            distance[i] = p;
        }

        while(!pq.isEmpty()) {
            Point cur = pq.remove();
            for(int i = 1; i<distance.length; i++) {
                if(graph[cur.x][i] != Double.MAX_VALUE && distance[i].w > distance[cur.x].w + graph[cur.x][i]) {
                    distance[i].w = distance[cur.x].w + graph[cur.x][i];
                    pq.add(distance[i]);
                }
            }
        }
    }

    static class Point implements Comparable<Point> {
        int x;
        int c;
        int r;
        double w;

        public Point(int x, int r, int c) {
            this.x = x;
            this.r = r;
            this.c = c;
        }

        public Point(int x, double w) {
            this.x = x;
            this.w = w;
        }

        public double getDistance(Point p) {
            return Math.sqrt(Math.pow(this.r - p.r,2) + Math.pow(this.c - p.c,2));
        }

        public int compareTo(Point o) {
            return Double.compare(this.w, o.w);
        }
    }
}