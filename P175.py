import matplotlib.pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    name = process.name()
    cpu_usage = p.cpu_percent()
    print('Name: ',name,'CPU Usage: ',cpu_usage)
    dictionary = {}
    app_name_dict.update({name:cpu_usage})
    keymax = max(app_name_dict,key=app_name_dict.get)
    print(keymax)
    keymin = min(app_name_dict,key=app_name_dict.get)
    print(keymin)
    name_list = [keymax,keymin]
    print(name_list)
    app = app_name_dict.values()
    max_app = max(app)
    print(max_app)
    min_app = min(app)
    print(min_app)
    max_min_list = [max_app,min_app]
    print(max_min_list)
    
plt.figure(figsize=(15,7))
plt.xlabel('Usage')
plt.ylabel('Applications')
plt.bar(max_min_list,name_list,width=0.6,color=('blue','yellow'))
plt.show()