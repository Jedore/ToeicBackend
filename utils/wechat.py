import base64
import json

from Crypto.Cipher import AES

import config


def decrypt(encrypted_data: str, iv: str, session_key: str):
    """ decrypt user info

    doc: https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/signature.html#%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE%E8%A7%A3%E5%AF%86%E7%AE%97%E6%B3%95

    :param encrypted_data: 加密数据
    :param iv: 加密算法初始向量
    :param session_key: 会话秘钥
    :return: {"openId": "OPENID",
              "nickName": "NICKNAME",
              "gender": GENDER,
              "city": "CITY",
              "province": "PROVINCE",
              "country": "COUNTRY",
              "avatarUrl": "AVATARURL",
              "unionId": "UNIONID",
              "watermark": {
                "appid":"APPID",
                "timestamp":TIMESTAMP
              }
            }
    """
    # base64 decode
    session_key = base64.b64decode(session_key)
    encrypted_data = base64.b64decode(encrypted_data)
    iv = base64.b64decode(iv)

    cipher = AES.new(session_key, AES.MODE_CBC, iv)

    decrypted = json.loads(_unpad(cipher.decrypt(encrypted_data)))

    if decrypted['watermark']['appid'] != config.APP_ID:
        raise Exception('Invalid Buffer')

    return decrypted


def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]
