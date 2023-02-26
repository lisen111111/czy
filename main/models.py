#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class duzhe(BaseModel):
    __doc__ = u'''duzhe'''
    __tablename__ = 'duzhe'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    shenfenzheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身份证' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    dizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    '''
    zhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    shenfenzheng=VARCHAR
    youxiang=VARCHAR
    dizhi=VARCHAR
    '''
    class Meta:
        db_table = 'duzhe'
        verbose_name = verbose_name_plural = '读者'
class tushufenlei(BaseModel):
    __doc__ = u'''tushufenlei'''
    __tablename__ = 'tushufenlei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    fenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类' )
    '''
    fenlei=VARCHAR
    '''
    class Meta:
        db_table = 'tushufenlei'
        verbose_name = verbose_name_plural = '图书分类'
class tushuxinxi(BaseModel):
    __doc__ = u'''tushuxinxi'''
    __tablename__ = 'tushuxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tushubianhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='图书编号' )
    tushumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书名称' )
    zuozhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作者' )
    fenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类' )
    jiage=models.CharField ( max_length=255, null=True, unique=False, verbose_name='价格' )
    chubanshe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='出版社' )
    chubanriqi=models.DateField   (  null=True, unique=False, verbose_name='出版日期' )
    shuliang=models.FloatField   (  null=True, unique=False, verbose_name='数量' )
    tushutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书图片' )
    tushujianjie=models.TextField   (  null=True, unique=False, verbose_name='图书简介' )
    tushuweizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书位置' )
    '''
    tushubianhao=VARCHAR
    tushumingcheng=VARCHAR
    zuozhe=VARCHAR
    fenlei=VARCHAR
    jiage=VARCHAR
    chubanshe=VARCHAR
    chubanriqi=Date
    shuliang=Float
    tushutupian=VARCHAR
    tushujianjie=Text
    tushuweizhi=VARCHAR
    '''
    class Meta:
        db_table = 'tushuxinxi'
        verbose_name = verbose_name_plural = '图书信息'
class jieyuejilu(BaseModel):
    __doc__ = u'''jieyuejilu'''
    __tablename__ = 'jieyuejilu'



    __authTables__={'zhanghao':'duzhe',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='是'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jieyuebianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='借阅编号' )
    zuozhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作者' )
    tushumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书名称' )
    tushutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书图片' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shuliang=models.FloatField   (  null=True, unique=False, verbose_name='数量' )
    jieshuriqi=models.DateTimeField  (  null=True, unique=False, verbose_name='借书日期' )
    daoqiriqi=models.DateTimeField  (  null=True, unique=False, verbose_name='到期日期' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    jieyuebianhao=VARCHAR
    zuozhe=VARCHAR
    tushumingcheng=VARCHAR
    tushutupian=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    shuliang=Float
    jieshuriqi=DateTime
    daoqiriqi=DateTime
    beizhu=VARCHAR
    userid=BigInteger
    '''
    class Meta:
        db_table = 'jieyuejilu'
        verbose_name = verbose_name_plural = '借阅记录'
class guihaijilu(BaseModel):
    __doc__ = u'''guihaijilu'''
    __tablename__ = 'guihaijilu'



    __authTables__={'zhanghao':'duzhe',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='是'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    guihaibianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='归还编号' )
    zuozhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作者' )
    tushumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书名称' )
    tushutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书图片' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shuliang=models.FloatField   (  null=True, unique=False, verbose_name='数量' )
    jieshuriqi=models.DateField   (  null=True, unique=False, verbose_name='借书日期' )
    haishuriqi=models.DateTimeField  (  null=True, unique=False, verbose_name='还书日期' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    guihaibianhao=VARCHAR
    zuozhe=VARCHAR
    tushumingcheng=VARCHAR
    tushutupian=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    shuliang=Float
    jieshuriqi=Date
    haishuriqi=DateTime
    userid=BigInteger
    '''
    class Meta:
        db_table = 'guihaijilu'
        verbose_name = verbose_name_plural = '归还记录'
class tushuxujie(BaseModel):
    __doc__ = u'''tushuxujie'''
    __tablename__ = 'tushuxujie'



    __authTables__={'zhanghao':'duzhe',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='是'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jieyuebianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='借阅编号' )
    zuozhe=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作者' )
    tushumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书名称' )
    tushutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图书图片' )
    jieshuriqi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='借书日期' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    xujieriqi=models.DateTimeField  (  null=True, unique=False, verbose_name='续借日期' )
    xujiebeizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='续借备注' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
   # shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    jieyuebianhao=VARCHAR
    zuozhe=VARCHAR
    tushumingcheng=VARCHAR
    tushutupian=VARCHAR
    jieshuriqi=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    xujieriqi=DateTime
    xujiebeizhu=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    userid=BigInteger
    '''
    class Meta:
        db_table = 'tushuxujie'
        verbose_name = verbose_name_plural = '图书续借'
class messages(BaseModel):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='留言人id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
    cpicture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='留言图片' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    rpicture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='回复图片' )
    '''
    userid=BigInteger
    username=VARCHAR
    content=Text
    cpicture=VARCHAR
    reply=Text
    rpicture=VARCHAR
    '''
    class Meta:
        db_table = 'messages'
        verbose_name = verbose_name_plural = '留言板'
