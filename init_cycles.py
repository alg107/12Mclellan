from cycle import Cycle, Notice

upstairs_bathroom = Cycle('Upstairs Bathroom', ['Nick', 'Lawrence', 'Hunter'], 'upstairs_bathroom')
downstairs_bathroom = Cycle('Downstairs Bathroom', ['Sam', 'Ashleigh', 'Jess', 'Alex'], 'downstairs_bathroom')
kitchen = Cycle('Kitchen', ['Alex', 'Jess', 'Hunter', 'Nick', 'Ashleigh', 'Lawrence', 'Sam'], 'kitchen')
notices = []
Notice.save_list(notices, "notices")
chefs = ["Jess", "Sam", "Lawrence", "Hunter", "Nick", "No one loves you :(", "Ashleigh"]
Cycle.easy_save(chefs, 'cooking_schedule')
