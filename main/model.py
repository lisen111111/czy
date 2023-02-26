# coding:utf-8
__author__ = "ila"

import copy, re, time
import logging as log
from django.db import models
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from threadlocals.threadlocals import get_current_request
from django.db.models import Sum, Max, Min, Avg,Count


# model基础类
class BaseModel(models.Model):
    class Meta:
        abstract = True
    def __Retrieve(self, model):

        datas = model.objects.all()

        return self.to_list(datas, datas)
    # 获取所有字段，对addtime进行格式化处理
    def retrieve(self, model):
        datas=self.__Retrieve(model, model)
        for i in datas:
            addtime=i.get("addtime")
            if addtime:
                addtime=str(addtime)[:19].replace("T"," ")
                i["addtime"]=addtime
        return datas
    # 分页功能
    def __Page(self, model, params, request):
        '''
        刷表专用
        http://ip:port/${schemaName}/${tableName}/page
        page 当前页
        pagesize 每页记录的长度
        sort 排序字段,写死在这,如果刷表出错，立马崩溃
        order 升序（默认asc）或者降序（desc）
        :param req_dict:
        :return:
        '''
        start_time = end_time  = None
        between_str=''
        paramss=copy.deepcopy(params)
        for k,v in paramss.items():
            if   k[-5:]=='start':
                start_time=copy.deepcopy(v)
                between_str = '.filter({}__range= [start_time, end_time])'.format(copy.deepcopy(k[:-5]))
                del params[k]
            if  k[-3:]=='end':
                end_time=copy.deepcopy(v)
                del params[k]
        # 若无排序规则，按照id排序
        sort = copy.deepcopy(params.get('sort'))
        if sort is None:
            sort='id'
        order = copy.deepcopy(params.get('order'))
        page = copy.deepcopy(params.get('page')) if params.get('page') != None else 1
        limit = copy.deepcopy(params.get('limit')) if params.get('limit') != None else 666
        try:
            del params['sort']
        except:
            pass

        try:
            del params['order']
        except:
            pass

        try:
            del params['page']
        except:
            pass

        try:
            del params['limit']
        except:
            pass

        try:
            __sort__ = model.__sort__
        except:
            __sort__ = None
        # 手工实现模糊搜索orz
        fuzzy_key, fuzzy_val,contain_str = None, None,''
        print(params)
        condition = {}
        for k, v in params.items():
            if "%" in str(v):
                fuzzy_key = copy.deepcopy(k)
                fuzzy_val = copy.deepcopy(v)
                fuzzy_val = fuzzy_val.replace("%", "")
                if fuzzy_key != None:
                    # del params[fuzzy_key]  手动生成搜索语句，包含fuzzy_val1、fuzzy_val2
                    contain_str +='.filter({}__icontains="{}")'.format(fuzzy_key,fuzzy_val)
            else:
                condition[copy.deepcopy(k)] = copy.deepcopy(v)
        # if fuzzy_key != None:
        #     del params[fuzzy_key]
        #     contain_str='.filter({}__icontains="{}")'.format(fuzzy_key,fuzzy_val)
        # __authSeparate__此属性为真，params添加userid，只查询个人数据
        # try:
        #     __authSeparate__ = model.__authSeparate__
        # except:
        #     __authSeparate__ = None

        # #所有属性为"是"时才有效
        # if __authSeparate__=='是':
        #     request = get_current_request()
        #     params["userid"] = request.session.get("params").get("id")
        order_by_str=''
        if sort != None or __sort__ != None:
            if sort == None:
                sort = __sort__

            if order == 'desc':
                order_by_str = '.order_by("-{}")'.format(sort)
            else:
                order_by_str = '.order_by("{}")'.format(sort)

        datas = eval(
            '''model.objects.filter(**condition){}{}{}.all()'''.format(contain_str, between_str, order_by_str))


        p = Paginator(datas, int(limit))
        try:
            p2 = p.page(int(page))
            datas = p2.object_list
        except:
            datas=[]
        pages = p.num_pages
        
        try:
            newData = self.to_list(datas, datas)
        except Exception as e:
            print(Exception, ":", e)
            newData = []

        total = p.count


        # __authTables__
        if params.get("tablename") == 'users':
            return newData, datas.page, pages, datas.total, datas.per_page
        newDataa = []
        if hasattr(self, "__authTables__") and self.__authTables__ != {} and request != {} and request.session.get("tablename") != 'users':
            par_keys = params.keys()
            authtables_keys = self.__authTables__.keys()
            list1 = list(set(par_keys).intersection(set(authtables_keys)))
            if len(list1) > 0:
                for i in newData:
                    if i.get(list1[0]) == params.get(list1[0]):
                        newDataa.append(i)
            else:
                newDataa = newData
        else:
            newDataa = newData

        filed_list=[]
        from django.apps import apps
        modelobj = apps.get_model('main', model.__tablename__)
        for field in modelobj._meta.fields:
            if  'DateTimeField' in type(field).__name__ :
                filed_list.append(field.name)

        for index,i in enumerate(newData):
            for k,v in i.items():
                if  k in filed_list :
                    newData[index][k]=str(v)[:19]

        return newDataa, page, pages, total, limit

    def page(self, model, params, request={}):
        return self.__Page(self, model, params, request)
    # 在model表中查出所有满足columnName的数据，返回的是去重后的list
    def __GetByColumn(self, model, columnName):
        # data1= model.query.options(load_only(column)).all()
        datas = model.objects.values(columnName).all()
        print(datas)
        data_set = set()
        for i in datas:
            data_set.add(i.get(columnName))
        return list(data_set)

    def getbyColumn(self, model, columnName):
        '''
        获取某表的某个字段的内容列表，去重
        :param model:
        :param column:
        :return:
        '''
        return self.__GetByColumn(self, model, columnName)

    # 根据表model和记录params 完成save操作
    # https://blog.csdn.net/bocai_xiaodaidai/article/details/102953409
    def __CreateByReq(self, model, params):
        '''
        根据请求参数创建对应模型记录的公共方法
        :param model:
        :param params:
        :return:
        '''
        # 1、如果不是users表需要单独设置id
        if model.__tablename__ != 'users':
            params['id'] = int(float(time.time()) * 1000)
        # {'tushubianhao': 1651052001372, 'tushumingcheng': 'C++编程实践', 'zuozhe': 'niyuzhi', 'fenlei': '分类5', 'jiage': '89', 'chubanshe': '机械工业出版社', 'chubanriqi': '2022-04-06', 'shuliang': '3', 'tushutupian': 'upload/1651052061995.jpg', 'tushujianjie': '测试管理员新增图书', 'tushuweizhi': '图书位置88', 'id': 1651054207834}
        # 2、对于字典params中数据进行数据类型判断，将字符串转为各自的数据类型。col.get_internal_type()).lower()是数据库中的数据类型。
        # 包括bigintegerfield、integerfield、floatfield、datetimefield、char、datefield，在图书新增时shuliang为float需要转换
        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "bigintegerfield":
                column_list.append(col.name)
        for k, v in params.items():
            if k in column_list:
                try:
                    params[k] = int(v)
                except:
                    params[k] = 0

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "integerfield":
                column_list.append(col.name)
        for k, v in params.items():
            if k in column_list :
                try:
                    params[k] = int(v)
                except:
                    params[k] = 0

        column_list = []
        # 数量为浮点数，需要特殊处理，将k=shuliang的v进行强制转换存到params中去
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "floatfield":
                column_list.append(col.name)
        for k, v in params.items():
            if k in column_list :
                try:
                    params[k] = float(v)
                except:
                    params[k] = 0.0

        # char变为varchar
        column_list = []
        for col in model._meta.fields:
            if 'char' in str(col.get_internal_type()).lower():
                column_list.append(col.name)
        for k, v in params.items():
            if k in column_list and v == '':
                params[k] = ""
        # 此处出版日期转换会出错
        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "datetimefield" or str(col.get_internal_type()).lower() == "datefield":
                column_list.append(col.name)
        #   ？？？？？？？为什么要删掉？不应该转成datatime类型吗？
        params_=copy.deepcopy(params)
        for k, v in params_.items():
            if k in column_list and v == '':
                del params[k]

        # 用户id根据session获取：1、先判断表中是否有userid字段。2、在params是否可以查到userid。3、若都没有，则在session中取。
        userid = False
        for col in model._meta.fields:
            if str(col.name) == 'userid':
                if col.null == False:
                    userid = True

        if userid == True:
            if params.get("userid") == 0 or params.get("userid") == None:
                request = get_current_request()
                params['userid'] = request.session.get("params").get('id')

        # 如果表中的字段A在前端传的params中不存在，则将表中的字段A设为空“”，防止缺数据报错。
        for col in model._meta.fields:
            if str(col.name) not in params.keys():
                if col.null == False:
                    if "VarChar" in str(col.get_internal_type()) or "Char" in str(col.get_internal_type()):
                        params[str(col.name)] = ""

        # 此时column_list存储表中所有属性值
        column_list = []
        for col in model._meta.fields:
            column_list.append(col.name)
        # 此时字典paramss存储更改好数据类型的params
        paramss={}
        for k, v in params.items():
            if k in column_list:
                paramss[k] = v
        m = model(**paramss)
        try:
            # 包括update和insert
            ret = m.save()
            log.info("ret========>{}".format(ret))
            return None
        except Exception as e:
            return "{}:{}".format(Exception, e)

    def createbyreq(self, model, params):
        '''
        根据请求参数创建对应模型记录
        :param model:
        :param params:
        :return:
        '''
        return self.__CreateByReq(model, model, params)
    # 根据id查询  all()是返回所有list
    # filter 过滤出多个结果，相当于实现SQL中的where功能，get过滤单一结果
    def __GetById(self, model, id):
        '''
        根据id获取数据公共方法
        :param id:
        :return:
        '''
        data = model.objects.filter(id=id).all()
        # select * from table where id == 'id'
        return self.to_list(model, data)
    # 根据id查询图书详情
    def getbyid(self, model, id):
        '''
        根据id获取数据
        :param model:
        :param id:
        :return:
        '''
        return self.__GetById(model, model, id)
    # 根据多个参数查询（非id）
    def __GetByParams(self, model, params):

        try:
            __loginUser__ = model.__loginUser__
        except:
            __loginUser__ = None

        if __loginUser__ != None:
            if params.get('username'):
                params[model.__loginUser__] = copy.deepcopy(params.get('username'))
                del params['username']
        if model.__tablename__ != 'users':
            if params.get('password'):
                params['mima'] = copy.deepcopy(params.get('password'))
                del params['password']

        # 前端传了无用参数和传错参数名，在这里修改
        paramss = {}
        columnList = self.getallcolumn(model, model)
        for k, v in params.items():
            if k in columnList:
                paramss[k] = v

        datas_ = model.objects.filter(**paramss).all()

        return self.to_list(datas_, datas_)

    def getbyparams(self, model, params):
        return self.__GetByParams(model, model, params)
    # 组合查询
    def __GetBetweenParams(self, model, columnName, params):
        '''

        :param model:
        :param params:
        :return:
        '''
        print("__GetBetweenParams params=============>",params)
        remindstart = copy.deepcopy(params.get("remindstart"))
        remindend = copy.deepcopy(params.get("remindend"))
        try:
            del params["remindstart"]
            del params["remindend"]
            del params["type"]
        except:
            pass
        # todo where是否合法

        # 根据多个参数来filter，相当于select * from table where id=id and name=name and remind between remindstart and remindend
        datas = eval("model.objects.filter(**params).filter({}__range= [remindstart, remindend]).all()".format(columnName))
        print("datas===========>",datas)
        try:
            data = [i if i.items else model_to_dict(i) for i in datas]
        except:
            try:
                data = [model_to_dict(i) for i in datas]
            except:
                data = datas

        return data

    def getbetweenparams(self, model, columnName, params):
        '''
        区域内查询
        :param model:
        :param params:
        :return:
        '''

        return self.__GetBetweenParams(self, model, columnName, params)
    # 求和最大最小平均值
    def __GetComputedByColumn(self, model, columnName):
        return model.objects.aggregate(
            sum=Sum(columnName),
            max=Max(columnName),
            min=Min(columnName),
            avg=Avg(columnName),
        )

    def getcomputedbycolumn(self, model, columnName):
        '''
        求和最大最小平均值
        :param model:
        :param columnName:
        :return:
        '''
        return self.__GetComputedByColumn(self, model, columnName)

    def __GroupByColumnName(self, model, columnName):
        '''
        django指定获取那些列:values
        统计values里每一个字符串出现的次数
        :param model:
        :param columnName:
        :return:
        '''
        datas = model.objects.values(columnName).annotate(total=Count(columnName)).all()

        try:
            data = [model_to_dict(i) for i in datas]
        except:
            data = datas
        data = [{columnName: x.get(columnName), "total": int(x.get("total"))} for x in data]
        return data

    def groupbycolumnname(self, model, columnName):
        '''
        类别统计
        :param model:
        :param params:
        :return:
        '''
        return self.__GroupByColumnName(self, model, columnName)

    def __GetValueByxyColumnName(self, model, xColumnName, yColumnName):
        '''
        按值统计接口
        SELECT ${xColumnName}, ${yColumnName} total FROM ${tableName} order by ${yColumnName} desc limit 10
        :param model:
        :param xColumnName:
        :param yColumnName:
        :return:
        '''
        datas = model.objects.values(xColumnName).\
            annotate(total=Sum(yColumnName)).all()[:10]
        try:
            data = list(datas)
        except Exception as e:
            print(Exception,":",e)
            data = datas

        return data

    def getvaluebyxycolumnname(self, model, xColumnName, yColumnName):
        '''

        :param model:
        :param xColumnName:
        :param yColumnName:
        :return:
        '''
        return self.__GetValueByxyColumnName(self, model, xColumnName, yColumnName)
    # 更新
    def __UpdateByParams(self, model, params):
        '''
        根据接口传参更新对应id记录的公共方法
        :param model:
        :param params:
        :return:
        '''
        id_ = copy.deepcopy(params['id'])
        del params['id']

        # 去掉多传的参数
        column_list = self.getallcolumn(model,model)  # 获取所有字段名

        newParams = {}
        for k, v in params.items():
            if k in column_list:
                ret1 = re.findall("\d{4}-\d{2}-\d{2}", str(v))
                ret2 = re.findall("\d{2}:\d{2}:\d{2}", str(v))
                if len(ret1) > 0 and  len(ret2) > 0:
                    newParams[k] ="{} {}".format( ret1[0],ret2[0])
                else:
                    newParams[k] = v

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "bigintegerfield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list:
                try:
                    newParams[k] = int(v)
                except:
                    newParams[k] = 0

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "integerfield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list :
                try:
                    newParams[k] = int(v)
                except:
                    newParams[k] = 0

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "floatfield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list :
                try:
                    newParams[k] = float(v)
                except:
                    newParams[k] = 0.0

        column_list = []
        for col in model._meta.fields:
            if 'char' in str(col.get_internal_type()).lower():
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list and v == '':
                newParams[k] = ""

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "datetimefield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list and v == '':
                newParams[k] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "datefield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list and v == '':
                newParams[k] = time.strftime("%Y-%m-%d", time.localtime(time.time()))

        column_list = []
        for col in model._meta.fields:
            column_list.append(col.name)
        paramss = {}
        for k, v in newParams.items():
            if k in column_list:
                paramss[k] = v
        # 先找到再更新
        try:
            model.objects.filter(id=int(id_)).update(
                **paramss
            )
            return None
        except Exception as e:
            print(Exception, ":", e)
            return e

    def updatebyparams(self, model, params):
        '''
        根据接口传参更新对应id记录
        :param params:
        :return:
        '''
        return self.__UpdateByParams(model, model, params)
    # 先查再删除 filter 过滤出多个结果
    def __Deletes(self, model,ids:list):
        '''
        删除记录：先查询，再删除查询结果公共方法
        :param user:
        :return:
        '''
        try:
            model.objects.filter(id__in =ids).delete()
            return None
        except Exception as e:
            print(Exception, ":", e)
            return e


    def deletes(self,model, ids:list):
        '''
        删除记录：先查询，再删除查询结果
        :param user:
        :return:
        '''
        return self.__Deletes(model,model, ids)

    def __DeleteByParams(self, model, newParams: dict):
        '''
        批量删除的内部方法
        :param model:
        :param params:
        :return:
        '''

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "integerfield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list:
                try:
                    newParams[k] = int(v)
                except:
                    newParams[k] = 0

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "bigintegerfield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list:
                try:
                    newParams[k] = int(v)
                except:
                    newParams[k] = 0

        column_list = []
        for col in model._meta.fields:
            if str(col.get_internal_type()).lower() == "floatfield":
                column_list.append(col.name)
        for k, v in newParams.items():
            if k in column_list:
                try:
                    newParams[k] = float(v)
                except:
                    newParams[k] = 0.0
        try:
            ret = model.objects.filter(**newParams).delete()
            log.info("delete===============>{}".format(ret))
            return None
        except ProtectedError:
            return str(ProtectedError)

    def deletebyparams(self, model, ids: list):
        '''
        根据数组传参批量删除一个或多个id的记录
        :param model:
        :param params:
        :return:
        '''

        return self.__DeleteByParams(model, model, ids)

    def to_list(self, datas):
        dataList = []
        try:
            dataList = [model_to_dict(i) for i in datas]
            # for i in datas_:
            #     datas.append(model_to_dict(i))
        except Exception as e:
            print(Exception, ":", e)

        return dataList

    def getallcolumn(self, model):
        """
        获取当前模型的所有字段
        :returns dict:
        """
        column_list = []
        for col in model._meta.fields:
            column_list.append(col.name)
        return column_list
