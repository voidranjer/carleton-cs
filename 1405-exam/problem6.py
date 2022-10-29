def box_weight(box):
    if len(box) == 0:
        return 0
    if len(box) == 1:
        if isinstance(box[0], list):
            return box_weight(box[0]) + box_weight(box[1:])
        return box[0]

    if isinstance(box[0], list):
        return box_weight(box[0]) + box_weight(box[1:])

    return box[0] + box_weight(box[1:])


print(box_weight([2, 1, [[4], 2, [9, 7]], 2,
      [1, 3, [1, [2], [3]], [9], [], 4]]))
