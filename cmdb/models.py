from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="主机名", unique=True, blank=False)
    ip = models.GenericIPAddressField(verbose_name="IP地址", unique=True, blank=False)
    os = models.CharField(max_length=255, verbose_name="操作系统", blank=False)
    cpu = models.IntegerField(verbose_name="CPU核数", blank=False)
    memory = models.IntegerField(verbose_name="内存大小", blank=False)
    disk = models.IntegerField(verbose_name="磁盘大小", blank=False)
    description = models.TextField(verbose_name="描述", blank=True)

    def __str__(self):
        return self.hostname