-- 코드를 입력하세요
-- 강남구에 위치한 가게의 아이디와 이름, 그리고 이 회사원이 가게에서 몇 번 결제를 했는 지 조회하는 SQL

-- merchants: 카드 가맹점 정보
-- card_usages: 회사원의 카드 사용 내역
SELECT m.id as "가게 ID",m.name as "NAME",count(*) as "결제 횟수" from (select id, name from merchants group by ID having name like "%강남%" or name like "%논현%") m join (select * from card_usages where category = 0) c on m.id = c.merchant_id group by c.merchant_id order by m.id;
