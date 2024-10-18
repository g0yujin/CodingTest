import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        Map<String,List<Node>> map = new HashMap<>();

        for(int i=0; i<genres.length; i++) {
            map.computeIfAbsent(genres[i], k -> new ArrayList<>()).add(new Node(i, plays[i]));
        }

        //장르별 총 재생횟수
        Map<String,Integer> sortedMap = new HashMap<>();
        for(Map.Entry<String,List<Node>> entry : map.entrySet()) {
            int sum = 0;
            for(Node node : entry.getValue()) {
                sum += node.count;
            }
            sortedMap.put(entry.getKey(), sum);
        }

        List<String> keys = new ArrayList<>(map.keySet());
        keys.sort((v1,v2) -> sortedMap.get(v2).compareTo(sortedMap.get(v1)));


        //장르 내 노래 정렬
        int i = 0;
        List<Integer> res = new ArrayList<>();
        for(String key : keys) {
            List<Node> nodeList = map.get(key);
            Collections.sort(nodeList);

            res.add(nodeList.get(0).x);
            if(nodeList.size() > 1) res.add(nodeList.get(1).x);

        }

        answer = res.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
    
}

class Node implements Comparable<Node> {
    int x; //고유번호
    int count; //재생횟수

    public Node(int x, int count) {
        this.x = x;
        this.count = count;
    }

    public int compareTo(Node o) {
        if(this.count == o.count) {
            return this.x - o.x;
        }
        return o.count - this.count;
    }

}