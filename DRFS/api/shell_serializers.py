
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from DRFS.api.serializers import StatusSerializer
from DRFS.models import Status

'''
Serializeing a single object.
'''
obj = Status.objects.first()
serialized_single_object = StatusSerializer(obj)
serialized_single_object.data
json_data = JSONRenderer.render(serialized_single_object)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse[stream]
print(data)

'''
Serializing a QuerySet
'''
QuerySet = Status.objects.all()
serialized_queryset = StatusSerializer(QuerySet)
json_data_queryset = JSONRenderer.render(serialized_queryset)
print(json_data_queryset)

stream = BytesIO(json_data_queryset)
data_queryset = JSONParser().parse[stream]
print(data_queryset)

'''
Creating a serialized dataset
'''
data = {'user':1,'content':'This is the third content.'}
create_serialized_data = StatusSerializer(data=data)
if create_serialized_data.is_valid():
    create_serialized_data.save()
else:
    print(create_serialized_data.errors)


'''
Updatig a serialized data set.
'''
obj = Status.objects.first()
data = {"user":1,"content":'This is the third content.'}
update_serialized_data = StatusSerializer(obj, data = data)
if update_serialized_data.is_valid():
    update_serialized_data.save()
else:
    print(update_serialized_data.errors)


'''
Deleting a serialized data.
Deletion is not possible so we can use the queryset deletion method
for deletion.
'''
obj = Status.objects.last()
obj.delete()
