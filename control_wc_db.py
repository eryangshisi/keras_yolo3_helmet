import requests
import json
import time
class SQL_WC():

    def __init__(self):
        self.WECHAT_URL = "https://api.weixin.qq.com/"
        self.APP_ID = "wx8538877d48163e8d"
        self.APP_SECRET = "8c1b0dd8e7410cf17c5cd7a3a640d37d"
        self.accessToken = self.get_access_token()
        self.ENV = "cloud-rh0km"
        self.collection = "data_test_yy" # 函数中还没有使用该变量
        self.collection_user = "User"
        self.message_id = "foMf4bZ6eaHCWFN5pLV5oR9YfxQOQMIL9flGp360RAw"

    def get_access_token(self):
        url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(self.WECHAT_URL, self.APP_ID, self.APP_SECRET)
        response = requests.get(url)
        result = response.json()
        return result['access_token']

    # =====删除数据=====
    def delete_data(self, id):
        url = '{0}tcb/databasedelete?access_token={1}'.format(self.WECHAT_URL, self.accessToken)
        query = '''db.collection("%s").doc("%s").remove()''' % (self.collection, id)

        data = {
            "env": self.ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('4.删除数据：' + response.text)

    # =======更新工人违规次数，每次调用违规次数+1========
    def WC_update_workers(self, Wnum):
        """
        :param Wnum: 工人的工号
        """
        url = '{0}tcb/databaseupdate?access_token={1}'.format(self.WECHAT_URL, self.accessToken)
        query = '''db.collection("%s").where({Wnum:"%s"}).update({data:{WnumberOfBreak: _.inc(1)}})''' % (self.collection, str(Wnum))
        data = {
            "env": self.ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        print('更新数据：' + response.text)

    # ===通过工号获取openid=====
    def WC_get_openid(self, num):
        """
        功能：通过工号获取违规人员的openid，从而能够在WC_topic_message中通知到对应登陆该账户的工人
        TODO：必须在小程序端登陆账号（工号）后获取openid，存入到User表中供给我这边调用
        【小程序端获取openid方法：https://blog.csdn.net/llayjun/article/details/78291641】
        :param num:工号
        :return:
        """
        url = "{0}tcb/databasequery?access_token={1}".format(self.WECHAT_URL, self.accessToken)
        query = '''db.collection("%s").where({_id:"%s"}).get()''' % (self.collection_user, str(num))
        data = {
            "env": self.ENV,
            "query": query
        }
        response = requests.post(url, data=json.dumps(data))
        openid = json.loads(json.loads(response.text)['data'][0])['openid']
        print('openid:' + openid)
        return openid


    def WC_topic_message(self,num):
        # foMf4bZ6eaHCWFN5pLV5oR9YfxQOQMIL9flGp360RAw
        time_key = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        url = "https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={}".format(self.accessToken)
        data = {
            "access_token": self.accessToken,
            "touser": self.WC_get_openid(num),
            "template_id": self.message_id,
            "data": {
                    "thing1": {"value": str(num)+"请佩戴安全帽"},
                    "thing2": {"value": time_key},
                    "thing3": {"value": "冠军"},
                    "thing4": {"value": "冠军"},
                    "thing5": {"value": "冠军"},
                     }
        }
        response = requests.post(url, data=json.dumps(data))
        print('xxx:' + response.text)

# if __name__ == '__main__':
#     # oemWb5X_ESvV_SdMqHlnAJ0tvUhc
#     WC = SQL_WC()
#     # for i in range(10):
#     #     print(WC.add_data())
#     # WC.update_data("5e847ab25ebca9f400df3b6113dd4abe")
#     # WC.WC_update_workers("20200303001")
#     WC.WC_topic_message("20200303003")
#     # WC.WC_get_openid("007")
