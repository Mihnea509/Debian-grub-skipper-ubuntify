#!/usr/bin/env python3
import os
import subprocess
import sys

def run(cmd):
    """Run a shell command and exit if it fails"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

def check_root():
    if os.geteuid() != 0:
        print("This script must be run as root.")
        sys.exit(1)

def configure_grub():
    grub_file = "/etc/default/grub"
    # Backup original file
    run(f"cp {grub_file} {grub_file}.bak")
    # Set GRUB_TIMEOUT=0
    run(f"sed -i 's/^GRUB_TIMEOUT=.*/GRUB_TIMEOUT=0/' {grub_file}")
    # Ensure GRUB_TIMEOUT_STYLE=hidden
    if not subprocess.run(f"grep -q '^GRUB_TIMEOUT_STYLE=' {grub_file}", shell=True).returncode == 0:
        with open(grub_file, "a") as f:
            f.write("\nGRUB_TIMEOUT_STYLE=hidden\n")
    else:
        run(f"sed -i 's/^GRUB_TIMEOUT_STYLE=.*/GRUB_TIMEOUT_STYLE=hidden/' {grub_file}")
    # Set quiet splash
    if subprocess.run(f"grep -q '^GRUB_CMDLINE_LINUX_DEFAULT=' {grub_file}", shell=True).returncode == 0:
        run(f"sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash\"/' {grub_file}")
    else:
        with open(grub_file, "a") as f:
            f.write('GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"\n')

def install_plymouth():
    run("apt update -y")
    run("apt install -y plymouth plymouth-themes")
    run("plymouth-set-default-theme spinner")

def update_system():
    run("update-initramfs -u")
    run("update-grub")

def main():
    check_root()
    print("=== Configuring GRUB and Plymouth ===")
    configure_grub()
    install_plymouth()
    update_system()
    print("Done! Reboot to see the changes.")

if __name__ == "__main__":
    main()

