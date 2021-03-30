from django.urls import path
from . import views

app_name = 'performance'

urlpatterns = [
    path('goal-type', views.GoalTypeList.as_view(), name='goal_type'),
    path('add-goal-type', views.AddGoalType.as_view(), name='add_goal_type'),
    path('update-goal-type/<int:goal_type_id>', views.UpdateGoalType.as_view(), name='update_goal_type'),
    path('delete-goal-type/<int:goal_type_id>', views.RemoveGoalType.as_view(), name='remove_goal_type'),

    path('goal-list', views.GoalList.as_view(), name='goal-list'),
    path('add-goal', views.AddGoal.as_view(), name='add_goal'),
    path('update-goal/<int:goal_id>', views.UpdateGoal.as_view(), name='update_goal'),
    path('remove-goal/<int:goal_id>', views.RemoveGoal.as_view(), name='remove_goal'),


    path('training-types', views.TrainingTypeList.as_view(), name='training_types'),
    path('add-training-types', views.AddTrainingType.as_view(), name='add_training_type'),
    path('update-training-type/<int:training_type_id>', views.UpdateTrainingType.as_view(), name='update_training_type'),
    path('remove-training-type/<int:training_type_id>', views.RemoveTrainingType.as_view(), name='remove_training_type'),


    path('trainers-list', views.TrainersList.as_view(), name='trainers_list'),
    path('add-trainer', views.AddTrainer.as_view(), name='add_trainer'),
    path('update-trainer/<int:trainer_id>', views.UpdateTrainer.as_view(), name='update_trainer'),
    path('remove-trainer/<int:trainer_id>', views.RemoveTrainer.as_view(), name='remove_trainer'),


    path('training-list', views.TrainingList.as_view(), name='training_list'),

    # ajax
    path('change-status', views.ChangeStatus.as_view(), name='change_status'),
]
