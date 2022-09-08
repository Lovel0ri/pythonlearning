# @Time: 2022/9/8 17:27
# @Author: 李树斌
# @File : 8.4.2禁止函数修改列表.py
# @Software :PyCharm

def print_models(unprinted_designs,completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models"""
    for unprinted_design in unprinted_designs:
        current_design = unprinted_design
        print(f"正在打印该设计:{current_design}")
        completed_models.append(current_design)
    # while unprinted_designs:
    #     current_design = unprinted_designs.pop()
    #     print(f"正在打印该设计:{current_design}")
    #     completed_models.append(current_design)

def show_models(completed_models):
    """显示打印好的所有模型"""
    print(f"以下的设计都打印好了:")
    for show_model in completed_models:
        print(show_model)


unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)#[:]切片表示法创建列表副本
show_models(completed_models)
print(unprinted_designs)
