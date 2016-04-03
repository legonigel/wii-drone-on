import tweepy
import json
import random



class MyStreamListener(tweepy.StreamListener):

    def on_status(self, data):
        tooManyDir = [' Slow down crazy!',
                      ' Make up your mind...',
                      ' What am I, a miracle worker?',
                      ' No.',
                      ' That sound slike too much work',
                      ' lol no thx',
                      ' No, you pass the butter']

        tooManyRep = [' You''re not the boss of me!',
                      ' No, you pass the butter!',
                      ' You''re pushy',
                      ' Maybe if you asked nicer',
                      ' What''s the point. The further I go, the less I see',
                      ' Life? Don''t talk to me about life',
                      ' Incredible... it''s even worse than I thought it would be.']
                      


        print data.text
        user = data.author.screen_name
        users.append(data.author.screen_name)
        
        dir = data.text
        
        temp = 'not'
        ret = 'none'
        count = 0

        
        #if self.checkChoice(user, dir):
        if 'forward' in dir:
            ret = 'forward'
            count = count + 1
        if 'back' in dir:
            ret = 'back'
            count = count + 1
        if 'left' in dir:
            ret = 'left'
            count = count + 1
        if 'right' in dir:
            ret = 'right'
            count = count + 1
        if 'up' in dir:
            ret = 'up'
            count = count + 1
        if 'down' in dir:
            ret = 'down'
            count = count + 1
        if 'turn left' in dir:
            ret = 'turn left'
            count = count + 1
        if 'turn right' in dir:
            ret = 'turn right'
            count = count + 1
        #else:
            #temp = user + ' The drone that goes in one direction may never see the world'


        if 'freeze' in dir:
            temp = user + ' Freeze? I''m a robot. I''m not a refridgerator'
        if 'up up down down left right left right b a start' in dir:
            temp = user + ' The hip drone''s connected to the back drone, the back drone''s connected to the neck drone!'
        if 'barrel roll' in dir:
            temp = user + ' I can''t let you do that starfox'
        if 'captain' in dir:
            temp = user + ' Represent.'
        if 'soylent' in dir:
            temp = user + ' @soylent Drink more soylent!'
            
        sponsors = ['str software', 'dominion enterprises', 'adobe', 'mapbox', 'ellucian', 'rts labs',
                    'logapps', 'fast orientation', 'aiddata', 'whereoware', 'namecheap', 'thalmiclabs',
                    'devpost', 'google', 'cleancoders', 'twilio', 'd', 'digitalocean', 'clarifai',
                    '.tech', 'paul''s deli', 'pita pit', 'zoes kitchen', 'panera']

        if all(c in dir for c in sponsors):
            temp = user + ' Yup, that''s a sponsor.'
        

        if count > 1:
            ret = 'none'
            temp = user + random.choice(tooManyDir)
        if len(users) > 3:
            users.pop(0)
        if all(x==users[0] for x in users and len(users) >= 3):
            temp = user + random.choice(tooManyRep)
        print temp
        try:
            if temp != 'not':
                client.update_status(temp)
        except Exception, e:
            print e
        print ret
        return ret
        
        

    def on_error(self, status):
        print(status)

    def checkChoice(self, user, choice):
        if user in userChoices:
            previous_choices = userChoices[user]
            if all(choice == c for c in previous_choices) and len(previous_choices) >= 3:
                foo = False
        else:
            userChoices[user] = []
            foo = True
        userChoices[user].append(choice)
        if len(userChoices[user]) > 3:
            userChoices[user].pop(0)
        return True
                
    
        


if __name__ == '__main__':
    global user
    user = 'none'
    global userChoices
    userChoices = {}
    global repCounter
    repCounter = 0
    global users
    users = []
    
    McStreamy = MyStreamListener()
    
    auth = tweepy.OAuthHandler("thz3N9hK8ocZ6FIdNHSz5MGHS", "8XJotF8mMFcAkQaibVWA8aa1JlGv3pb7NqyyMJ9C8OciCDceSL")
    auth.set_access_token("716293351990038529-zxRvPzT2ULesb0aOT8slNOy9L0Xlink", "gTq4xRz0eiETTfuB7W6zfypYjFid3uYWSHcsgZ5vf7Aol")
    global client
    client = tweepy.API(auth)

    stream = tweepy.Stream(auth, McStreamy)
    stream.filter(track = ['@twittyDrone'])

