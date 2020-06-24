from import_export import fields, resources
from import_export.widgets import ManyToManyWidget

from .models import Duty, Celebrity


class DutyResource(resources.ModelResource):
    class Meta:
        model = Duty


class CelebrityResource(resources.ModelResource):
    duties = fields.Field(
        attribute='duties',
        column_name='duties',
        widget=ManyToManyWidget(Duty, field='code', separator=','))

    class Meta:
        model = Celebrity
