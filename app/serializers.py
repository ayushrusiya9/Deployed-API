from app.models import Student
from rest_framework import serializers


# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     stu_name = serializers.CharField(max_length=50)
#     stu_email = serializers.EmailField()
#     stu_contact = serializers.IntegerField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Student` instance, given the validated data.
#         """
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Student` instance, given the validated data.
#         """
#         instance.stu_name = validated_data.get('stu_name', instance.stu_name)
#         instance.stu_email = validated_data.get('stu_email', instance.stu_email) 
#         instance.stu_contact = validated_data.get('stu_contact', instance.stu_contact)
#         instance.save()
#         return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = '__all__'