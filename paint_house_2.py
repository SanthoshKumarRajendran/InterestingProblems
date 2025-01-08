# Leet Code - Problem 265 (Paint House II)
# https://leetcode.ca/all/265.html

###########################################################

import sys

house_count = 3
cost = [[1,5,3],[2,9,4],[6,7,8]]

LEAST_COST = sys.maxsize
LEAST_COST_COMBO = None

process_queue = []

for i in range(len(cost[0])):
    process_queue.append([[cost[0][i]], i])

while(process_queue):
    paint_combo_so_far, last_paint_num = process_queue.pop(0)

    if len(paint_combo_so_far) == house_count:
        if sum(paint_combo_so_far) < LEAST_COST:
            LEAST_COST = sum(paint_combo_so_far)
            LEAST_COST_COMBO = paint_combo_so_far
        continue

    next_house_num = len(paint_combo_so_far)
    for i in range(len(cost[0])):
        if i == last_paint_num:
            continue
        process_queue.append([paint_combo_so_far + [cost[next_house_num][i],], i])

print(LEAST_COST)
print(LEAST_COST_COMBO)
