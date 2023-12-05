#!/bin/sh
sudo launchctl unload /Library/LaunchDaemons/bpw.plist || true
sudo launchctl unload /Library/LaunchDaemons/snap-agent.plist || true

sudo rm -rf /etc/snap-agent/runtime
