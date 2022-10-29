def box_weight(box):
    if len(box) == 0:
        return 0
    if isinstance(box[0], list):
        return box_weight(box[0]) + box_weight(box[1:])
    if len(box) == 1:
        return box[0]
    return box[0] + box_weight(box[1:])
