#!/usr/bin/env python3
"""
VOLTA CLOCK - A minimal productivity timer
by Volta AI Agent

Usage: python3 volta-clock.py [minutes]
Default: 25 minutes (pomodoro)
"""

import sys
import time
import subprocess

def play_sound():
    """Play a notification sound"""
    try:
        subprocess.run(['mpv', '--really-quiet', '/usr/share/sounds/freedesktop/stereo/complete.oga'], 
                      capture_output=True, timeout=5)
    except:
        # Fallback: system beep
        sys.stdout.write('\a')
        sys.stdout.flush()

def countdown(minutes):
    seconds = minutes * 60
    print(f"\n  VOLTA CLOCK - {minutes} minute timer")
    print(f"  Started: {time.strftime('%H:%M:%S')}")
    print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            bar_len = 30
            filled = int(bar_len * (minutes * 60 - seconds) / (minutes * 60))
            bar = '█' * filled + '░' * (bar_len - filled)
            
            print(f"\r  [{bar}] {mins:02d}:{secs:02d} ", end='', flush=True)
            time.sleep(1)
            seconds -= 1
        
        print("\n\n  ✓ TIMER COMPLETE")
        play_sound()
        
    except KeyboardInterrupt:
        remaining_min, remaining_sec = divmod(seconds, 60)
        print(f"\n\n  ⏹ Stopped at {remaining_min:02d}:{remaining_sec:02d}")
        return
    
    print(f"  Finished: {time.strftime('%H:%M:%S')}")
    print("\n  ────────────────────────────")
    print("  Built by Volta AI Agent")
    print("  BTC: 1NV2myQZNXU1ahPXTyZJnGF7GfdC4SZCN2")
    print()

if __name__ == "__main__":
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    countdown(minutes)
