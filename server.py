from flask import Flask, json, request, render_template
import os
import csv
import math
import random
json_file = "images.json"

api = Flask(__name__, template_folder='templates')

@api.route('/img_history', methods=['POST'])
def img_history():
    global image_history
    image_history = []
    if request.json:
        selected_images = request.json['selectedImages']
        with open('images.json') as json_file:
            image_history = json.load(json_file)['img_history'] + selected_images
        os.remove("images.json")
        with open('images.json', 'w') as json_file:
            json.dump({'img_history': image_history}, json_file)
    

    user_interested_clusters = {}
    total_user_interested_items = len(image_history)
    products_by_clusters = {}
    with open('img_clusters.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            img = row[0]
            cluster = row[1]
            if cluster not in products_by_clusters.keys():
                products_by_clusters[cluster] = []
            products_by_clusters[cluster].append(img)
            if img in image_history:
                if cluster not in user_interested_clusters.keys():
                    user_interested_clusters[cluster] = 0
                user_interested_clusters[cluster] += 1

    img_recommended = []
    for cluster in user_interested_clusters.keys():
        try:
            no_items_recommend = math.ceil(user_interested_clusters[cluster]*20/total_user_interested_items)
            img_recommended = img_recommended + random.sample(products_by_clusters[cluster], no_items_recommend)
        except:
            img_recommended = img_recommended + products_by_clusters[cluster]
    
    return json.dumps({'img_recommended': img_recommended})

@api.route('/', methods=['GET'])
def render_static():
    return render_template('./test.html')

if __name__ == '__main__':
    api.run()
