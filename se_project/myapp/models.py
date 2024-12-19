
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

# โมเดลผู้ใช้ (User)
class User(AbstractUser):  # สืบทอดจาก AbstractUser
    age = models.PositiveIntegerField(null=True, blank=True)  # อายุ
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'ชาย'), ('Female', 'หญิง'), ('Other', 'อื่น ๆ')],
        null=True,
        blank=True
    )
    height = models.FloatField(null=True, blank=True)  # ส่วนสูง (เซนติเมตร)
    weight = models.FloatField(null=True, blank=True)  # น้ำหนัก (กิโลกรัม)

    def __str__(self):
        return self.username

# โมเดลบันทึกกิจกรรม (ExerciseRecord)
class ExerciseRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ความสัมพันธ์กับผู้ใช้
    exercise_type = models.CharField(max_length=100)  # ประเภทของการออกกำลังกาย (วิ่ง, ว่ายน้ำ ฯลฯ)
    duration = models.PositiveIntegerField()  # ระยะเวลา (นาที)
    calories_burned = models.FloatField()  # แคลอรี่ที่เผาผลาญ
    date = models.DateField()  # วันที่บันทึกกิจกรรม

    def __str__(self):
        return f"{self.exercise_type} - {self.user.username}"

# โมเดลเป้าหมาย (Goal)
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ความสัมพันธ์กับผู้ใช้
    target_type = models.CharField(max_length=100)  # ประเภทเป้าหมาย เช่น แคลอรี่, ระยะเวลา
    target_value = models.FloatField()  # ค่าเป้าหมาย เช่น 500 แคลอรี่
    achieved = models.BooleanField(default=False)  # บรรลุเป้าหมายหรือไม่

    def __str__(self):
        return f"{self.target_type} - {self.user.username}"

# โมเดลการแจ้งเตือน (Notification)
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ความสัมพันธ์กับผู้ใช้
    message = models.TextField()  # ข้อความการแจ้งเตือน
    date_time = models.DateTimeField(auto_now_add=True)  # วันที่และเวลาที่สร้างการแจ้งเตือน

    def __str__(self):
        return f"Notification for {self.user.username}"
