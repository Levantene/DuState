from django import forms
from .models import (
    PropertyType,
    RoomsNumber,
    MasterProject,
    ProjectName,
    BuildingName
)


class RealEstateForm(forms.Form):
    master_project = forms.ModelChoiceField(
        queryset=MasterProject.objects.all(),
        widget=forms.Select(
            attrs={
                "hx-get": "load_project_names/",
                "hx-target": "#id_project_name",
                "hx-trigger": "select2.select",
                "class": "form-select form-select-sm",
                "onchange": "getProjectName();"}),
        empty_label='Community')

    project_name = forms.ModelChoiceField(
        queryset=ProjectName.objects.none(),
        widget=forms.Select(
            attrs={
                "hx-get": "load_building_names/",
                "hx-target": "#id_building_name",
                "class": "form-select form-select-sm",
                "onchange": "getBuildingName();"}))

    building_name = forms.ModelChoiceField(
        queryset=BuildingName.objects.none(),
        widget=forms.Select(
            attrs={
                # "hx-get": "load_master_projects/",
                # "hx-target": "#id_master_project",
                # "empty_label": "Choose Building Name",
                "class": "form-select form-select-sm",
                "onchange": "listBuildingName();"
                }))

    property_type = forms.ModelChoiceField(
        queryset=PropertyType.objects.all(),
        widget=forms.Select(
            attrs={
                "hx-get": "load_rooms_number/",
                "hx-target": "#id_rooms_number",
                "class": "form-select form-select-sm mt-3",
                "onchange": "getRoomsNumber();"}),
        empty_label='Property Type')

    rooms_number = forms.ModelChoiceField(
        queryset=RoomsNumber.objects.none(),
        widget=forms.Select(
            attrs={
                # "hx-get": "load_building_names/",
                # "hx-target": "#id_building_name",
                # "placeholder": "Choose type",
                "class": "form-select form-select-sm",
                "onchange": "listRoomsNumber();"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "master_project" in self.data:
            master_project = int(self.data.get("master_project"))
            self.fields["project_name"].queryset = ProjectName.objects.filter(
                realestate__master_project=master_project).distinct()

        if "project_name" in self.data:
            project_name = int(self.data.get("project_name"))
            self.fields["building_name"].queryset = (
                BuildingName.objects.filter(
                    realestate__project_name=project_name).distinct())

        if "property_type" in self.data:
            property_type = int(self.data.get("property_type"))
            self.fields["rooms_number"].queryset = (
                RoomsNumber.objects.filter(
                    realestate__property_type=property_type).distinct())
