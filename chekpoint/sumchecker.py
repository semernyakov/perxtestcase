import hashlib
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import KeyCounter


def check_sum_generator(self):
    """
    Генерация контрольных сумм, c установкой сопутсвующих параметров
    """
    if self.key_code is not None:
        hashgen = hashlib.md5()
        key_code = self.key_code.encode()
        hashgen.update(key_code)
        self.check_sum = hashgen.hexdigest()
        if self.check_sum:
            self.pub_date = timezone.now()
            if not self.issue_status and self.key_counter.keys_amount:
                obj = get_object_or_404(KeyCounter, pk=self.key_counter.id)
                obj.keys_amount -= 1
                obj.save()
            self.issue_status = True
        return


def check_sum_controller(self):
    """
    Проверка контрольных сумм
    """
    hash = hashlib.md5()
    if self.key_code:
        # t = self.key_code.encode()
        hash.update(b'self')
    return hash.hexdigest()
