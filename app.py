from flask import Flask, render_template
import random
app = Flask(__name__)
# list of dog images
images = [
        "https://images.dog.ceo/breeds/terrier-norwich/n02094258_2070.jpg",
        "https://images.dog.ceo/breeds/waterdog-spanish/20180723_185544.jpg",
        "https://images.dog.ceo/breeds/mountain-swiss/n02107574_97.jpg",
        "https://images.dog.ceo/breeds/dalmatian/cooper1.jpg",
        "https://images.dog.ceo/breeds/puggle/IMG_122350.jpg",
        "https://images.dog.ceo/breeds/appenzeller/n02107908_849.jpg",
        "https://images.dog.ceo/breeds/cattledog-australian/IMG_5177.jpg",
        "https://images.dog.ceo/breeds/dachshund/dachshund-1018409_640.jpg",
        "https://images.dog.ceo/breeds/terrier-border/n02093754_6248.jpg",
        "https://images.dog.ceo/breeds/terrier-scottish/n02097298_3780.jpg",
        "https://images.dog.ceo/breeds/borzoi/n02090622_8745.jpg",
        "https://images.dog.ceo/breeds/ovcharka-caucasian/IMG_20200206_195949.jpg",
        "https://images.dog.ceo/breeds/springer-english/n02102040_5283.jpg",
        "https://images.dog.ceo/breeds/dingo/n02115641_4265.jpg",
        "https://images.dog.ceo/breeds/pembroke/n02113023_4782.jpg"
]
@app.route('/')
def index():
        url = random.choice(images)
        return render_template('index.html', url=url)
if __name__ == "__main__":
        app.run(host="0.0.0.0")
