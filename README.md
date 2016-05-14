# 七牛jssdk客户端上传简单demo

只实现了最基本的图片上传

## 准备:

1. 注册一个七牛账号, 获取access_key, secret_key
2. 修改app.py 中的access_key, secret_key, bucket_name (存储对象)
3. 修改upload.html中的 domain

## 运行

```shell
python app.py
```

访问 `localhost:8888`


## 其他

reference:
- [jssdk doc](http://developer.qiniu.com/code/v6/sdk/javascript.html#upload)
- [python doc](http://developer.qiniu.com/code/v7/sdk/python.html), python的api 7.0之后变化较大, 官方的demo有些是用的老的接口, 请注意.

enjoy!
by: tangkikodo
