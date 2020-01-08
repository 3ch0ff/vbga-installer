import os,sys,time,getpass

VBOX = "6.1.0"

TUSER = getpass.getuser()
if TUSER == "root":
    try:
        import pyfiglet
    except ImportError:
        os.system("pip3 install pyfiglet")
        import pyfiglet
else:
    print("no require find")

def update():
    print("update")
    os.system("wget https://download.virtualbox.org/virtualbox/{0}/VBoxGuestAdditions_{0}.iso".format(VBOX))
    os.system("sudo mount -i exec VBoxGuestAdditions_{0}.iso".format(VBOX))

def fedora():
    print("-start-fedora-installer-")
    os.system("KERN_DIR=/usr/src/kernels/`uname -r`")
    os.system("export KERN_DIR")
    os.system("wget https://download.virtualbox.org/virtualbox/{0}/VBoxGuestAdditions_{0}.iso".format(VBOX))
    os.system("sudo mount -o exec VBoxGuestAdditions_{0}.iso /mnt".format(VBOX))
    os.system("sudo sh /mnt/VBoxLinuxAdditions.run")
    print("-finish-installer-")
    os.system("clear")
    print("-now-reboot-your-system!-")

def debian():
    print("-start-debian-installer-")
    os.system("wget https://download.virtualbox.org/virtualbox/{0}/VBoxGuestAdditions_{0}.iso".format(VBOX))
    os.system("sudo mount -o exec VBoxGuestAdditions_{0}.iso /mnt".format(VBOX))
    os.system("sudo sh /mnt/VBoxLinuxAdditions.run")
    print("-finish-installer-")
    os.system("clear")
    print("-now-reboot-your-system!-")

def arch():
    print("-start-arch-installer-")
    os.system("wget https://download.virtualbox.org/virtualbox/{0}/VBoxGuestAdditions_{0}.iso".format(VBOX))
    os.system("sudo mount -o exec VBoxGuestAdditions_{0}.iso /mnt".format(VBOX))
    os.system("sudo sh /mnt/VBoxLinuxAdditions.run")
    print("-finish-installer-")
    os.system("clear")
    print("-now-reboot-your-system!-")

def pre_main():
    TUSER = getpass.getuser()
    if TUSER == "root":
        print("( OK ) root access ")
        main()
    else:
        print("( X ) root access")
        print("run this program with root privileges")

def main():
    try:
        os.system("clear")
        font_vb = pyfiglet.figlet_format("VBGA-I", font="slant")
        print("\033[0;32m" + font_vb + "\033[0;37m")
        print("[ this program work with the last version of the distro ]")
        print("-----------------------------------------")
        print("distro:                        package-manager \n")
        print(" - ubuntu                           [apt]")
        print(" - debian                           [apt]")
        print(" - arch                             [pacman]")
        print(" - fedora                           [dnf]")
        print(" - centos                           [yum]")
        print(" - update ")
        print("----------------------------------------\n")
        print("  [ by 3ch0 ] \n")
        a = input("distro name: ")
        if a == "arch":
            os.system("clear")
            os.system("pacman -Syyu")
            os.system("pacman -S dkms linux-headers base-devel")
            os.system("clear")
            arch()
        elif a == "debian" or a == "ubuntu":
            os.system("clear")
            os.system("apt update && apt dist-upgrade -y")
            os.system("apt install dkms virtualbox-guest-dkms linux-headers-(uname -r)")
            os.system("clear")
            debian()
        elif a == "fedora":
            os.system("clear")
            os.system("dnf update kernel*")
            os.system("dnf install gcc kernel-devel kernel-headers dkms make bzip2 perl libxcrypt-compat")
            os.system("clear")
            fedora()
        elif a == "centos":
            os.system("clear")
            os.system("yum update kernel*")
            os.system("yum install gcc kernel-devel kernel-headers dkms make bzip2 perl")
            os.system("clear")
            fedora()
        elif a == "exit":
            os.system("clear")
            print("goodbye!")
        elif a == "update":
            try:
                c = input("which version do you want to install?\n [ Ex: 6.1.0, 6.0.14 ] \n>> ")
                print("-start-update-")
                os.system("wget https://download.virtualbox.org/virtualbox/{0}/VBoxGuestAdditions_{0}.iso".format(c))
                os.system("sudo mount -o exec VBoxGuestAdditions_{0}.iso /mnt".format(c))
                os.system("sudo sh /mnt/VBoxLinuxAdditions.run")
                print("-finish-installer-")
                os.system("clear")
                print("-now-reboot-your-system!-")
            except KeyboardInterrupt:
                main()
        else:
            print("vbga > command not found")
            time.sleep(3)
            main()
    except KeyboardInterrupt:
        os.system("clear")
        print("goodbye!")

pre_main()
