from django.contrib import admin
from .models import Team, UserVote, VotingPasscode

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'votes')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(VotingPasscode)
class VotingPasscodeAdmin(admin.ModelAdmin):
    list_display = ('passcode', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    
    def has_add_permission(self, request):
        # Allow adding only if there's no passcode yet
        return not VotingPasscode.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(UserVote)
class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('voter_name', 'get_scratch_count', 'get_app_inventor_count', 'get_robotics_count', 'is_complete', 'created_at')
    readonly_fields = ('session_key', 'created_at', 'completed_at', 'voter_name')
    list_filter = ('is_complete', 'created_at')
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields
        return []
