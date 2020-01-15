class tvControl:
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume = 10
        self.volumeMax= 50
        self.channelMax=30
    def power(self):
        if self.on:
            self.on - False
        else:
            self.on = True
    def increase_channel(self):
        if self.on:
            if self.channel < self.channelMax:
                self.channel +=1
    def descrease_channel(self):
        if self.on:
            if self.channel > 0:
                self.channel -= 1
    def turnUp_volume(self):
        if self.on:
            if self.volume < self.volumeMax:
                self.volume +=1
    def turnDown_volume(self):
        if self.on:
            if self.volume > 0:
                self.volume -= 1
if __name__ == "__main__":
    tv=tvControl()
    power=input('Do you want to turn on the tv? (yes) or (no)\n')
    if power == 'yes':
        tv.power()
        print('Channel: {}'.format(tv.channel))
        change_channel=input(('Do you want to change channels?(yes) or (no)\n' ))
        if change_channel == 'yes':
            n=input('Do you want to increase or decrease the channel? (up) or (down)\n')
            if n == 'up':
                up = True
                while (up == True):
                    tv.increase_channel()
                    print('Channel: {}'.format(tv.channel))
                    more =input('Increase the channel more? (yes) or (no)\n ')
                    if tv.channel == tv.channelMax:
                        print('No more channel')
                        break
                    elif more != 'yes':
                         break
            elif n == 'down':
                down = True
                while (down == True):
                    tv.descrease_channel()
                    print('Channel: {}'.format(tv.channel))
                    less =input('Lower the channel more? (yes) or (no)\n ')
                    if tv.channel < 1:
                        print('No more channel')
                        break
                    elif less != 'yes':
                         break
        print('Volume: {}'.format(tv.volume))
        change_volume=input('Would you like to change the volume ?(yes) or (no)\n')
        if change_volume == 'yes':
            n=input('Do you want to increase or decrease the volume? (up) or (down)\n')
            if n == 'up':
                up = True
                while (up == True):
                    tv.turnUp_volume()
                    print('Volume: {}'.format(tv.volume))
                    more =input('Turn the volume up more? (yes) or (no)\n ')
                    if tv.volume == tv.volumeMax:
                        print('Volume is at maximum')
                        break
                    if more != 'yes':
                         break
            elif n == 'down':
                down = True
                while (down == True):
                    tv.turnDown_volume()
                    print('Volume: {}'.format(tv.volume))
                    less =input('Turn the volume down more? (yes) or (no)\n ')
                    if tv.volume < 1 :
                        print('Volume is at minimum')
                        break
                    elif less != 'yes':
                         break





