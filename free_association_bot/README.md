# follow these steps for the CTSB installation

# First start pulseaudio : 
pulseaudio -D
# Second start tmux:
tmux
# for female
python ~/workspace/api_bots/free_association_bot/daemon.py 0
# for male
python ~/workspace/api_bots/free_association_bot/daemon.py 1



