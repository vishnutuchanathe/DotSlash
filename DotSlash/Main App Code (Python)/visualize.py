import cv2
import numpy as np
import easygui    
from datetime import datetime
import string
import random
from alert import call
from model import class_names
from log import upload

def random_colors(N):
    np.random.seed(1)
    colors = [tuple(255 * np.random.rand(3)) for _ in range(N)]
    return colors


colors = random_colors(len(class_names))
class_dict = {
    name: color for name, color in zip(class_names, colors)
}


def apply_mask(image, mask, color, alpha=0.5):
    for n, c in enumerate(color):
        image[:, :, n] = np.where(
            mask == 1,
            image[:, :, n] * (1 - alpha) + alpha * c,
            image[:, :, n]
        )
    return image


def display_instances(image, boxes, masks, ids, names, scores):
    n_instances = boxes.shape[0]

    if not n_instances:
        print('NO INSTANCES TO DISPLAY')
    else:
        assert boxes.shape[0] == masks.shape[-1] == ids.shape[0]
    elephant = 0
    for i in range(n_instances):
        if not np.any(boxes[i]):
            continue
        y1, x1, y2, x2 = boxes[i]
        label = names[ids[i]]
        if(label != "elephant"):
            continue
        elephant = 1
        color = class_dict[label]
        score = scores[i] if scores is not None else None
        caption = '{} {:.2f}'.format(label, score) if score else label
        mask = masks[:, :, i]

        image = apply_mask(image, mask, color)
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        image = cv2.putText(
            image, caption, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2
        )
    if(elephant == 1):
        N = 4
        res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = N))
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        color = class_dict[label]
        img = cv2.putText(
            image, date_time, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2
        )
        cv2.imwrite('./logs/frame'+res+'.jpg', img)
        upload(img,res)
        call()
        easygui.msgbox("ELephants found at the border!!!", title="Alert")

    return image
