from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View

from system.utils import SoftDelete
from .models import *


class GoalTypeList(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        goal_types = GoalType.objects.filter(is_delete=False)
        context = {
            'goal_types': goal_types
        }
        return render(request, 'goal/goal_type.html', context)


class AddGoalType(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.POST
        goal_type = data.get('goal_type')
        description = data.get('description')
        status = data.get('status')

        obj = GoalType(goal_type=goal_type, description=description)
        obj.status = 1 if status == '1' else 0
        obj.save()

        messages.success(request, 'Goal Type added successfully. ')
        return redirect('performance:goal_type')


class UpdateGoalType(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, goal_type_id):
        obj = GoalType.objects.get(id=goal_type_id)

        data = request.POST
        goal_type = data.get('goal_type')
        description = data.get('description')
        status = data.get('status')

        obj.goal_type = goal_type
        obj.description = description
        obj.status = 1 if status == '1' else 0
        obj.save()

        messages.success(request, 'Goal Type Updated Successfully. ')
        return redirect('performance:goal_type')


class RemoveGoalType(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, goal_type_id):
        obj = GoalType.objects.get(id=goal_type_id)
        obj.is_delete = True
        obj.save()

        messages.success(request, 'GoalType removed Successfully. ')
        return redirect('performance:goal_type')

# Ajax


class ChangeStatus(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = request.GET
        goal_type_id = data.get('type_id')

        obj = GoalType.objects.get(id=goal_type_id)
        obj.status = 1 if obj.status == 0 else 0
        obj.save()

        context = {
            'updated': 'Successful'
        }
        return JsonResponse(context)

# Goal Type ENDS


class GoalList(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        goals = Goal.objects.filter(is_delete=False)
        goal_types = GoalType.objects.filter(status=1, is_delete=False)
        context = {
            'goals': goals,
            'goal_types': goal_types,
            'status_choices': list(STATUS_CHOICES),
        }
        return render(request, 'goal/goal_list.html', context)


class AddGoal(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.POST
        goal_type_id = data.get('goal_type_id')
        goal_type_obj = GoalType.objects.get(id=goal_type_id)

        subject = data.get('subject', '')
        target = data.get('target', '')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        description = data.get('description', '')
        status = data.get('status')

        goal_obj = Goal(goal_type=goal_type_obj, subject=subject, target=target, start_date=start_date,
                        end_date=end_date, description=description, status=status)
        goal_obj.save()

        messages.success(request, "Goal Added Successfully. ")
        return redirect('performance:goal-list')


class UpdateGoal(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, goal_id):
        data = request.POST
        goal_obj = Goal.objects.get(id=goal_id)

        goal_type_id = data.get('goal_type_id')
        goal_type_obj = GoalType.objects.get(id=goal_type_id)

        subject = data.get('subject', '')
        target = data.get('target', '')
        start_date = data.get('start_date')
        progress = data.get('progress')
        end_date = data.get('end_date')
        description = data.get('description', '')
        status = data.get('status')

        if start_date:
            goal_obj.start_date = start_date
        if end_date:
            goal_obj.end_date = end_date
        goal_obj.goal_type = goal_type_obj
        goal_obj.subject = subject
        goal_obj.target = target
        goal_obj.progress = progress
        goal_obj.description = description
        goal_obj.status = status
        goal_obj.save()

        messages.success(request, "Goal Updated Successfully. ")
        return redirect('performance:goal-list')


class RemoveGoal(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, goal_id):
        obj = SoftDelete.delete(Goal, goal_id)
        messages.success(request, "Goal Removed Successfully. ")
        return redirect('performance:goal-list')


class TrainingTypeList(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        training_types = TrainingType.objects.filter(is_delete=False)

        context = {
            'training_types': training_types,
            'status_choices': list(STATUS_CHOICES),
        }
        return render(request, 'training/training_types.html', context)


class AddTrainingType(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.POST
        types = data.get('type', '')
        description = data.get('description', '')
        status = data.get('status')

        obj = TrainingType(training_type=types, description=description, status=status)
        obj.save()

        messages.success(request, "Training Type added successfully. ")
        return redirect('performance:training_types')


class UpdateTrainingType(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, training_type_id):
        data = request.POST
        obj = TrainingType.objects.get(id=training_type_id)

        types = data.get('type', '')
        description = data.get('description', '')
        status = data.get('status')

        obj.training_type = types
        obj.description = description
        obj.status = status
        obj.save()

        messages.success(request, "Training Type added successfully. ")
        return redirect('performance:training_types')


class RemoveTrainingType(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, training_type_id):
        obj = SoftDelete.delete(TrainingType, training_type_id)
        messages.success(request, "Training Type Removed Successfully. ")
        return redirect('performance:training_types')


class TrainersList(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        trainers = Trainer.objects.filter(is_delete=False)

        context = {
            'trainers': trainers,
            'status_choices': list(STATUS_CHOICES),
        }
        return render(request, 'training/trainer_list.html', context)


class AddTrainer(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.POST
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        role = data.get('role', '')
        email = data.get('email', '')
        phone = data.get('phone', '')
        status = data.get('status')
        description = data.get('description', '')

        obj = Trainer(first_name=first_name, last_name=last_name, role=role,
                      email=email, phone=phone, status=status, description=description)
        obj.save()

        messages.success(request, 'Trainer Added Successfully. ')
        return redirect('performance:trainers_list')


class UpdateTrainer(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, trainer_id):
        data = request.POST
        obj = Trainer.objects.get(id=trainer_id)

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        role = data.get('role', '')
        email = data.get('email', '')
        phone = data.get('phone', '')
        status = data.get('status')
        description = data.get('description', '')

        obj.first_name = first_name
        obj.last_name = last_name
        obj.role = role
        obj.email = email
        obj.phone = phone
        obj.status = status
        obj.description = description
        obj.save()

        messages.success(request, 'Trainer Updated Successfully. ')
        return redirect('performance:trainers_list')


class RemoveTrainer(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, trainer_id):
        obj = SoftDelete.delete(Trainer, trainer_id)
        messages.success(request, "Trainer Removed Successfully. ")
        return redirect('performance:trainers_list')


class TrainingList(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        trainings = Training.objects.filter(is_delete=False)
        context = {
            'trainings': trainings,
            'status_choices': list(STATUS_CHOICES),
        }
        return render(request, 'training/training_list.html', context)

