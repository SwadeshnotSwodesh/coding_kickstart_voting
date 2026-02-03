from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Team, UserVote, VotingPasscode

def get_or_create_user_vote(request):
    if not request.session.session_key:
        request.session.create()
    user_vote, created = UserVote.objects.get_or_create(session_key=request.session.session_key)
    return user_vote

def vote_view(request):
    user_vote = get_or_create_user_vote(request)
    
    # Check if user has completed voting and is showing thank you message
    if user_vote.is_complete:
        if request.method == 'POST':
            passcode_input = request.POST.get('passcode', '').strip()
            current_passcode = VotingPasscode.get_passcode()
            
            if passcode_input == current_passcode:
                # Correct passcode entered by admin, proceed to next voter
                request.session.flush()
                return redirect('vote')
            else:
                messages.error(request, "Incorrect passcode. Please try again.")
        
        return render(request, 'vote.html', {
            'show_thank_you': True,
            'voter_name': user_vote.voter_name
        })
    
    # Check if voter name has been entered
    if not user_vote.voter_name:
        if request.method == 'POST':
            voter_name = request.POST.get('voter_name', '').strip()
            if voter_name:
                user_vote.voter_name = voter_name
                user_vote.save()
                messages.success(request, f"Welcome, {voter_name}! You can now vote.")
                return redirect('vote')
            else:
                messages.error(request, "Please enter your name to continue.")
        
        return render(request, 'vote.html', {'show_name_form': True})
    
    # Voting process
    if request.method == 'POST':
        if request.POST.get('action') == 'submit':
            # Confirm submission
            user_vote.is_complete = True
            user_vote.completed_at = timezone.now()
            user_vote.save()
            return redirect('vote')
        
        team_id = request.POST.get('team_id')
        action = request.POST.get('action')
        
        team = Team.objects.get(id=team_id)
        category = team.category
        
        if category == 'scratch':
            votes_set = user_vote.scratch_votes
        elif category == 'app_inventor':
            votes_set = user_vote.app_inventor_votes
        else:
            votes_set = user_vote.robotics_votes
        
        if action == 'vote':
            if votes_set.count() < 5:
                votes_set.add(team)
                team.votes += 1
                team.save()
                messages.success(request, f"Voted for {team.name}")
            else:
                messages.error(request, f"You can only vote for 5 teams in {category}")
        elif action == 'unvote':
            if team in votes_set.all():
                votes_set.remove(team)
                team.votes -= 1
                team.save()
                messages.success(request, f"Unvoted for {team.name}")
        
        return redirect('vote')
    
    # Get teams grouped by category
    scratch_teams = Team.objects.filter(category='scratch').order_by('-votes')
    app_inventor_teams = Team.objects.filter(category='app_inventor').order_by('-votes')
    robotics_teams = Team.objects.filter(category='robotics').order_by('-votes')
    
    # Get user's current votes
    scratch_voted = set(user_vote.scratch_votes.values_list('id', flat=True))
    app_inventor_voted = set(user_vote.app_inventor_votes.values_list('id', flat=True))
    robotics_voted = set(user_vote.robotics_votes.values_list('id', flat=True))
    
    context = {
        'scratch_teams': scratch_teams,
        'app_inventor_teams': app_inventor_teams,
        'robotics_teams': robotics_teams,
        'scratch_voted': scratch_voted,
        'app_inventor_voted': app_inventor_voted,
        'robotics_voted': robotics_voted,
        'scratch_count': user_vote.get_scratch_count(),
        'app_inventor_count': user_vote.get_app_inventor_count(),
        'robotics_count': user_vote.get_robotics_count(),
        'is_all_complete': user_vote.is_all_complete(),
        'voter_name': user_vote.voter_name,
    }
    return render(request, 'vote.html', context)
