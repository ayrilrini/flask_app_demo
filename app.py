from flask import Flask, render_template, request

'''
创建Flask应用对象
__name__ 当前模块名
'''
app = Flask(__name__)


'''
@app.route("/") 是 Flask 的路由装饰器，表示访问网站根路径 / 时，调用 index() 函数
render_template("index.html") 会从 templates/index.html 中读取 HTML 内容并返回给浏览器
'''
@app.route("/")
def index():
    return render_template("index.html")


'''
这个路由处理 /hello 的 GET 请求,从URL查询参数中获取name的值
'''
@app.route("/hello")
def hello():
    name = request.args.get("name", "Stranger")
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
