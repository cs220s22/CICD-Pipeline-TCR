from flask import Flask
app = Flask(__name__)

def read_count():
    try:
        with open('count.txt', 'r') as f:
            count = int(f.read())
        return count
    except IOError:
        return 0


def save_count(count):
    with open('count.txt', 'w') as f:
        f.write(str(count))


@app.route("/")
def hello():
    count = read_count()    
    count += 1
    save_count(count);
    return "<h1 style='color:red'>Hello World! {}</h1>".format(count)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
