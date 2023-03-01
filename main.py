from cryptography.fernet import Fernet

# have to generate a master password process



#function for generating key for the creation of the key file
'''
def write_key():
  key = Fernet.generate_key()
  with open('key.key', 'wb') as key_file:
    key_file.write(key)
    
write_key()
'''

create_master_pwd = input('Create a master password: ')

def load_key():
  file = open('key.key', 'rb')
  key = file.read()
  file.close
  return key

master_pwd = input('What is the master password?: ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)

  
if create_master_pwd == master_pwd:
  
  def view():
    with open('passwords.txt', 'r') as f:
      for line in f.readlines():
        data = line.rstrip()
        user, passw = data.split('|')
        print('User: ', user, '| Password: ', fer.decrypt(passw.encode()).decode()) 
  
  
  def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    with open('passwords.txt', 'a') as f:
      f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n') 
  
  
  while True:
      mode = input('Would you like to add a new password or view the existing ones (view/add)?Or press q to quit: ')
      if mode == 'q':
        break
        
      if mode == 'view':
        view()
      elif mode == 'add':
        add()
      else:
        print('Invalid mode')
        continue

else:
  print ('Incorrect master password. Quitting...')
  quit()
  