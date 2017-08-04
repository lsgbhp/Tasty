# Tasty

* [PyMongo Doc](http://api.mongodb.com/python/current/index.html)

### 部署
* [阿里云Python+Flask](https://zhuanlan.zhihu.com/p/22126999)
* [centos install python3](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)
* centos下yum install安装的nginx没有etc/nginx/sites-available目录，可直接将配置文件放在conf.d/文件夹下，并在nginx.conf的http的block中include。[参考](https://stackoverflow.com/questions/17413526/nginx-missing-sites-available-directory)
* centos service和chkconfig命令替换为systemctl。[参考](https://cnzhx.net/blog/centos-7-rhel-7-systemd-commands/)

### MongoDB
* log  /var/log/mongodb/mongod.log
* 

### Backend-Flask

* 可以用@app.teardown_appcontext修饰一个函数，该函数会在app服务关闭时调用，是终止数据库连接的好时机。[参考](http://flask.pocoo.org/docs/0.12/tutorial/dbcon/)
* 通过request.args获取请求参数。[参考](https://segmentfault.com/q/1010000002671013)
* [mongodb关键概念解释](http://wiki.jikexueyuan.com/project/the-little-mongodb-book/the-basics.html)
* [mongodb分页](https://scalegrid.io/blog/fast-paging-with-mongodb/)

### WebApp-Vue.js






