class Solution {
    public int solution(int[] gift_cards, int[] wants) {
        int answer=0;
        int gc_l=gift_cards.length;
        int w_l=wants.length;
        int[] gc_a=new int[gc_l+1];
        //Arrays.fill(gc_a, 0);
        int[] w_a=new int[w_l+1];
        //Arrays.fill(w_a, 0);
        for(int i=0;i<gc_l;++i){
            gc_a[gift_cards[i]]+=1;
            w_a[wants[i]]+=1;
        }
        for(int i=0;i<gc_l;++i){
            if(w_a[i]>gc_a[i]){
                answer+=w_a[i]-gc_a[i];
            }
        }
   return answer;
    }
}