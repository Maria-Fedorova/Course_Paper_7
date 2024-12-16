from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import RewardOrRelatedValidator, CheckLeadTimeValidator, \
    IsPleasantNotRelatedOrRewardValidator, RelatedNotPleasantValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardOrRelatedValidator(field_1="related_habit", field_2="reward"),
            CheckLeadTimeValidator(field="lead_time"),
            RelatedNotPleasantValidator(field_1="related_habit"),
            IsPleasantNotRelatedOrRewardValidator(field_1="is_pleasant", field_2="related_habit", field_3="reward")
        ]
