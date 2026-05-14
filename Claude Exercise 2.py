#this base works now - to enumerate (dont concern you here Claude hehe, these are my notes.)
# learned and used dictionaries
# learned more on nested conditionals and indentations.
# dictionary and append is in loop which helps make each trade its own list instead of compiled or the last only
# journaled.
# enumerate:
# The 1 at the end just tells Python to start counting from 1 instead of 0.
# That number on the left — 1, 2, 3 — that's index (it can be named anything).
# The current issue is that the ran program enumerates repetitively and not each individual trade.

trade_amount = int(input('How many trades do you want to log: '))

journal_list = []
win = 0
break_even = 0
loss = 0

for x in range(trade_amount):
	pair = input('Currency pair: ')
	direction = input('Buy or sell: ').upper()
	entry = float(input('Entry price: '))
	exit_price = float(input('Exit price: '))

	buy_profit = exit_price - entry
	sell_profit = entry - exit_price

	if direction == 'BUY' and buy_profit > 0:
		win = win + 1
		print('Win')
	elif direction == 'BUY' and buy_profit == 0:
		break_even = break_even + 1
		print('Break-even')
	elif direction == 'BUY' and buy_profit < 0:
		loss = loss + 1
		print('Loss')
	if direction == 'SELL' and sell_profit > 0:
		win = win + 1
		print('Win')
	elif direction == 'SELL' and sell_profit == 0:
		break_even = break_even + 1
		print('Break-even')
	elif direction == 'SELL' and sell_profit < 0:
		loss = loss + 1
		print('Loss')

	result = ''
	if direction == 'BUY' and buy_profit > 0:
		result = 'Win ✅'
	elif direction == 'BUY' and buy_profit == 0:
		result = 'Break-even ⚖️'
	elif direction == 'BUY' and buy_profit <0:
		result = 'Loss ❌'
	if direction == 'SELL' and sell_profit > 0:
			result = 'Win ✅'
	elif direction == 'SELL' and sell_profit == 0:
			result = 'Break-even ⚖️'
	elif direction == 'SELL' and sell_profit < 0:
			result = 'Loss ❌'

	trade = {
		'Pair' : pair,
		'Entry' : entry,
		'Exit' : exit_price,
		'Direction' : direction,
		'Result' : result
	}
	journal_list.append(trade)

for index, trade in enumerate(journal_list, 1):
	print(index, trade)

win_rate = win / trade_amount * 100


print('-------- Trade Journal --------')
print(f'Total trades: {trade_amount}')
print(f'Wins: {win}')
print(f'Break-even: {break_even}')
print(f'Losses: {loss}')
print(f'Win rate: {win_rate} ')