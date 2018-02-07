# Dependencies
import config
import func
import time

# Login
func.login(config.USERNAME, config.PASSWORD)

# Check if already registered
if func.isRegistered():
  print('Είστε ήδη εγγεγραμμένοι στο επιθυμητό group.') #meaning: You've already registered for this specific lab lesson
  raise SystemExit(0)

# Register to your desired group
starttime = time.time()
tries = 1
while not func.isRegistered():
  print('%sη προσπάθεια' %(str(tries))) #meaning: Number of tries
  func.register(config.DATE['day'], config.DATE['time'])
  time.sleep((config.INTERVAL * 60.0) - ((time.time() - starttime) % (config.INTERVAL * 60.0)))
  tries += 1

# Registration Complete
print('Έχετε εγγραφεί επιτυχώς στο group που θα πραγματοποιηθεί ημέρα %s και ώρα %s.' %(config.DATE['day'], config.DATE['time'])) #meaning: You have successfully registered for your desired lab lesson
