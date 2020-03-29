import praw
reddit = praw.Reddit('bot1')
print("Script Starting")
print ("Enter subreddit to test on")
sub = input()
subreddit = reddit.subreddit(sub)

keyphrase = '!polibot'

#check
#keywords, substitutions
#word_list = ["witnesses", "allegedly"]
#smallSubs = ["these dudes I know", "kinda probably"]

word_list         = ["witnesses", "allegedly", "study", "rebuilds", "space", "google", 
                    "smartphone", "eletric", "senator", "car", "election", "leaders",
                    "security", "comment", "debate", "driving", 
                    "poll", "candidate", "drone", "vows", "large", "successfully", "expands", 
                    "first-degree", "second-degree", "third-degree", "number", "runner",
                    "global", "years", "minutes", "indication", "horsepower", 
                    "gaffe", "ancient", "star-studded", "seen", "subway",
                    "surprising", "tension", "optimistic", "doctors", 
                    "votes",  "emails", "facebook post", "tweets", "Zuckerberg",
                    "latest", "disrupt", "meeting", "scientists",]
substitutions    = ["these dudes I know", "kinda probably", "tumblr post", "avenge", "SPAAACE", "virtual boy",
                    "pokédex", "atomic", "elf-lord", "cat", "eating contest", "river spirits", "homestar runner",
                    "is guilty and everyone knows it", "dance-off", "uncontrollably swerving", "psychic reading",
                    "airbending", "dog", "probably won't", "very large", "suddenly", "physically expands", 
                    "frigging' awful", "frigging' awful", "frigging' awful", "hundreds", "blade runner", "spherical", "minutes", 
                    "years", "lots of signs", "tons of horsemeat", "magic spell", "haunted", "blood-soaked",
                    "never found", "tunnels I found", "surprising (but not to me)",
                    "sexual tension", "delusional", "the big bang theory", "finds pokémon","poem", "poem", "poem", 
                    "this guy", "final", "destroy", "ménage à trois", "channing tatum and his friends"]
def convert(lst):
    return (lst[0].split())

def checkList(sentence):
    listSentence = [sentence]
    word = convert(listSentence)
    newSentence = ""
    #listIndex = []
    for i in range(len(word)):
        #indexPos = word_list.index(word[i])
        if word[i] in word_list:
            if word[i] == '.':
                i = i + 1
            else:
                indexPos = word_list.index(word[i])          
                newSentence += substitutions[indexPos] + " "
        else:
            newSentence += word[i] + " "
    return newSentence
    


for comment in subreddit.stream.comments():
    #checks the keyphrase to call bot
    parent = comment.parent()
    if keyphrase in comment.body:
        sentence = parent.body.replace(keyphrase, ' ')
        #attempts bots actions
        try:
            newWord = checkList(sentence)
            #print(newWord)
            comment.reply(newWord)
            print("Posted")
        except:
            print("to frequent")
                