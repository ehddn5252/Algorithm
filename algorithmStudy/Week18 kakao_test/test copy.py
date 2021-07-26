import java.util.Hashtable;

class Solution {
    public int solution(int[] gift_cards, int[] wants) {
        

        Hashtable<Integer,Integer> gift_cards_h = new Hashtable<Integer, Integer>();
        Hashtable<Integer,Integer> wants_h = new Hashtable<Integer, Integer>();
        // wants_h의 key가 gift_cards_h에 없다면 0으로 세팅
        
        for(int i=0;i<wants.length;i++){
            // map에 없다면 0으로 세팅
            if(gift_cards_h.containsKey(wants[i])==false){
                gift_cards_h.put(wants[i],0);
            }
        }
        // gift_cards에 세팅하는 코드 
        for(int i=0;i<gift_cards.length;i++){
            // gift_cards_h에 없다면
            if (gift_cards_h.containsKey(gift_cards[i])==false){
                gift_cards_h.put(gift_cards[i],1);
            }
            // 있다면 
            else{
                gift_cards_h.put(gift_cards[i],gift_cards_h.get(gift_cards[i])+1);
            }
        }
        // wants 세팅
        for(int i=0;i<wants.length;i++){
            if(wants_h.containsKey(wants[i])==false){
                wants_h.put(wants[i],1);
            }
            else{
                wants_h.put(wants[i],wants_h.get(wants[i])+1);
            }
        }

        int answer=0;
        int wants_value=0;
        int gift_cards_value=0;
        // wants와 giftcard 비교해서

        for(int i=0;i<wants.length;i++){
            wants_value=wants_h.get(wants[i]);
            gift_cards_value=gift_cards_h.get(wants[i]);
            System.out.println("====");
            System.out.println(wants_value);
            System.out.println(gift_cards_value);
            if(wants_value>gift_cards_value){
                answer+=wants_value-gift_cards_value;
            }
        }
        
        return answer;
    }
}