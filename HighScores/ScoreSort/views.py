import time
from django.http import JsonResponse
from ScoreSort import models
from django.views import View

import logging
logger = logging.getLogger('django')


class GetScores(View):

    def get(self,request):
        data_status={
            'msg':'请使用Post方式提交数据'
        }
        return JsonResponse(data_status)

    def post(self,request):
        '''接受用户提交的分数值,进行存储'''
        uid=request.POST.get('uid')
        scores=request.POST.get('scores')
        logger.info(f'{uid}提交数据')
        logger.info(f'提交数据{scores}')
        logger.info('--------------------')
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        data_status = {
            'status_code': 1000,
            'msg': 'Submit Success',
            'uid': uid,
            'scores': scores,
            'post_time': now_time
        }
        if uid and scores:
            if scores.isdigit():
                if 1 < int(scores) < 10000000: # 此处数字为分数的上下限
                    models.UserScores.objects.update_or_create(uid=uid, defaults={'scores': scores})
                    data_status['uid']=uid
                    data_status['scores']=scores
                    return JsonResponse(data_status)
                else:
                    data_status['status_code']=1001 # 状态码
                    data_status['msg']='请输入范围在1-10000000内的数字'
                    return JsonResponse(data_status)
            else:
                data_status['status_code'] = 1002
                data_status['msg']='查看是否是合法的数字,是否夹带字母等?'
                return JsonResponse(data_status)
        else:
            data_status['status_code'] = 1003
            data_status['msg']='用户id或分数为空'
            return JsonResponse(data_status)


class SortScores(View):

    def get(self,request):
        data_status={
            'msg':'请使用Post方式提交数据'
        }
        return JsonResponse(data_status)

    def post(self,request):
        '''查询玩家分数排行榜'''
        uid=request.POST.get('uid')
        start_num=request.POST.get('start')
        end_num=request.POST.get('end')
        logger.info(f'{uid}查询排名')
        logger.info(f'start_num:{start_num}')
        logger.info(f'end_num:{end_num}')
        logger.info('====================')
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        data_status = {
            'status_code': 2000, 
            'msg': 'Search Success',
            'uid': uid,
            'scores': None,
            'postion':None,
            'search_time': now_time,
            'sort_scores_list':[]
        }
        uid_obj=models.UserScores.objects.filter(uid=uid)
        if not uid_obj:
            data_status['status_code']=2001 # 状态码
            data_status['msg']='请输入正确的uid'
            return JsonResponse(data_status)
        if start_num and end_num:
            if start_num.isdigit() and end_num.isdigit():
                if int(start_num)>int(end_num):
                    data_status['status_code'] = 2004
                    data_status['msg'] = 'start值需要小于end值'
                    return JsonResponse(data_status)
                start_num=int(start_num)
                obj_all = models.UserScores.objects.all().order_by('-scores')
                for k,v in enumerate(obj_all):
                    if v.uid == uid_obj[0].uid:
                        data_status['postion']=k+1
                        break
                obj_list = obj_all[int(start_num)-1:int(end_num)]
                for obj in obj_list:
                    obj_dict={}
                    obj_dict['postion']=start_num
                    obj_dict['uid']=obj.uid
                    obj_dict['scores']=obj.scores
                    data_status.get('sort_scores_list').append(obj_dict)
                    start_num+=1
                data_status['scores']=uid_obj[0].scores
                return JsonResponse(data_status)
            else:
                data_status['status_code'] = 2002
                data_status['msg'] = 'start或者end,不是合法数字'
                return JsonResponse(data_status)
        else:
            data_status['status_code'] = 2003
            data_status['msg'] = '请输入start以及end'
            return JsonResponse(data_status)
