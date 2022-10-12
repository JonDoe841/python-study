num_ppl = int(input())
num_nights = int(input())
num_cards = int(input())
num_billets = int(input())
night_price = num_nights * 20
card_price = num_cards * 1.60
billet_price = num_billets * 6
price = night_price + card_price + billet_price
group_price = price * num_ppl
final_price = group_price * 1.25
print(f"{final_price:.2f}")


