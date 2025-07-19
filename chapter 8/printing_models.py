def printing_models(model_orders, completed_models):
    '''simulates model printing and adds to completed queue.'''
    while model_orders:
        current_model = model_orders.pop(0)
        print(f"Printing model: {current_model.title()}")
        completed_models.append(current_model)

def show_models(completed_models):
    '''Displayiing all the printed models.'''

    print("\nThe completed models are: ")
    for index, model in enumerate(completed_models, start = 1):
        print(f"\t{index}. {model.title()}")
    print()

model_orders = ['model 1', 'model 2', 'model 3', 'model 4', 'model 5']
completed_models = []

printing_models(model_orders, completed_models)
show_models(completed_models)