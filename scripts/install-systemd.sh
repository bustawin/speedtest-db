echo Run as regular user!
ln networky.service ~/.config/systemd/user/
ln networky.timer ~/.config/systemd/user/
systemctl --user enable networky
systemctl --user start networky.timer
echo You should see the timer in here:
systemctl --user list-timers