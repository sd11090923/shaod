from django.db import models
from utils.get_hash import get_hash
# Create your models here.
from db.base_model import BaseModel
class PassportManager(models.Manager):
    def add_one_passport(self,username,password,email):
        passport =self.create(username=username,password=get_hash(password),email=email)
        return passport
    def get_one_passport(self,username,password):
        try:
            passport = self.get(username=username,password=get_hash(password))
        except self.model.DoesNotExist:
            passport = None
        return passport
    def check_passport(self,username):
        try:
            passport=self.get(username=username)
        except self.model.DoesNotExist:
            passport =None
        if passport:
            return True
        return False

class Passport(BaseModel):
    username=models.CharField(max_length=20,unique=True,verbose_name='用户名称')
    password=models.CharField(max_length=40,verbose_name='用户密码')
    email=models.EmailField(default=False,verbose_name='用户邮箱')
    is_active=models.BooleanField(default=False,verbose_name='激活状态')

    objects = PassportManager()

    class Meta:
        db_table='s_user_account'
class AddressManager(models.Manager):
    '''地址模型管理器类'''
    def get_default_address(self,passport_id):
        '''查询指定用户的默认收货地址'''
        try:
            addr=self.get(passport_id=passport_id,is_default=True)
        except self.model.DoesNotExist:
            addr=None
        return addr
    def add_one_address(self,passport_id,recipient_name,recipient_addr,zip_code,recipient_phone):

        '''添加收货地址'''
        #判断用户是否有默认的收货地址
        addr=self.get_default_address(passport_id=passport_id)
        if addr :
            is_default=False
        else:
            is_default=True
        addr= self.create(passport_id=passport_id,
                          recipient_name=recipient_name,
                          recipient_addr=recipient_addr,
                          zip_code=zip_code,
                          recipient_phone=recipient_phone,
                          is_default=is_default)
        return addr



class Address(BaseModel):
    '''地址模型'''
    recipient_name=models.CharField(max_length=20,verbose_name='收件人')
    recipient_addr=models.CharField(max_length=256,verbose_name='收件地址')
    recipient_phone=models.CharField(max_length=256,verbose_name='联系电话')
    zip_code=models.CharField(max_length=256,verbose_name='邮政编码')
    is_default=models.BooleanField(max_length=256,verbose_name='是否默认')
    passport=models.ForeignKey('Passport',verbose_name='账户')

    objects=AddressManager()

    class Meta:
        db_table='s_user_address'



