#!/usr/bin/python
# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier

train = [
    ('I am sad', 'sad'),
    ('This is upsetting', 'sad'),
    ('I feel very good about these beers.', 'sad'),
    ('The tall slender girl looked hauntingly sad, and yet proud', 'sad'),
    ("Nobody deserves your tears, but whoever deserves them will not make you cry.", 'sad'),
    ('I do not like this restaurant', 'sad'),
    ('I am tired of this stuff.', 'sad'),
    ("I can't deal with this", 'sad'),
    ('He is my sworn enemy!', 'sad'),
    ('My boss is horrible.', 'sad'),
    ('I hate doing laundry', 'sad'),
    ('This is not a good day', 'sad'),
    ('Well, I guess I did not die in my sleep last night. :(', 'sad'),
    ('Never give up on your dreams...no matter how stupid and unattainable they clearly are.', 'sad'),
    ('Good things come to those who wait: death!', 'sad'),
    ('Your youth is gone and it is never ever returning.', 'sad'),
    ('Excluding the crushing loneliness you have no friends.', 'sad'),
    ('I would say goodnight, but we both know it is not.', 'sad'),
    ('You work a job you hate just to allow yourself to buy things you dont need.', 'sad'),
    ('People dont care enough to even make fun of you.', 'sad'),
    ('Well, I guess I didnt die in my sleep last night.  *sigh*', 'sad'),
    ('Today was just another wasted day on the inevitable journey to death.', 'sad'),
    ('Life is disappointing.', 'sad'),
    ("The majority of U.S. adults are single, so you're not alone. You're totally alone in every other way though.", 'sad'),
    ("Nothing matters. Except the fact that life is completely meaningless. And no one loves you.", 'sad'),
    ("Everything is meaningless", 'sad'),
    ("Feelings only create massive disappointment", 'sad'),
    ("Life is a cesspool of misery and despair", 'sad'),
    ("Effort is just not worth the effort", 'sad'),
    ("Life is completely and totally hopeless. Goodnight!", 'sad'),
    ("Table for one, please.", 'sad'),
    ("Taking a nap, but hoping for a coma.", 'sad'),
    ("Spoiler Alert: Someday, we'll all be dead.", 'sad'),
    ("Today is awful, tomorrow will be worse", 'sad'),
    ("Why bother?", 'sad'),
    ("If you live long enough to truly understand life, your only reward is death.", 'sad'),
    ("Good morning! Happiness is an illusion.", 'sad'),
    ("You peaked in high school and even kind of sucked then, too.", 'sad'),
    ("Starting to worry I'm not going to die young.", 'sad'),
    ("You're at rock bottom, yet somehow, it's all downhill from here.", 'sad'),
    ("The art of being happy lies in the power of extracting happiness from common things.", 'happy'),
    ("You are somebody's reason to smile.", 'happy'),
    ("I'm the most carefree, happy person you'll meet.", 'happy'),
    ("A genuinely happy person is one who has rendered others happy.", 'happy'),
    ("I think I am basically a happy person.", 'happy'),
    ("Life is better when you stop caring too much.", 'happy'),
    ("I love life", 'happy'),
    ("Today you are you! That is truer than true! There is no one alive who is youer than you!", 'happy'),
    ("The chemical process that makes you angry stays active in your system for 90 seconds, after that its up to you to choose how to be.", 'happy'),
    ("You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose", 'happy'),
    ("There may be Peace without Joy, and Joy without Peace, but the two combined make Happiness", 'happy'),
    ("One of the keys to happiness is a bad memory", 'happy'),
    ("If more of us valued food and cheer above hoarded gold, it would be a much merrier world", 'happy'),
    ("Educations purpose is to replace an empty mind with an open one", 'happy'),
    ("Happiness is when what you think, what you say, and what you do are in harmony", 'happy'),
    ("Happiness is not something you postpone for the future; it is something you design for the present.", 'happy'),
    ("Your success and happiness lies in you. Resolve to keep happy, and your joy and you shall form an invincible host against difficulties", 'happy'),
    ("Pleasure may come from illusion, but happiness can come only of reality", 'happy'),
    ("One of the keys to happiness is a bad memory", 'happy'),
    ("Happiness makes up in height for what it lacks in length", 'happy'),
    ("To be without some of the things you want is an indispensable part of happiness", 'happy'),
    ("I would maintain that thanks are the highest form of thought, and that gratitude is happiness doubled by wonder", 'happy'),
    ("The man who makes everything that leads to happiness depend upon himself... has adopted the very best plan for living happily.", 'happy'),
    ("Everyone wants to live on top of the mountain, but all the happiness and growth occurs while you're climbing it", 'happy'),
    ("Courage doesn't always roar. Sometimes courage is the quiet voice at the end of the day saying, 'I will try again tomorrow.'", 'happy'),
    ("f you tell the truth, you don't have to remember anything.", 'happy'),
    ("I have never been able to conceive how any rational being could propose happiness 2 himself from the exercise of power over others", 'happy'),
    ("Today is a good day", 'happy'),
    ("I love having a smile on my face", 'happy'),
    ("What a wonderful world", 'happy'),
    ("Life is wonderful", 'happy'),
    ("There are cool people everywhere", 'happy'),
    ("I enjoy things", 'happy'),
    ("Everythign is awesome", 'happy'),
    ("People are amazing", 'happy'),
    ("Things are all great", 'happy'),
    ("This is splendid", 'happy'),
    ("All I can do is smile", 'happy'),
    ("Everything is too amazing", 'happy'),
    ("I love all the things", 'happy'),
    ('The beer was good.', 'happy'),
    ('I do not enjoy my job', 'sad'),
    ("I ain't feeling dandy today.", 'sad'),
    ("I feel amazing!", 'happy'),
    ('Gary is a friend of mine.', 'happy'),
    ("I can't believe I'm doing this.", 'sad'),
    ("Coding is fun.", 'happy'),
    ("Dieing sucks", 'sad'),
    ("Laughing is cheerful and awesome", 'happy'),
    ("I feel bitter when being cheated", 'sad'),
    ("Skipping makes me feel delighted", 'happy'),
    ("Being hurt is a sorrowful thing", 'sad'),
    ("Making something new makes me thrilled", 'happy'),
    ("When bad things happen, I feel mournful", 'sad'),
    ("I love happy things", 'happy'),
    ("I hate horrible things", 'sad'),
    ("There are beautiful joyful enjoyable things", 'happy'),
    ("I hate it when bad things make me upset and sad", 'sad'),
    ("Happy radiant delightful things make me pleased and content", 'happy'),
    ("Miserable depressing horrible awful people make me heartbroken and unhappy", 'sad'),
    ("Life is beautiful", 'happy'),
    ("Bad sad crazy horrible wrong unpleasant stuff sucks", 'sad'),
    ("There are many beautiful thigns about my day", 'happy'),
    ("Horror painful sad bad tough events are hard", 'sad'),
    ("Fun loving beautiful awesome eventufl exciting things make my life great", 'happy'),
    ("Sad is bad", 'sad'),
    ("I enjoy doing fun stuff", 'happy'),
    ("No I hate this", 'sad'),
    ("I enjoy doing fun", 'happy'),
    ("I dont care about anything", 'sad'),
    ("Yes I love this", 'happy'),
    ("Life is tough", 'sad'),
    ("Today is wonderful", 'happy'),
    ("unhappy, sorrowful, dejected, depressed, downcast, miserable, down", 'sad'),
    ("cheerful, cheery, merry, joyful, jovial, jolly, jocular, gleeful, carefree, untroubled", 'happy'),
    ("despondent, despairing, disconsolate, desolate, wretched, glum", 'sad' ), 
    ("delighted, smiling, beaming, grinning, in good spirits, in a good mood, lighthearted", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),  
    ("pleased, contented, content, satisfied, gratified, buoyant, radiant, sunny, blithe, joyous, beatific", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),
    ("super, exciting amazing awesome great cool wonerful", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),
    ("Today is wonderful", 'happy'),
    ("unhappy, sorrowful, dejected, depressed, downcast, miserable, down", 'sad'),
    ("cheerful, cheery, merry, joyful, jovial, jolly, jocular, gleeful, carefree, untroubled", 'happy'),
    ("despondent, despairing, disconsolate, desolate, wretched, glum", 'sad' ), 
    ("delighted, smiling, beaming, grinning, in good spirits, in a good mood, lighthearted", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),  
    ("pleased, contented, content, satisfied, gratified, buoyant, radiant, sunny, blithe, joyous, beatific", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),
    ("super, exciting amazing awesome great cool wonerful", 'happy'),
    ("unhappy, sorrowful, dejected, depressed, downcast, miserable, down", 'sad'),
    ("cheerful, cheery, merry, joyful, jovial, jolly, jocular, gleeful, carefree, untroubled", 'happy'),
    ("despondent, despairing, disconsolate, desolate, wretched, glum", 'sad' ), 
    ("delighted, smiling, beaming, grinning, in good spirits, in a good mood, lighthearted", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),  
    ("pleased, contented, content, satisfied, gratified, buoyant, radiant, sunny, blithe, joyous, beatific", 'happy'),
    ("gloomy, doleful, dismal, melancholy, mournful, woebegone, forlorn, crestfallen, heartbroken, inconsolable", 'sad'),
    ("super, exciting amazing awesome great cool wonerful", 'happy'),
    ("upsetting tough shit horrible stupid awful bad", 'sad'),
    ("KICKASS kick ass bad ass awesome sweet rad bad ass fun cool", 'happy'),
    ("I love numbers and other cool things", 'happy'),
    ("KICKASS kick ass bad ass awesome sweet rad bad ass fun cool", 'happy'),
    ("I love numbers and other cool things", 'happy'),
    ("pleased, contented, content, satisfied, gratified, buoyant, radiant, sunny, blithe, joyous, beatific", 'happy'),
    ("Laughing is cheerful and awesome and cool", 'happy'),
    ("pleased, contented, content, satisfied, gratified, buoyant, radiant, sunny, blithe, joyous, beatific", 'happy'),
    ("Skipping makes me feel delighted", 'happy'),
    ("Today is a good day", 'happy'),
    ("I love having a smile on my face", 'happy'),
    ("What a wonderful world", 'happy'),
    ("Life is wonderful", 'happy'),
    ("There are cool people everywhere", 'happy'),
    ("I enjoy things", 'happy'),
    ("Everythign is awesome", 'happy'),
    ("People are amazing", 'happy'),
    ("Things are all great", 'happy'),
    ("This is splendid", 'happy'),
    ("All I can do is smile", 'happy'),
    ("Everything is too amazing", 'happy'),
    ("I love all the things", 'happy'),
    ("Today is a good day", 'happy'),
    ("I love having a smile on my face", 'happy'),
    ("What a wonderful world", 'happy'),
    ("Life is wonderful", 'happy'),
    ("There are cool people everywhere", 'happy'),
    ("I enjoy things", 'happy'),
    ("Everythign is awesome", 'happy'),
    ("People are amazing", 'happy'),
    ("Things are all great", 'happy'),
    ("This is splendid", 'happy'),
    ("All I can do is smile", 'happy'),
    ("Everything is too amazing", 'happy'),
    ("I love all the things", 'happy'),
    ("Fuuuuck fuck FUCK fuck fuck Fuuuckkkk fuckk fuck fuuckk you", 'sad'),
    ("Fake stupid lame shit tough bad horrible lame", 'sad'),
    ("I hate bad mean rude cruel shitty evil harsh devil devilish", 'sad')

]

cl = NaiveBayesClassifier(train)

#Initial Testing, no need to use
def basicAnalyzeString(testingString):
    if ':(' in testingString :
        return 'sad'
    if ': (' in testingString :
        return 'sad'
 
    return cl.classify("testingString")    
  
#Use me.  I will most accurately classify strint
def classifyString(testingString):
    prob_dist = cl.prob_classify(testingString)   
    sadChance = round(prob_dist.prob("sad"), 2)
    happyChance = round(prob_dist.prob("happy"), 2)
    
    if sadChance > happyChance:
        return 'sad' 
    else:
        return 'happy'

#If needed more details about a classification, run this
def printClassifyStringDetails(testingString):
    prob_dist = cl.prob_classify(testingString)   
    sadChance = round(prob_dist.prob("sad"), 2)
    happyChance = round(prob_dist.prob("happy"), 2)

    print testingString
    print "Sad Prob"
    print sadChance
    print
    print "Happy Prob"
    print happyChance
    return


print classifyString("I am super excited to be sponsoring and repping @ordrin! This is going to be a kick ass weekend!")
print
printClassifyStringDetails("If you know that'll make me upset, why do you do it?!")
printClassifyStringDetails("I hate when people are lame and stupid")
printClassifyStringDetails("Her heart finally told her to stop wasting her time.")
print 

